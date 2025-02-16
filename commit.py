#!/usr/bin/env python3
"""Add the next edit batch"""

import subprocess

p = subprocess.run(
    ["git", "log", "-1", "--pretty=%B"],
    capture_output=True,
    text=True,
)
num = int(p.stdout.removeprefix("ddsl")) + 1

subprocess.run(["git", "commit", "-a", "-m", f"ddsl{num}"])
