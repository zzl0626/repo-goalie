import os
from dotenv import load_dotenv
import openai
import typer
from goalie.github.github import GitHubClient

app = typer.Typer()

@app.command()
def write_me(
    problem_id: str = typer.Option(
        ...,
        "--id",
        help="The problem ID to write a README for"
    )
):
    """
    Generate a README for a new problem folder and optionally create a pull request.
    """
    load_dotenv()
    github_token = os.getenv("GITHUB_TOKEN")
    openai_key = os.getenv("OPENAI_API_KEY")
    if not github_token:
        typer.echo("Error: GITHUB_TOKEN not set in environment.")
        raise typer.Exit(1)
    if not openai_key:
        typer.echo("Error: OPENAI_API_KEY not set in environment.")
        raise typer.Exit(1)

    # Use test/problems/<difficulty>/<problem_id> as the problem folder
    # Search for the problem_id folder inside all subfolders of test/problems
    problems_dir = os.path.join(os.getcwd(), "problems")
    problem_folder = None
    for difficulty in os.listdir(problems_dir):
        difficulty_path = os.path.join(problems_dir, difficulty)
        if os.path.isdir(difficulty_path):
            for folder in os.listdir(difficulty_path):
                if os.path.isdir(os.path.join(difficulty_path, folder)) and folder.startswith(f"{problem_id}-"):
                    problem_folder = os.path.join(difficulty_path, folder)
                    break
        if problem_folder:
            break
    if not problem_folder:
        typer.echo(f"Problem folder not found for id '{problem_id}' in any difficulty folder under {problems_dir}")
        raise typer.Exit(1)

    # Find the main code file in the problem folder (e.g., .py file)
    code_file = None
    for f in os.listdir(problem_folder):
        if f.endswith(".py"):
            code_file = os.path.join(problem_folder, f)
            break
    if not code_file:
        typer.echo(f"No code file found in {problem_folder}")
        raise typer.Exit(1)

    with open(code_file, "r", encoding="utf-8") as f:
        code = f.read()

    # Generate README content using OpenAI
    prompt = f"Write a README for a coding problem named '{problem_id}'. Here is the solution code:\n\n{code}\n\nInclude a problem description, approach, and usage instructions."
    client = openai.OpenAI(api_key=openai_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.choices[0].message.content if response.choices and hasattr(response.choices[0].message, 'content') else None
    if not message:
        typer.echo("No response from AI model.")
        raise typer.Exit(1)
    readme_path = os.path.join(problem_folder, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(message.strip())
    typer.echo(f"README.md generated at {readme_path}")
