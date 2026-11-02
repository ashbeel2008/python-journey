"""Read and write the portfolio data file.

The only file that touches data/portfolio.json. Everything else asks this
module for the data.
"""

import json
import os

# portfolio-app/portfolio_core/loader.py -> go up two folders -> portfolio-app/
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DATA_FILE = os.path.join(PROJECT_ROOT, "data", "portfolio.json")

# Every portfolio file must have these keys. If one is missing we say so
# clearly instead of crashing later with a confusing KeyError.
REQUIRED_KEYS = [
    "name",
    "headline",
    "about",
    "links",
    "skills",
    "projects",
    "achievements",
]


class PortfolioError(Exception):
    """Raised when the portfolio file is missing or malformed."""


def load_portfolio(path=None):
    """Load the portfolio dict from `path` (or the default data file)."""
    path = path or DEFAULT_DATA_FILE

    if not os.path.exists(path):
        raise PortfolioError("Data file not found: " + path)

    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as error:
            raise PortfolioError(
                "Not valid JSON in " + path + ": " + str(error)
            )

    if not isinstance(data, dict):
        raise PortfolioError("Top level of " + path + " must be a JSON object")

    missing = [key for key in REQUIRED_KEYS if key not in data]
    if missing:
        raise PortfolioError("Missing required keys: " + ", ".join(missing))

    return data


def save_portfolio(data, path=None):
    """Write `data` back to `path` as readable JSON."""
    path = path or DEFAULT_DATA_FILE

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
