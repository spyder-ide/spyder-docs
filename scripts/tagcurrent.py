#!/usr/bin/env python3
"""Tag the current git branch with 'current' if not on a customizable list."""

# Standard library imports
import argparse
import os
import re
import subprocess


BRANCH_COMMAND = ["git", "branch", "--show-current", "--quiet"]
TAG_ADD_COMMAND = ["git", "tag", "-f", "-a", "current", "-m",
                   "Tag used for tracking the branch for Sphinx-Multiversion"]
TAG_DELETE_COMMAND = ["git", "tag", "-d", "current"]

CI_BRANCH_VARIABLES = [
    "BRANCH",
    "TRAVIS_PULL_REQUEST_BRANCH",
    "TRAVIS_BRANCH",
    ]


def tag_current_branch(exclude_pattern=None, verbose=False):
    """Tag the current branch if it doesn't match an exclude pattern."""
    current_branch = subprocess.run(
        BRANCH_COMMAND, check=False, stdout=subprocess.PIPE, encoding="utf-8")
    branch_name = current_branch.stdout.strip()

    # Check CI variables if not on a branch (in a detached HEAD state)
    if not branch_name and os.environ.get("CI", None):
        for branch_variable in CI_BRANCH_VARIABLES:
            branch_name = os.environ.get(branch_variable, "").strip()
            if branch_name:
                break

    if exclude_pattern and re.match(exclude_pattern, branch_name):
        if verbose:
            print(f"Current branch {branch_name!r} matches exclude pattern "
                  f"{exclude_pattern!r}, removing tag")
        subprocess.run(TAG_DELETE_COMMAND, check=False)
        return False

    if verbose:
        print(f"Adding tag to current branch {branch_name!r}")
    subprocess.run(TAG_ADD_COMMAND, check=False)
    return True


def generate_arg_parser():
    """Create and return the argument parser for the tag current script."""
    arg_parser = argparse.ArgumentParser(
        description="Tags a branch if it doesn't match an exclude pattern",
        argument_default=argparse.SUPPRESS)

    arg_parser.add_argument(
        "--exclude-pattern", help=(
            "The regex pattern of the branch(es) to not tag."
            "if not absolute; defaults to the working dir."))
    arg_parser.add_argument(
        "-v", "--verbose", action="store_true", help=(
            "If passed, prints whether the branch was tagged."))

    return arg_parser


def main(argv=None):
    """Tag the current branch if it doesn't match an exclude pattern."""
    arg_parser = generate_arg_parser()
    parsed_args = arg_parser.parse_args(argv)
    did_tag = tag_current_branch(**vars(parsed_args))
    return did_tag


if __name__ == "__main__":
    main()
