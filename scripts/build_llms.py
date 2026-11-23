"""Bygger llms.txt och llms-full.txt i repots rot ur mkdocs.yml.

llms-full.txt innehåller hela guiden i nav-ordning med begreppstexterna
inlagda, så att en AI kan läsa allt via en enda länk. Kör skriptet och
commita resultatet efter varje ändring i docs/ eller begrepp/.
"""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://solsidan21.github.io/AI_workflow_guide_svenska/"
RAW = "https://raw.githubusercontent.com/Solsidan21/AI_workflow_guide_svenska/main/"


class Loader(yaml.SafeLoader):
    pass


Loader.add_multi_constructor("", lambda loader, suffix, node: None)


def pages(nav):
    for item in nav:
        for title, value in item.items():
            if isinstance(value, list):
                yield from pages(value)
            else:
                yield title, value


def expand(text):
    def repl(m):
        indent, name = m.group(1), m.group(2)
        body = (ROOT / "begrepp" / name).read_text(encoding="utf-8").strip()
        return "\n".join(indent + line if line else line for line in body.splitlines())

    return re.sub(r'^([ \t]*)--8<-- "([^"]+)"', repl, text, flags=re.M)


def main():
    cfg = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=Loader)
    index_lines = [
        "# AI-workflowguiden",
        "",
        "> En persons upplägg för att arbeta med Claude (och ChatGPT) med en vanlig prenumeration. Inget facit.",
        "",
        f"Hela guiden i en fil: {RAW}llms-full.txt",
        "",
    ]
    full = [
        "# AI-workflowguiden (hela texten)",
        "",
        "Guiden beskriver en persons upplägg och är inget facit. Använd det som passar läsaren och ställ frågor om resten.",
        "",
    ]
    for title, path in pages(cfg["nav"]):
        url = RAW + "docs/" + path
        index_lines.append(f"- [{title}]({url})")
        text = expand((ROOT / "docs" / path).read_text(encoding="utf-8"))
        full += ["", "---", f"Källa: {url}", "", text.strip(), ""]
    (ROOT / "llms.txt").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    (ROOT / "llms-full.txt").write_text("\n".join(full) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
