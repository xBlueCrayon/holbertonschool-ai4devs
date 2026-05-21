# Setup Notes

## Development Environment Setup

### IDE Installation

The development environment was configured using Visual Studio Code as the primary IDE for AI-assisted coding and testing.

**IDE Used:**  
- Visual Studio Code

**Version:**  
- VS Code 1.99 or later

---

## AI Coding Assistant Setup

### GitHub Copilot Installation

GitHub Copilot was installed as the AI coding assistant to support code generation, debugging, refactoring, and documentation tasks.

### Installation Steps

1. Open Visual Studio Code.
2. Navigate to the Extensions Marketplace.
3. Search for:
   - GitHub Copilot
4. Click Install.
5. Sign in using a GitHub account with Copilot access enabled.
6. Restart VS Code after installation.

---

## Extensions Installed

### Core Extensions

- GitHub Copilot
- GitHub Copilot Chat
- Python Extension Pack
- Prettier - Code Formatter
- ESLint
- C/C++ Extension

### Purpose of Extensions

| Extension | Purpose |
|---|---|
| GitHub Copilot | AI code suggestions |
| Copilot Chat | AI debugging and explanations |
| Python Extension | Python language support |
| Prettier | Code formatting |
| ESLint | JavaScript linting |
| C/C++ Extension | C language support |

---

## Environment Configuration

### Programming Languages Used

- Python 3.12
- JavaScript (Node.js)
- C (GCC Compiler)

### Installed Tool Versions

| Tool | Version |
|---|---|
| Python | 3.12 |
| Node.js | 20.x |
| GCC | 13.x |
| Git | 2.49+ |

---

## Git Configuration

Git was configured for version control and GitHub repository synchronization.

### Commands Used

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Repository Setup

```bash
git clone https://github.com/xBlueCrayon/holbertonschool-ai4devs.git
```

---

## Testing Environment

### Python Testing

```bash
python filename.py
```

### JavaScript Testing

```bash
node filename.js
```

### C Program Compilation

```bash
gcc filename.c -o output
./output
```

---

## AI Productivity Workflow

The AI assistant was used for:
- Debugging code errors
- Explaining runtime exceptions
- Refactoring code
- Generating documentation
- Creating test cases
- Producing architecture and API specifications

Manual verification and testing were performed after each AI-generated suggestion to ensure correctness and compatibility with project requirements.

---

## Notes and Observations

- AI-assisted coding significantly reduced debugging time.
- Manual validation remained important for formatting and edge cases.
- GitHub Copilot was most effective for repetitive coding tasks and documentation generation.
- Combining AI suggestions with human review improved overall code quality and reliability.