#!/usr/bin/env python3
"""Export the course markdown to HTML fragments for ProductDyno Pro lessons.

ProductDyno's lesson editor accepts pasted HTML (use the editor's source/HTML
view). Page-level <style> blocks are often stripped by rich-text editors, so
every style is written inline on the element it applies to.

Usage:
    pip install markdown
    python3 tools/build_productdyno.py

Output: productdyno/<lesson-file>.html (one fragment per lesson) and
productdyno/index.html (a local preview of all lessons in course order).
"""
import html
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "productdyno"

# Course order as it should appear in ProductDyno: (section, markdown path)
LESSONS = [
    ("Start Here", "assets/reference/KE-00-kenya-regional-reference.md"),
    ("Module 1", "modules/module-1/01-infrastructure-climate.md"),
    ("Module 1", "assets/sops/SOP-101-low-cost-passive-climate.md"),
    ("Module 1", "assets/deliverables/Deliverable-101-hvac-parameter-matrix.md"),
    ("Module 2", "modules/module-2/02-substrate-composting.md"),
    ("Module 2", "assets/sops/SOP-201-phase-1-composting.md"),
    ("Module 2", "assets/sops/SOP-202-phase-2-pasteurization.md"),
    ("Module 2", "assets/deliverables/Deliverable-202-cn-ratio-calculator.md"),
    ("Module 3", "modules/module-3/03-spawning-casing.md"),
    ("Module 3", "assets/sops/SOP-301-aseptic-spawning.md"),
    ("Module 3", "assets/sops/SOP-302-casing-preparation.md"),
    ("Module 3", "assets/deliverables/Deliverable-303-spawn-run-audit.md"),
    ("Module 4", "modules/module-4/04-fruiting-harvest.md"),
    ("Module 4", "assets/sops/SOP-401-pinning-induction.md"),
    ("Module 4", "assets/sops/SOP-402-ipm-sanitization.md"),
    ("Module 4", "assets/sops/SOP-403-harvesting-grading.md"),
    ("Module 4", "assets/deliverables/Deliverable-404-flush-yield-tracking.md"),
    ("Module 5", "modules/module-5/05-economics-marketing.md"),
    ("Module 5", "assets/deliverables/Deliverable-505-business-plan-model.md"),
]

FONT = "font-family:Arial,Helvetica,sans-serif;line-height:1.6;color:#1f2933;"
STYLES = {
    "h1": "font-size:28px;margin:0 0 16px;color:#14532d;",
    "h2": "font-size:22px;margin:32px 0 12px;padding-bottom:6px;border-bottom:2px solid #16a34a;color:#14532d;",
    "h3": "font-size:18px;margin:24px 0 8px;color:#166534;",
    "h4": "font-size:16px;margin:20px 0 8px;color:#166534;",
    "table": "border-collapse:collapse;width:100%;margin:12px 0 20px;font-size:14px;",
    "th": "border:1px solid #cbd5e1;background:#ecfdf5;padding:8px;text-align:left;vertical-align:top;",
    "td": "border:1px solid #cbd5e1;padding:8px;vertical-align:top;",
    "blockquote": "margin:16px 0;padding:12px 16px;background:#f0fdf4;border-left:4px solid #16a34a;",
    "pre": "background:#f8fafc;border:1px solid #e2e8f0;padding:12px;overflow-x:auto;font-size:13px;line-height:1.4;",
    "code": "font-family:Consolas,Menlo,monospace;",
    "hr": "border:0;border-top:1px solid #e2e8f0;margin:28px 0;",
}


def inline_styles(fragment: str) -> str:
    """Add a style attribute to every bare tag listed in STYLES."""
    for tag, style in STYLES.items():
        fragment = re.sub(rf"<{tag}(?=[\s>])", f'<{tag} style="{style}"', fragment)
    # python-markdown writes table alignment as style="text-align: ..." on th/td;
    # merge it with the inline style we just added instead of emitting two attributes.
    fragment = re.sub(
        r'(<t[hd]) style="([^"]*)" style="([^"]*)"', r'\1 style="\2\3"', fragment
    )
    # Markdown task-list boxes ("[ ]") read better as a printable ballot box.
    return fragment.replace("[ ]", "☐").replace("[x]", "☑")


def convert(md_text: str) -> str:
    body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])
    return f'<div style="{FONT}">\n{inline_styles(body)}\n</div>\n'


def main() -> None:
    OUT.mkdir(exist_ok=True)
    preview = []
    for section, rel in LESSONS:
        src = ROOT / rel
        fragment = convert(src.read_text(encoding="utf-8"))
        name = src.stem + ".html"
        (OUT / name).write_text(fragment, encoding="utf-8")
        preview.append(f"<h6>{html.escape(section)} · {html.escape(name)}</h6>\n{fragment}<hr>")
        print(f"wrote productdyno/{name}")
    (OUT / "index.html").write_text(
        "<!doctype html><meta charset='utf-8'><title>Course preview</title>"
        "<body style='max-width:960px;margin:auto;padding:16px'>\n" + "\n".join(preview),
        encoding="utf-8",
    )
    print("wrote productdyno/index.html")


if __name__ == "__main__":
    main()
