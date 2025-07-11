import typer
import openai
import os
from dotenv import load_dotenv

app = typer.Typer()

@app.command()
def ask_ai(
    prompt: str = typer.Argument(..., help="The prompt to send to the AI model."),
    model: str = typer.Option("gpt-3.5-turbo", help="The OpenAI model to use."),
    api_key: str = typer.Option(None, help="OpenAI API key. If not provided, will use OPENAI_API_KEY env var.")
):
    """
    Ask an AI model a question and print the response.
    """
    load_dotenv()
    key = api_key or os.getenv("OPENAI_API_KEY")
    if not key:
        typer.echo("Error: OpenAI API key not provided. Use --api-key or set OPENAI_API_KEY env var.")
        raise typer.Exit(1)
    try:
        client = openai.OpenAI(api_key=key)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
# Defensive: handle None or missing content
        message = response.choices[0].message.content if response.choices and hasattr(response.choices[0].message, 'content') else None
        if message:
            typer.echo(message.strip())
        else:
            typer.echo("No response from AI model.")
    except Exception as e:
        typer.echo(f"Error: {e}")
