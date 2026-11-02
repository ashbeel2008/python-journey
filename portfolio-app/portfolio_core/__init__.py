"""Core logic for the portfolio app.

Two jobs, kept in separate files:

- loader.py  -> read and save the data in data/portfolio.json
- display.py -> turn that data into readable text

Keeping them apart means the Tkinter window (Phase 2) can reuse loader.py
without touching display.py.
"""
