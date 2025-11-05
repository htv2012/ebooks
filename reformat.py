#!/usr/bin/env python3
"""
Reformat a HTML file
"""
import argparse
import textwrap

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    options = parser.parse_args()
    with open(options.file) as stream:
        content = stream.read()

    lines = content.split("<br /><br />")
    lines = (line.strip() for line in lines)
    lines = (textwrap.fill(line) for line in lines)
    content = "<br /><br />\n\n".join(lines)

    with open(options.file, "w") as stream:
        stream.write(content)


if __name__ == "__main__":
    main()

