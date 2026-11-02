"""Turn portfolio data into readable terminal text.

This module only decides how things look. It never reads files.
That separation is why the same data can later feed a Tkinter window.
"""

import textwrap

LINE = "=" * 62
WIDTH = 76


def _text(value):
    """Return a clean string, safe for None and stray whitespace."""
    if value is None:
        return ""
    return str(value).strip()


def _wrap(value, indent=""):
    """Word-wrap a paragraph, keeping `indent` on every line."""
    text = _text(value)
    if not text:
        return []
    return textwrap.wrap(
        text,
        width=WIDTH,
        initial_indent=indent,
        subsequent_indent=indent,
    )


def _heading(title):
    return "\n" + LINE + "\n" + title.upper() + "\n" + LINE


def render_header(data):
    lines = [_heading("portfolio")]
    lines.append((_text(data.get("name")) or "(no name)").upper())

    headline = _text(data.get("headline"))
    if headline:
        lines.append(headline)

    details = []
    location = _text(data.get("location"))
    email = _text(data.get("email"))
    if location:
        details.append(location)
    if email:
        details.append(email)
    if details:
        lines.append(" | ".join(details))

    return "\n".join(lines)


def render_about(data):
    lines = [_heading("about")]
    lines.extend(_wrap(data.get("about")) or ["(empty)"])
    return "\n".join(lines)


def render_links(data):
    lines = [_heading("links")]
    shown = 0

    for link in data.get("links") or []:
        label = _text(link.get("label")) or "Link"
        url = _text(link.get("url"))
        if not url:
            continue  # skip empty placeholders instead of printing blank lines
        lines.append(label.ljust(14) + url)
        shown += 1

    if shown == 0:
        lines.append("(no links yet)")

    return "\n".join(lines)


def render_skills(data):
    lines = [_heading("skills")]
    shown = 0

    for skill in data.get("skills") or []:
        name = _text(skill.get("name"))
        if not name:
            continue
        lines.append(name.ljust(20) + _text(skill.get("level")))
        shown += 1

    if shown == 0:
        lines.append("(no skills yet)")

    return "\n".join(lines)


def render_projects(data):
    lines = [_heading("projects")]
    projects = data.get("projects") or []

    if not projects:
        lines.append("(no projects yet)")
        return "\n".join(lines)

    for number, project in enumerate(projects, start=1):
        title = _text(project.get("title")) or "(untitled)"
        status = _text(project.get("status"))

        head = str(number) + ". " + title
        if status:
            head += "  [" + status + "]"
        lines.append(head)

        lines.extend(_wrap(project.get("description"), indent="   "))

        url = _text(project.get("url"))
        if url:
            lines.append("   " + url)

        tags = project.get("tags") or []
        if tags:
            lines.append("   tags: " + ", ".join(str(tag) for tag in tags))

        lines.append("")

    if lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


def render_achievements(data):
    lines = [_heading("achievements")]
    achievements = data.get("achievements") or []

    if not achievements:
        lines.append("(no achievements yet)")
        return "\n".join(lines)

    for item in achievements:
        title = _text(item.get("title")) or "(untitled)"
        date = _text(item.get("date"))

        head = "- " + title
        if date:
            head += "  (" + date + ")"
        lines.append(head)

        lines.extend(_wrap(item.get("note"), indent="  "))

    return "\n".join(lines)


# The order here is the order you see on screen.
SECTIONS = {
    "header": render_header,
    "about": render_about,
    "links": render_links,
    "skills": render_skills,
    "projects": render_projects,
    "achievements": render_achievements,
}


def render_all(data):
    """Render every section, top to bottom."""
    parts = [render(data) for render in SECTIONS.values()]
    return "\n".join(part for part in parts if part)


def render_section(data, name):
    """Render one section by name, e.g. 'projects'."""
    if name not in SECTIONS:
        raise KeyError(
            "Unknown section: " + name + ". Choose from: " + ", ".join(SECTIONS)
        )
    return SECTIONS[name](data)
