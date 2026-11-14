#!/usr/bin/env python3
"""Generates assets/stats.svg and assets/langs.svg for the profile README.

Uses only the standard library. Reads public data through the GitHub API
(GITHUB_TOKEN is optional, it just raises the rate limit).
Run with --seed to draw the cards from built-in numbers without network access.
"""
import json
import os
import sys
import urllib.request
from html import escape

USER = os.environ.get("GH_USER", "ANICKONS")
TOKEN = os.environ.get("GITHUB_TOKEN")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")

BG, BORDER, TITLE, TEXT, MUTED, ACCENT = "#1a1b27", "#2f334d", "#7aa2f7", "#c0caf5", "#787c99", "#7dcfff"
FONT = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
COLORS = {
    "C#": "#178600", "JavaScript": "#f1e05a", "TypeScript": "#3178c6", "CSS": "#563d7c",
    "C++": "#f34b7d", "C": "#555555", "HTML": "#e34c26", "PowerShell": "#5391fe",
    "Python": "#3572A5", "ShaderLab": "#5c6bc0", "HLSL": "#aace60", "Batchfile": "#C1F12E",
}


def api(path):
    req = urllib.request.Request("https://api.github.com" + path)
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch():
    user = api(f"/users/{USER}")
    repos, page = [], 1
    while True:
        chunk = api(f"/users/{USER}/repos?per_page=100&type=owner&page={page}")
        repos += chunk
        if len(chunk) < 100:
            break
        page += 1
    own = [r for r in repos if not r["fork"]]
    langs = {}
    for r in own:
        for name, size in api(f"/repos/{r['full_name']}/languages").items():
            langs[name] = langs.get(name, 0) + size
    try:
        commits = api(f"/search/commits?q=author:{USER}&per_page=1")["total_count"]
    except Exception:
        commits = None
    return {
        "repos": user["public_repos"],
        "followers": user["followers"],
        "stars": sum(r["stargazers_count"] for r in own),
        "commits": commits,
        "langs": langs,
    }


def seed():
    # counted by the main language of each public repository
    return {"repos": 6, "followers": 1, "stars": 0, "commits": 109,
            "langs": {"C#": 3, "JavaScript": 1, "TypeScript": 1, "CSS": 1}}


def card(width, height, title, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        f'role="img" aria-label="{escape(title)}">'
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="6" fill="{BG}" stroke="{BORDER}"/>'
        f'<text x="25" y="35" font-family="{FONT}" font-size="18" font-weight="600" fill="{TITLE}">{escape(title)}</text>'
        f"{body}</svg>"
    )


def stats_svg(d):
    commits = "—" if d["commits"] is None else str(d["commits"])
    rows = [("Репозитории", d["repos"]), ("Коммиты", commits), ("Звёзды", d["stars"]), ("Подписчики", d["followers"])]
    body = ""
    for i, (label, value) in enumerate(rows):
        y = 70 + i * 28
        body += (
            f'<circle cx="32" cy="{y - 5}" r="4" fill="{ACCENT}"/>'
            f'<text x="46" y="{y}" font-family="{FONT}" font-size="14" fill="{MUTED}">{escape(label)}</text>'
            f'<text x="440" y="{y}" font-family="{FONT}" font-size="14" font-weight="600" fill="{TEXT}" text-anchor="end">{value}</text>'
        )
    return card(495, 190, f"Статистика {USER}", body)


def langs_svg(d):
    items = sorted(d["langs"].items(), key=lambda kv: -kv[1])[:6]
    total = sum(v for _, v in items) or 1
    body, x, bar_w = "", 25, 445
    for name, v in items:
        w = bar_w * v / total
        body += f'<rect x="{x:.1f}" y="52" width="{max(w, 1):.1f}" height="10" fill="{COLORS.get(name, "#8b949e")}"/>'
        x += w
    body = f'<clipPath id="c"><rect x="25" y="52" width="{bar_w}" height="10" rx="5"/></clipPath><g clip-path="url(#c)">{body}</g>'
    for i, (name, v) in enumerate(items):
        col, row = i % 2, i // 2
        cx, cy = 25 + col * 225, 90 + row * 28
        body += (
            f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{COLORS.get(name, "#8b949e")}"/>'
            f'<text x="{cx + 18}" y="{cy}" font-family="{FONT}" font-size="13" fill="{TEXT}">{escape(name)}</text>'
            f'<text x="{cx + 200}" y="{cy}" font-family="{FONT}" font-size="13" fill="{MUTED}" text-anchor="end">{v / total * 100:.1f}%</text>'
        )
    return card(495, 190, "Языки", body)


def main():
    data = seed() if "--seed" in sys.argv else fetch()
    os.makedirs(OUT, exist_ok=True)
    for name, svg in (("stats.svg", stats_svg(data)), ("langs.svg", langs_svg(data))):
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(svg)
    print("ok:", {k: v for k, v in data.items() if k != "langs"}, "langs:", len(data["langs"]))


if __name__ == "__main__":
    main()
