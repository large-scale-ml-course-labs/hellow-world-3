#!/usr/bin/env python3
"""Grader for the hello-world labs.

Reads a student's output file and compares it against the expected string.
Exits with code 0 on success and 1 on failure so it can be used directly
in a GitHub Actions step.

Usage:
    python grade.py --file output.txt --expected "hellow world 1"
"""
import argparse
import os
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a student's output.txt")
    parser.add_argument("--file", default="output.txt", help="Path to the student's output file")
    parser.add_argument("--expected", required=True, help="Expected content of the file")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"::error::File '{args.file}' not found. Did you commit it?")
        return 1

    with open(args.file, encoding="utf-8") as f:
        actual = f.read().strip()

    expected = args.expected.strip()

    if actual == expected:
        print(f"✅ Correct! '{args.file}' contains exactly: {expected!r}")
        return 0

    print("❌ Wrong answer.")
    print(f"   expected: {expected!r}")
    print(f"   got:      {actual!r}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
