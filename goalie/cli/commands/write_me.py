import os
from dotenv import load_dotenv
import openai
import typer
from goalie.github.github import GitHubClient

app = typer.Typer()

@app.command()

def find_problem_folder(problem_id: str) -> str:
    problems_dir = os.path.join(os.getcwd(), "problems")
    for difficulty in os.listdir(problems_dir):
        difficulty_path = os.path.join(problems_dir, difficulty)
        if os.path.isdir(difficulty_path):
            for folder in os.listdir(difficulty_path):
                if os.path.isdir(os.path.join(difficulty_path, folder)) and folder.startswith(f"{problem_id}-"):
                    return os.path.join(difficulty_path, folder)
    typer.echo(f"Problem folder not found for id '{problem_id}' in any difficulty folder under {problems_dir}")
    raise typer.Exit(1)

def find_code_file(problem_folder: str) -> str:
    for f in os.listdir(problem_folder):
        if f.endswith(".py"):
            return os.path.join(problem_folder, f)
    typer.echo(f"No code file found in {problem_folder}")
    raise typer.Exit(1)

def read_code(code_file: str) -> str:
    with open(code_file, "r", encoding="utf-8") as f:
        return f.read()

def build_prompt(problem_id: str, code: str) -> str:
    return f"""
Write a README for a coding problem named '{problem_id}'. Here is the solution code:\n\n{code}\n\nInclude a problem description and approach
Follow this format:

# LeetCode [[Question Number]. [Question Title]](link)

---

## 1. Problem Description

### Description:
*(Briefly describe the problem in your own words or paste the problem statement here)*

---

### Input:
*(Clearly specify the input format)*

---

### Output:
*(Clearly specify the output format)*

---

### Example(s):
**Example 1:**
```

Input: ...
Output: ...

```

**Example 2:**
```

Input: ...
Output: ...

```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**
```

Input: ...
Output: ...
Explanation: *(Optional, why this case is important)*

```

**Test Case 2:**
```

Input: ...
Output: ...
Explanation: *(Optional)*

```

</details>

---

## 2. Approach

*(Step-by-step explanation of your solution. Include key decisions, patterns used, and any alternative approaches you considered.)*

- Describe the logic and flow.
- Mention why this solution is optimal or chosen.
- Note any patterns: Two Pointers, Sliding Window, Dynamic Programming, etc.
- If applicable, briefly mention brute-force or other alternative methods.

---

## 3. Algorithm Complexity

- **Time Complexity:** O(...)
- **Space Complexity:** O(...)

---

Here is an example of a high quality README for a coding problem:

# LeetCode [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

---

## 1. Problem Description

### Description:

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operation.

---

### Input:

* `s`: A string consisting of only uppercase English letters.
* `k`: An integer representing the maximum number of character replacements allowed.

---

### Output:

* An integer representing the length of the longest valid substring after at most `k` replacements.

---

### Example(s):

**Example 1:**

```
Input: s = "ABAB", k = 2
Output: 4
```

**Example 2:**

```
Input: s = "AABABBA", k = 1
Output: 4
```

---

<details>
<summary><strong>Additional Test Cases (click to expand)</strong></summary>

**Test Case 1:**

```
Input: s = "AAAA", k = 2
Output: 4
Explanation: All characters are already the same.
```

**Test Case 2:**

```
Input: s = "ABBB", k = 2
Output: 4
Explanation: Replace 'A' with 'B' to get "BBBB".
```

</details>

---

## 2. Approach

The solution uses a **Sliding Window Strategy**:

* Use a window defined by `left` and `right` pointers to scan the string.
* Maintain a frequency map of characters within the current window.
* Track the count of the most frequent character in the window.
* If the number of characters to replace (window size - max frequency) exceeds `k`, shrink the window from the left.
    *   The max frequency determines the length of the window.
    *    We do not update max frequency if the new max is lower because we dont need to check windows that are smaller than the max length we have currently found.
* The maximum window size seen during this process is the result.

This approach ensures the substring always requires at most `k` replacements to be uniform.

---

## 3. Algorithm Complexity

* **Time Complexity:** O(n), where n is the length of the string. Each character is processed at most twice.
* **Space Complexity:** O(1), since the character set is limited to 26 uppercase English letters.

---

"""

def call_openai_api(openai_key: str, prompt: str) -> str:
    client = openai.OpenAI(api_key=openai_key)
    response = client.chat.completions.create(
        model="o4-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.choices[0].message.content if response.choices and hasattr(response.choices[0].message, 'content') else None
    if not message:
        typer.echo("No response from AI model.")
        raise typer.Exit(1)
    return message.strip()

def write_readme(problem_folder: str, content: str):
    readme_path = os.path.join(problem_folder, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    typer.echo(f"README.md generated at {readme_path}")


def get_env_var(var_name: str) -> str:
    value = os.getenv(var_name)
    if not value:
        typer.echo(f"Error: {var_name} not set in environment.")
        raise typer.Exit(1)
    return value

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
    github_token = get_env_var("GITHUB_TOKEN")
    openai_key = get_env_var("OPENAI_API_KEY")
    problem_folder = find_problem_folder(problem_id)
    code_file = find_code_file(problem_folder)
    code = read_code(code_file)
    prompt = build_prompt(problem_id, code)
    readme_content = call_openai_api(openai_key, prompt)
    write_readme(problem_folder, readme_content)
