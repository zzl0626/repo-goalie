# repo-goalie

## Overview

**repo-goalie** is an automation toolkit designed to streamline the process of generating high-quality README files for coding problems, especially in competitive programming and LeetCode-style repositories. It leverages OpenAI's language models to create detailed, well-structured documentation for each problem solution, and can be integrated into CI/CD workflows to automate pull requests for new or updated READMEs.

## Features

- **Automated README Generation:** Uses OpenAI to generate comprehensive README files for coding problems based on solution code.
- **CLI Tooling:** Includes a Typer-based CLI for easy local or automated use.
- **GitHub Integration:** Supports creating branches and pull requests automatically after generating documentation.
- **Reusable GitHub Actions Workflow:** Provides a workflow that can be called from other repositories to automate README generation and PR creation.
- **Customizable Prompts:** Generates READMEs in a consistent, high-quality format with sections for problem description, approach, complexity, and examples.

## Directory Structure

```
repo-goalie/
├── goalie/
│   ├── ai/
│   ├── cli/
│   │   └── commands/
│   │       └── write_me.py
│   │       └── analyse_code.py
│   │       └── ask_ai.py
│   ├── github/
│   └── main.py
├── test/
│   └── problems/
│       └── <difficulty>/<problem-id>-<title>/
│           ├── solution.py
│           └── README.md
├── .github/
│   └── workflows/
│       └── write-me.yml
├── pyproject.toml
├── README.md
└── uv.lock
```

## Getting Started

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) for dependency management (or pip)
- OpenAI API key
- GitHub Personal Access Token (PAT) with `repo` and `workflow` scopes

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/zzl0626/repo-goalie.git
   cd repo-goalie
   ```

2. Install dependencies:
   ```sh
   uv sync
   ```

3. Set up environment variables:
   ```
   GITHUB_TOKEN=your_github_pat
   OPENAI_API_KEY=your_openai_key
   ```

### Usage

#### CLI

Generate a README for a specific problem:
```sh
uv run goalie write_me --id <problem_id>
```

#### GitHub Actions

Use the reusable workflow in `.github/workflows/write-me.yml` to automate README generation and PR creation from other repositories.

Example workflow call:
```yaml
jobs:
  call-goalie:
    uses: zzl0626/repo-goalie/.github/workflows/write-me.yml@main
    with:
      problem_id: "49"
    secrets:
      PAT_GITHUB: ${{ secrets.PAT_GITHUB }}
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

## Contributing

Contributions are welcome! Please open issues or pull requests for improvements, bug fixes, or new features.

## Future Improvements

- **Test Case Generation:** Automate the creation of diverse and meaningful test cases for each coding problem, potentially leveraging AI to suggest edge cases and validate solution robustness.

## License

MIT License