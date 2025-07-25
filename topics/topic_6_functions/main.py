"""
Implement the functions below according to the specification. Remove the `pass` statements and add your code.

Functions:
    1. fibonacci(n): list of first n Fibonacci numbers (recursive).
    2. factorial(n): n! (recursive).
    3. apply(func, seq, /, *, reverse=False): apply function to each element of seq; reverse result if needed.
    4. print_table(k, row_func, /, *, title="Table"): print k lines using row_func.

Main flow:
    • Read integer k from stdin (input()).
    • Print a "Fibonacci" table with the first k numbers.
    • Print a "Factorials" table.
    • Print result of apply(factorial, range(1, k+1), reverse=True).
"""

from typing import Callable, Iterable, List, Any


"""
How it works (step by step):
	1.	If n <= 0 → return an empty list (no numbers requested).
	2.	If n == 1 → return [1].
	3.	If n == 2 → return [1, 1].
	4.	Otherwise:
	•	Get the first n-1 numbers: prev = aleksei_fibonacci(n - 1).
	•	Compute the next number: prev[-1] + prev[-2].
	•	Append it and return the new list.

Example for n = 4:
	•	f(4) → needs f(3) → [1, 1, 2], next is 1 + 2 = 3 → [1, 1, 2, 3].
"""
def fibonacci(n: int) -> List[int]:
    """Return a list with the first *n* Fibonacci numbers (recursive)."""

    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:  # That's important because we need [last_val[-1] + last_val[-2]]
        return [1, 1]

    last_val = fibonacci(n - 1)
    return last_val + [last_val[-1] + last_val[-2]]


def factorial(n: int) -> int:
    """Return the factorial of *n* using recursion."""
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def apply(
    func: Callable[[int], Any], seq: Iterable[int], /, *, reverse: bool = False
) -> List[Any]:
    """
    Apply *func* to every element of *seq* and return the results.
    If *reverse* is True, return the list in reverse order.
    """
    pass


def print_table(
    k: int, row_func: Callable[[int], Any], /, *, title: str = "Table"
) -> None:
    """Print *k* rows generated by *row_func(i)*. The first column is the index starting from 1."""
    print(f"\n=== {title} ===")
    for i in range(1, k + 1):
        print(f"{i:>3} : {row_func(i)}")


def main() -> None:
    """Entry point for simple CLI testing."""
    try:
        k = int(input("Enter k (positive integer): "))
        if k <= 0:
            raise ValueError
    except ValueError:
        print("k must be a positive integer")
        return

    # Fibonacci table – show the *number* at position i, not the list.
    print_table(k, lambda i: fibonacci(i)[-1], title="Fibonacci")

    # Factorials table
    print_table(k, factorial, title="Factorials")


if __name__ == "__main__":
    main()
