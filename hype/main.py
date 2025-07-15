"""Main module for hype project.

This module provides a simple greet function as example.
"""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("World"))
