# Portfolio App

A portfolio that is itself a portfolio piece: my intro, links, skills, projects
and achievements, stored in one JSON file and rendered by Python.

Built in three stages, so nothing is throwaway:

| Stage | What | Status |
|-------|------|--------|
| 1 | Terminal version (read JSON, print sections) | done |
| 2 | Desktop GUI with Tkinter | next |
| 3 | Web version with Flask, deployed | later |

## Run it

From this folder:

```powershell
cd "C:\Users\MIRAAL FATIMA\Documents\Default Project\portfolio-app"
python main.py
```

One section only:

```powershell
python main.py projects
```

Available sections: `header`, `about`, `links`, `skills`, `projects`,
`achievements`.

## Test it

```powershell
python test_portfolio.py
```

Aim for `10/10 passing`.

## Edit your content

Everything you see comes from **`data/portfolio.json`**. Open it in VS Code and
change the text. No Python needed. Save, then run `python main.py` again.

Rules for that file:

- Keep every top-level key: `name`, `headline`, `about`, `links`, `skills`,
  `projects`, `achievements`.
- Lists (`links`, `skills`, `projects`, `achievements`) hold objects.
- A link with an empty `url` is skipped, so you can leave placeholders.
- Use `""` for empty text, not `null`.

## What to fill in first

- [ ] `location` — city/country, or leave empty
- [ ] `email` — only if you want it public
- [ ] `LinkedIn` and `YouTube` URLs, or leave them empty
- [ ] Your own words in `about` — do not leave the sample text
- [ ] Real skills with honest levels
- [ ] One project per thing you actually built

## Project layout

```
portfolio-app/
  main.py                  entry point, argument handling
  data/portfolio.json      all your content
  portfolio_core/
    loader.py              read + validate + save JSON
    display.py             turn data into text
  test_portfolio.py        tests for both
  assets/                  images later
```

Why split it up: `loader.py` knows about files, `display.py` knows about
formatting, `main.py` knows about arguments. The GUI stage will add a new
front-end and reuse the first two unchanged.

## Roadmap

- **Now** — terminal version, tested
- **Next** — Tkinter window: sidebar of sections, scrollable content
- **Then** — add a project from inside the app, saved back to JSON
- **Later** — Flask web version and a public link for the résumé

## Screenshot

_Add one after the GUI stage._
