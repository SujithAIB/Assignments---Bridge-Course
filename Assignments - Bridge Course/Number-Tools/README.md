# Number Tools

Number Tools is a beginner-friendly Python application that reverses an integer and checks whether it is a palindrome. It includes a small graphical interface built with Tkinter.

## Features

- Reverse positive and negative integer digits while keeping the sign.
- Check whether a non-negative integer reads the same forward and backward.
- Validate empty and invalid input with a clear message.
- Clear the input and results with one button.
- Press Enter to run the check.

## Technologies

- Python 3
- Tkinter (Python standard library)

No third-party Python packages are needed. `requirements.txt` documents this.

## Run the application

Open a terminal in the `Number-Tools` folder and run:

```text
python main.py
```

On some Windows installations, use `py main.py` instead. A Python installation with Tkinter available is required.

## Sample results

| Input | Reversed integer | Palindrome |
| --- | ---: | :---: |
| `121` | `121` | Yes |
| `12321` | `12321` | Yes |
| `12345` | `54321` | No |
| `0` | `0` | Yes |
| `7` | `7` | Yes |
| `-121` | `-121` | No |

Empty input displays “Please enter an integer.” Non-numeric input displays a message asking for a valid whole number.

## How the palindrome check works

The application converts the entered integer to text and compares that text with its reverse. For example, `"12321"` equals `"12321"[::-1]`, so it is a palindrome. Negative numbers are not palindromes because the minus sign makes the complete value read differently in reverse.

## GitHub Copilot assignment evidence

The project files do not claim Copilot actions that have not been performed. To capture your own evidence in VS Code:

1. **Inline suggestion:** Open `main.py`, add a small function stub such as `def format_result(number):`, and ask Copilot Inline Completions to complete it. Review and accept a meaningful suggestion with Tab (or the shortcut configured in your VS Code). Keep the accepted, useful code in the project. Capture the editor with the accepted code visible.
2. **Chat Edit:** Select an existing section in `main.py`, open Copilot Chat's **Edit** workflow, and request a focused improvement, such as adding a reset button or improving invalid-input feedback. Review and apply the edit, then capture the application running with a result visible.

Use your real VS Code screenshots; do not present generated or simulated screenshots as Copilot evidence.

## Publish to GitHub

Create a public repository named `Number-Tools` in your GitHub account, then add this folder's files and push them using the GitHub workflow available in VS Code or Git. The repository link and screenshots must come from your own account and session.
