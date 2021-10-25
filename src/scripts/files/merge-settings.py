#!/usr/bin/env python3
import yaml
import sys

def dict_merge(a, b, leaf_merger=None):
    """
    Recursively deep-merges two dictionaries.

    Taken from https://www.xormedia.com/recursively-merge-dictionaries-in-python/

    Arguments:
        a (dict): The dictionary to merge ``b`` into
        b (dict): The dictionary to merge into ``a``
        leaf_merger (callable): An optional callable to use to merge leaves (non-dict values)

    Returns:
        dict: ``b`` deep-merged into ``a``
    """

    from copy import deepcopy

    if a is None:
        a = dict()
    if b is None:
        b = dict()

    if not isinstance(b, dict):
        return b
    result = deepcopy(a)
    for k, v in b.items():
        if k in result and isinstance(result[k], dict):
            result[k] = dict_merge(result[k], v, leaf_merger=leaf_merger)
        else:
            merged = None
            if k in result and callable(leaf_merger):
                try:
                    merged = leaf_merger(result[k], v)
                except ValueError:
                    # can't be merged by leaf merger
                    pass

            if merged is None:
                merged = deepcopy(v)

            result[k] = merged
    return result

def merge_config_files(input_file, config_file):
    with open(input_file, mode="r", encoding="utf8") as f:
        to_merge = yaml.safe_load(f)

    with open(config_file, mode="r", encoding="utf8") as f:
        config = yaml.safe_load(f)
    
    merged = dict_merge(config, to_merge)

    with open(config_file, mode="w", encoding="utf8") as f:
        yaml.safe_dump(merged, f)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: merge-settings.py <input file> <target file>")
        sys.exit(-1)

    input_file = sys.argv[1]
    target_file = sys.argv[2]

    print(f"Merging {input_file} on {target_file}...")
    merge_config_files(input_file, target_file)
    print(f"Done!")
