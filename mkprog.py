#!/usr/bin/env python3

# ****************************************************************************
# Description
#   Create a program source based on tmpls
#
# bugs and hints: lrsklemstein@gmail.com
# ****************************************************************************

from typing import Dict


TEMPLATE = {
    'python3_simple': """

    #!/usr/bin/env {python_prog}

    import sys


    def main():
        # your great stuff here...

        sys.exit(0)


    if __name__ == '__main__:
        main()
    """,

    'python3_argparse': """
    #!/usr/bin/env {python_prog}

    # {decoline}
    # DESCRIPTION
    #   {short_description}
    # 
    # bugs and hints: {author}
    # {decoline}

    import argparse
    import sys


    def main():
        setup = get_setup_or_exit_with_usage()

        # your great stuff here...

        sys.exit(0)


    def get_setup_or_exit_with_usage() -> argparse.Namespace:


    if __name__ == '__main__:
        main()
    """,

    'bash': """
    #!/bin/bash

    main() {
        :
        # your great stuff here
    }

    main "$@"
    """,

    'bash_complex': """
    #!/bin/bash

    {decoline}
    # DESCRIPTION
    #   {short_description}
    # 
    # bugs and hints: {author}
    {decoline}

    typeset -r PROG=${0##/}

    main() {
        # your great stuff here

        exit 0
    }

    msg() {
        echo "[$PROG]: $*" >&2
    }

    abort() {
        local rc=${0:-1}
        msg "$*"
        exit $rc
    }
    

    main "$@"
    """,
}


def main():
    tvalues = {
        'decoline' : '*' * 78,
        'author': 'lrsklemstein@gmail.com',
        'python_prog': 'python3',
        'short_description': 'Demo program to access a S3 bucket',
    }

    pt = get_tmpl('python3_argparse', tvalues)
    print(pt)


def get_tmpl(tname: str, tvalues: Dict[str, str] = {}) -> str:
    tmpl_raw = TEMPLATE[tname]

    return enrich_tmpl(strip_tmpl(unindent_tmpl(tmpl_raw)), tvalues)


def unindent_tmpl(tmpl: str, unindent_by: int = 4) -> str:
    tmpl = '\n'.join([line[unindent_by:] for line in tmpl.split('\n')])

    return tmpl


def strip_tmpl(tmpl: str) -> str:
    tmpl = tmpl.strip()
    
    return tmpl


def enrich_tmpl(tmpl: str, tvalues: Dict[str, str]) -> str:
    tmpl = tmpl.format(**tvalues)

    return tmpl


if __name__ == '__main__':
    main()
