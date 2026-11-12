"""A small Tkinter app for reversing integers and checking palindromes."""

import tkinter as tk
from tkinter import ttk


def parse_integer(text: str) -> int:
    """Convert user input to an integer, with a helpful validation message."""
    cleaned_text = text.strip()
    if not cleaned_text:
        raise ValueError("Please enter an integer.")

    try:
        return int(cleaned_text)
    except ValueError as error:
        raise ValueError("Please enter a valid whole number, such as 123 or -123.") from error


def reverse_integer(number: int) -> int:
    """Reverse an integer's digits while keeping its sign."""
    sign = -1 if number < 0 else 1
    reversed_digits = str(abs(number))[::-1]
    return sign * int(reversed_digits)


def is_palindrome(number: int) -> bool:
    """Return whether a non-negative integer reads the same both ways."""
    number_text = str(number)
    return number >= 0 and number_text == number_text[::-1]


def main() -> None:
    """Create and run the Number Tools window."""
    root = tk.Tk()
    root.title("Number Tools")
    root.resizable(False, False)

    content = ttk.Frame(root, padding=20)
    content.grid()

    ttk.Label(content, text="Enter an integer:").grid(
        row=0, column=0, columnspan=2, sticky="w"
    )

    number_input = ttk.Entry(content, width=32)
    number_input.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(6, 12))

    reversed_result = tk.StringVar(value="Not calculated")
    palindrome_result = tk.StringVar(value="Not calculated")
    message = tk.StringVar()

    def check_number() -> None:
        try:
            number = parse_integer(number_input.get())
        except ValueError as error:
            reversed_result.set("Not calculated")
            palindrome_result.set("Not calculated")
            message.set(str(error))
            return

        reversed_result.set(str(reverse_integer(number)))
        palindrome_result.set("Yes" if is_palindrome(number) else "No")
        message.set("")

    def clear_results() -> None:
        number_input.delete(0, tk.END)
        reversed_result.set("Not calculated")
        palindrome_result.set("Not calculated")
        message.set("")
        number_input.focus_set()

    ttk.Button(content, text="Reverse & Check", command=check_number).grid(
        row=2, column=0, sticky="ew", pady=(0, 16)
    )
    ttk.Button(content, text="Clear", command=clear_results).grid(
        row=2, column=1, sticky="ew", padx=(8, 0), pady=(0, 16)
    )

    ttk.Label(content, text="Reversed integer:").grid(row=3, column=0, sticky="w")
    ttk.Label(content, textvariable=reversed_result).grid(
        row=3, column=1, sticky="e", padx=(12, 0)
    )
    ttk.Label(content, text="Palindrome:").grid(
        row=4, column=0, sticky="w", pady=(8, 0)
    )
    ttk.Label(content, textvariable=palindrome_result).grid(
        row=4, column=1, sticky="e", padx=(12, 0), pady=(8, 0)
    )

    ttk.Label(content, textvariable=message, foreground="red", wraplength=320).grid(
        row=5, column=0, columnspan=2, sticky="w", pady=(12, 0)
    )

    root.bind("<Return>", lambda _event: check_number())
    number_input.focus_set()
    root.mainloop()


if __name__ == "__main__":
    main()
