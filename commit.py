#!/usr/bin/env python3
"""Commit the next edit batch"""

import subprocess

def main():
    p = subprocess.run(
        ["git", "log", "-1", "--pretty=%B"],
        capture_output=True,
        text=True,
    )
    num = int(p.stdout.removeprefix("ddsl")) + 1
    subprocess.run(["git", "commit", "-a", "-m", f"ddsl{num}"])
    subprocess.run(['git', 'push'])


if __name__ == '__main__':
    main()
