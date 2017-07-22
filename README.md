# pymatch

Match strings in one file to strings in another file.

## Installation

`pip install -r requirements.txt`

## Usage

`pymatch.py` will compare lines in two files and print the closest match to
`stdout`.

```sh
$ python3 pymatch.py test/foo test/bar
{   '1 JEFFERSON PKWY  APT 133': {'15 NE TANDEM WAY APT 151': 15},
    '1003 NW SHATTUCK WAY 416': {'1003 NW SHATTUCK WAY 209': 3},
    '10050 SW BARBUR BLVD': {'5000 SW 188TH PL': 11},
    '10211 N SMITH ST': {'1051 S GRANT ST': 8},
    '10630 SW PARKWOOD LN': {'8360 SW NORFOLK LN': 9},
    '10880 SW DAVIES RD # 1008': {'11549 SW DAVIES RD # 2602': 7},
    '11555 SW 155TH TER': {'11920 SW 11TH ST': 8},
    '1156 NE 73RD AVE': {'820 NW 3RD AVE': 6},
...
```

This app is not designed to show all edit distances; it is designed to show the
best matches. Once a perfect match is found, `pymatch.compare()` will move onto
the next string. Otherwise, it will compute all edit distances for that string.
This is intentional to save CPU cycles.
