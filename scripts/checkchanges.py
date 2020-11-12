#!/usr/bin/env python3

import sys
import json
import argparse
import os
import os.path

from typing import Dict, Callable, Any, List, Set


VERSION = "0.0.0alpha"  #  you got the point, right?


DEFAULT_CONFIG = {
    'thresholds': {
        'max_changes': '20%',
        'max_new_files': 0,
        'max_old_files': 0
    }
}


def parse_args() -> Any:
    parser = argparse.ArgumentParser(
        description='Check if the changes between old version and new version requires a human validation')
    parser.add_argument("old", help='Base path of the old versions')
    parser.add_argument("new", help='Base path of the new versions')
    return parser.parse_args()


def main() -> None:
    is_check_ok = True
    is_changed = False

    args = parse_args()

    if not os.path.exists(args.old):
        raise RuntimeError(f"Path {args.old} does not exist")
    if not os.path.exists(args.new):
        raise RuntimeError(f"Path {args.new} does not exist")

    try:
        with open(".checkchangesconfig.json", 'r') as f:
            config = json.load(f)
    except Exception as e:
        config = DEFAULT_CONFIG
        print(f"Error loading config: {str(e)}", file=sys.stderr)

    new_files = 0
    old_files = 0

    if not config['thresholds']['max_changes'].endswith('%'):
        raise RuntimeError("Config error: threshold.max_changes should be a percentage")
    max_changes = int(config['thresholds']['max_changes'][:-1])/100

    # let's compare new files with old files
    num_new_path_toks = len(os.path.split(args.new))
    for rootdir, _, filenames in os.walk(args.new):
        root_path_toks = os.path.split(rootdir)[(num_new_path_toks-1):]
        relpath = ""
        if len(root_path_toks) > 0:
            relpath = os.path.join(*root_path_toks)

        for fname in filenames:
            new_filename = os.path.join(args.new, relpath, fname)
            old_filename = os.path.join(args.old, relpath, fname)

            if not os.path.exists(old_filename):
                new_files += 1
                print(f"Comparing {new_filename} with {old_filename}: Added")
                continue

            with open(new_filename, 'r') as nf:
                new_lines = set(nf.readlines())

            with open(old_filename, 'r') as of:
                old_lines = set(of.readlines())

            num_added_lines = len(new_lines - old_lines)
            num_removed_lines = len(old_lines - new_lines)
            num_changes = num_added_lines + num_removed_lines

            is_changed |= num_changes != 0

            if len(old_lines)*max_changes < (num_added_lines+num_removed_lines):
                print(f"Comparing {new_filename} with {old_filename}: {num_changes} changes (> max_changes threshold)")
                is_check_ok = False
                continue
            
            print(f"Comparing {new_filename} with {old_filename}: {num_changes} changes")
            
    # let's check if old files have disappeared
    num_old_path_toks = len(os.path.split(args.old))
    for rootdir, _, filenames in os.walk(args.old):
        root_path_toks = os.path.split(rootdir)[(num_old_path_toks-1):]
        relpath = ""
        if len(root_path_toks) > 0:
            relpath = os.path.join(*root_path_toks)

        for fname in filenames:
            new_filename = os.path.join(args.new, relpath, fname)
            old_filename = os.path.join(args.old, relpath, fname)

            if not os.path.exists(new_filename):
                print(f"Comparing {new_filename} with {old_filename}: Removed")
                old_files += 1

    is_changed |= new_files != 0
    is_changed |= old_files != 0

    print("")

    added_files_check = ""
    if new_files > config['thresholds']['max_new_files']:
        added_files_check = "(> threshold)"
        is_check_ok = False
    print(f"# Added files: {new_files} {added_files_check}")

    removed_files_check = ""
    if old_files > config['thresholds']['max_old_files']:
        removed_files_check = "(> threshold)"
        is_check_ok = False
    print(f"# Removed files: {old_files} {removed_files_check}")

    sys.exit(0 if is_check_ok else 1)


if __name__ == "__main__":
    main()
