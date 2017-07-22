import argparse
import os
import pprint

import pylev


pp = pprint.PrettyPrinter(indent=4)


def minkey(d):
    return min(d, key=d.get)


def get_strings(filename):
    '''
    Read a file containing strings separated by newlines.

    Parameters
    ----------
    filename : str
        Relative filepath containing addresses separated by newlines.

    Returns
    -------
    addresses : set
        Set containing all of the addresses found in filename.
    '''
    filepath = os.path.relpath(filename)
    addresses = set()  # Using set is faster to access than list
    f = open(filepath, 'r')
    for line in f:
        addresses.add(line.strip())
    f.close()
    return addresses


def find_distances(source, target):
    '''
    Find edit distances between two sets containing strings.

    Parameters
    ----------
    source : set
        Contains addresses loaded from the first file.
    target : set
        Contains addresses loaded from the second file.

    Returns
    -------
    matches : dict
        Contains the edit distance for each pair of addresses
        from source and target.

    '''
    matches = {}
    for s in source:
        matches[s] = {}
        if s in target:
            matches[s][s] = 0
        else:
            for t in target:
                matches[s][t] = pylev.wfi_levenshtein(s, t)
                if matches[s][t] == 0:  # Stop calculating edit distances
                    break               # once the perfect match is found
    return matches


def choose_matches(matches):
    '''
    Find the best match for each dictionary key.

    Parameters
    ----------
    matches : dict
        Contains the edit distance for each pair of addresses
        from source and target.

    Returns
    -------
    answers : dict
        Contains the closest match for each address.
    '''
    answers = {}
    for m in matches:
        answers[m] = {minkey(matches[m]): min(matches[m].values())}
    return answers


def main():
    # Build the command line interface
    parser = argparse.ArgumentParser(description='Compare strings in two files')
    parser.add_argument(
        "source_file",
        help="source file containing strings separated by newlines",
        type=str,
        )
    parser.add_argument(
        "target_file",
        help="target file containing strings separated by newlines",
        type=str,
        )
    args = parser.parse_args()

    # Calculate the edit distances
    source = get_strings(args.source_file)
    target = get_strings(args.target_file)
    distances = find_distances(source, target)

    # Show the best matches
    answers = choose_matches(distances)
    pp.pprint(answers)


if __name__ == '__main__':
    main()
