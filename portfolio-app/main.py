"""Portfolio app — entry point.

Run all sections:

    python main.py

Run one section:

    python main.py projects

Use a different data file (useful for testing):

    python main.py --file=data/example.json
"""

import sys

from portfolio_core import display, loader

HELP = """Portfolio app

Usage:
    python main.py                 show everything
    python main.py <section>       show one section
    python main.py --file=PATH     use another JSON file
    python main.py --help          show this message

Sections:
    header, about, links, skills, projects, achievements
"""


def main(args):
    path = None
    section = None

    for arg in args:
        if arg in ("-h", "--help"):
            print(HELP)
            return 0
        if arg.startswith("--file="):
            path = arg.split("=", 1)[1]
        elif arg in display.SECTIONS:
            section = arg
        else:
            print("Unknown argument: " + arg)
            print()
            print(HELP)
            return 2

    try:
        data = loader.load_portfolio(path)
    except loader.PortfolioError as error:
        print("Error: " + str(error))
        return 1

    print()
    if section:
        print(display.render_section(data, section))
    else:
        print(display.render_all(data))
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
