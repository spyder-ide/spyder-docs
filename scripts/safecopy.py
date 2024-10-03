#!/usr/bin/env python3
"""Copy the source directory to the target dir if the target doesn't exist."""

# Standard library imports
import argparse
import shutil
from pathlib import Path


def copy_dir_if_not_existing(
    source_dir, target_dir, base_path="", verbose=False
):
    """Copy a directory to another path if the target doesn't already exist."""
    base_path = Path(base_path)
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)

    if not source_dir.is_absolute():
        source_dir = base_path / source_dir
    if not target_dir.is_absolute():
        target_dir = base_path / target_dir

    if not source_dir.exists():
        if verbose:
            print(
                f"Source directory {source_dir} doesn't exist; "
                f"skipping copy to {target_dir}"
            )
        return False
    if target_dir.exists():
        if verbose:
            print(
                f"Target directory {target_dir} exists; "
                f"skipping copy from {source_dir}"
            )
        return False
    print(f"Copying {source_dir} to {target_dir}")
    shutil.copytree(source_dir, target_dir)
    return True


def generate_arg_parser():
    """Create and return the argument parser for the safe copy script."""
    arg_parser = argparse.ArgumentParser(
        description="Copies a directory, skipping if the target exists",
        argument_default=argparse.SUPPRESS,
    )

    arg_parser.add_argument(
        "source_dir", help="The directory from which to copy"
    )
    arg_parser.add_argument(
        "target_dir", help="The directory to which to copy"
    )
    arg_parser.add_argument(
        "--base-path",
        help=(
            "The path that source_dir and target_dir are relative to "
            "if not absolute; defaults to the working dir."
        ),
    )
    arg_parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help=("If passed, prints details about the copy attempt."),
    )

    return arg_parser


def main(argv=None):
    """Copy a directory, not doing so if it isn't possible safely."""
    arg_parser = generate_arg_parser()
    parsed_args = arg_parser.parse_args(argv)
    did_copy = copy_dir_if_not_existing(**vars(parsed_args))
    return did_copy


if __name__ == "__main__":
    main()
