#!/usr/bin/python3
"""
This Script converts Markdown to HTML.
"""

import sys
import os
import re

def convert_markdown_to_html(input_file, output_file):
    """
    It converts a Markdown file to HTML and also writes the output to a file.
    """
    # Checks if the Markdown file exists and if it is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # It reads the Markdown file and converts it to HTML
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        for line in f:
            # It checks for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    # It writes the HTML output to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))

if __name__ == "__main__":
    # Checks that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # I gets the input and output file names from the command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Converts the Markdown file to HTML and writes the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit  with a successful status code
    sys.exit(0)
