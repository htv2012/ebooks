#!/usr/bin/env python3
"""Commit the next edit batch"""

from subprocess import run
import datetime


def main():
    now = datetime.datetime.now()
    message = now.strftime('Batch %Y-%m-%d %H:%M')
    run(["git", "commit", "-a", "-m", message])
    run(["git", "push"])


if __name__ == "__main__":
    main()
