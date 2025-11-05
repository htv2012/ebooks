#!/usr/bin/env python3
"""Commit the next edit batch"""

import collections
from subprocess import run
import datetime
import pathlib
import collections


def get_modified_dir():
    process = run(["git", "status", "--porcelain"], text=True, capture_output=True, check=False)
    dirs = collections.Counter(
        pathlib.Path(line.split()[-1]).parent.name
        for line in process.stdout.splitlines()
    )
    common_dir, count =  dirs.most_common(1)[0]
    return common_dir

def main():
    modified_dir  = get_modified_dir()
    now = datetime.datetime.now()
    message = modified_dir + now.strftime(' %Y-%m-%d %H:%M')
    run(["git", "commit", "-a", "-m", message])
    run(["git", "push"])


if __name__ == "__main__":
    main()
