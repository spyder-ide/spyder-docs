#!/usr/bin/env python3
"""Recursively build redirects for the HTML in a given dir to an output dir."""

# Standard library imports
import argparse
import os.path
from pathlib import Path


REDIRECT_TEXT = """<!DOCTYPE html>
<html>
  <head>
    <title>Spyder IDE Documentation</title>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url={redirect_url}">
    <link rel="canonical" href="{base_url}{canonical_url}">
  </head>
</html>
"""


def generate_redirect(
        canonical_path,
        canonical_dir,
        redirect_dir="",
        base_path="",
        base_url="/"
        ):
    """Generate an individual HTML redirect from one location to another."""
    base_path = Path(base_path).resolve()
    canonical_dir = base_path / canonical_dir
    redirect_dir = base_path / redirect_dir
    if base_url[-1] != "/":
        base_url += "/"

    redirect_output_path = (
        redirect_dir / canonical_path.relative_to(canonical_dir))
    redirect_url = Path(os.path.relpath(
        canonical_path, start=redirect_output_path.parent))
    canonical_url = canonical_path.relative_to(base_path)

    output_text = REDIRECT_TEXT.format(
        redirect_url=redirect_url.as_posix(),
        base_url=base_url,
        canonical_url=canonical_url.as_posix(),
        )

    redirect_output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(redirect_output_path, mode="w",
              encoding="utf-8", newline="\n") as redirect_file:
        redirect_file.write(output_text)

    return redirect_output_path


def generate_redirects(
        canonical_dir,
        base_path="",
        match_glob="**/*.html",
        verbose=False,
        **redirect_kwargs):
    """Generate HTML redirect from one set of locations to another."""
    base_path = Path(base_path).resolve()

    redirect_paths = []
    for canonical_path in (base_path / canonical_dir).glob(match_glob):
        redirect_path = generate_redirect(
            canonical_path=canonical_path,
            canonical_dir=canonical_dir,
            base_path=base_path,
            **redirect_kwargs)
        redirect_paths.append(redirect_path)
        if verbose:
            print("Generated redirect from "
                  f"{redirect_path.relative_to(base_path).as_posix()} "
                  f"--> {canonical_path.relative_to(base_path).as_posix()}")

    return redirect_paths


def generate_arg_parser():
    """Create and return the argument parser for the redirect script."""
    arg_parser = argparse.ArgumentParser(
        description="Generate redirects given a directory of HTML files",
        argument_default=argparse.SUPPRESS)

    arg_parser.add_argument(
        "canonical_dir", help=(
            "The directory of pages to build redirects to, "
            "relative to base_dir."))
    arg_parser.add_argument(
        "--redirect-dir", help=(
            "The dir that should be redirected from and "
            "the redirect files should be written to, "
            "relative to base_path. By default, base_path."))
    arg_parser.add_argument(
        "--base-path", help=(
            "The path that canonical_dir and redirect_dir "
            "are relative to; defaults to the working dir."))
    arg_parser.add_argument(
        "--base-url", help=(
            "Full URL for the site, for use with the canonical tag."))
    arg_parser.add_argument(
        "--match-glob", help=(
            "The glob pattern to match files to redirect to "
            "in canonical_dir. By default, '**/*.html'."))
    arg_parser.add_argument(
        "-v", "--verbose", action="store_true", help=(
            "If passed, prints each redirect generated."))

    return arg_parser


def main(argv=None):
    """Generate redirects for the given directories."""
    arg_parser = generate_arg_parser()
    parsed_args = arg_parser.parse_args(argv)
    redirect_paths = generate_redirects(**vars(parsed_args))
    return redirect_paths


if __name__ == "__main__":
    main()
