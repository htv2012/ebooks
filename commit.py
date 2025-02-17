#!/usr/bin/env python3
"""Commit the next edit batch"""

from subprocess import run


def main():
    p = run(["git", "log", "-1", "--pretty=%B"], capture_output=True)
    num = int(p.stdout.removeprefix(b"batch ")) + 1
    run(["git", "commit", "-a", "-m", f"batch {num}"])
    run(["git", "push"])


if __name__ == "__main__":
    main()
