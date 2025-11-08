"""Calculate the area and volume related to a circle/cylinder.

This script defines helpers to compute the base area of a circle and the
volume of a cylinder. It accepts optional command-line arguments
(`radius` and `height`). If they are not provided, it interactively
prompts the user with validation.

Usage examples:
  python task3.py 3 5        # non-interactive: radius=3, height=5
  python task3.py            # interactive prompts
"""

import argparse
import math
import sys


def cylinder_volume(r: float, h: float) -> float:
    """Return the volume of a cylinder with radius r and height h.

    V = π * r² * h
    """
    return math.pi * (r ** 2) * h


def circle_area(r: float) -> float:
    """Return the area of a circle with radius r.

    A = π * r²
    """
    return math.pi * (r ** 2)


def parse_positive_float(value: str) -> float:
    """Parse a string into a positive float or raise ValueError.

    This helper centralizes validation used both for CLI and interactive
    prompts.
    """
    try:
        f = float(value)
    except ValueError:
        raise ValueError("not a number")
    if f <= 0:
        raise ValueError("must be positive")
    return f


def prompt_for_positive(prompt: str) -> float:
    """Prompt until the user provides a valid positive float."""
    while True:
        try:
            value = input(prompt)
            return parse_positive_float(value)
        except ValueError as exc:
            print(f"Invalid input ({exc}). Please enter a positive number.")


def main(argv: list[str] | None = None) -> int:
    argv = list(argv) if argv is not None else sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="task3.py",
        description="Compute circle area and cylinder volume from radius and height.",
    )
    parser.add_argument("radius", nargs="?", help="radius of the circle/cylinder", type=float)
    parser.add_argument("height", nargs="?", help="height of the cylinder", type=float)
    args = parser.parse_args(argv)

    if args.radius is not None and args.height is not None:
        try:
            radius = parse_positive_float(str(args.radius))
            height = parse_positive_float(str(args.height))
        except ValueError as exc:
            print(f"Invalid command-line value: {exc}")
            return 2
    else:
        radius = prompt_for_positive("Enter the radius: ")
        height = prompt_for_positive("Enter the height: ")

    area = circle_area(radius)
    volume = cylinder_volume(radius, height)

    print(f"\nRadius: {radius:.4f}")
    print(f"Height: {height:.4f}")
    print(f"Base area (πr²): {area:.4f}")
    print(f"Cylinder volume (πr²h): {volume:.4f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
 