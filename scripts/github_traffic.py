"""Hämtar GitHubs trafikstatistik och lägger till den i CSV-filer.

GitHub sparar bara 14 dagar. Skriptet körs dagligen av
.github/workflows/traffic.yml och skriver till katalogen OUT_DIR (grenen
traffic-data). Kräver miljövariablerna GH_TOKEN, REPO och OUT_DIR.

Token: skapa en fine-grained personal access token på GitHub
(Settings > Developer settings > Fine-grained tokens) med åtkomst bara till
det här repot och behörigheten Administration: Read-only. Lägg den som
repository secret med namnet TRAFFIC_TOKEN
(repot > Settings > Secrets and variables > Actions).
"""
import csv
import datetime as dt
import json
import os
import urllib.request
from pathlib import Path

TOKEN = os.environ["GH_TOKEN"]
REPO = os.environ["REPO"]
OUT = Path(os.environ.get("OUT_DIR", "traffic"))
TODAY = dt.date.today().isoformat()


def get(endpoint):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/traffic/{endpoint}",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def merge_daily(name, items):
    """Views och clones: en rad per dag, nyare hämtning skriver över äldre."""
    path = OUT / f"{name}.csv"
    rows = {}
    if path.exists():
        with path.open(newline="") as f:
            rows = {r["date"]: r for r in csv.DictReader(f)}
    for it in items:
        day = it["timestamp"][:10]
        rows[day] = {"date": day, "count": it["count"], "uniques": it["uniques"]}
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "count", "uniques"])
        w.writeheader()
        w.writerows(rows[d] for d in sorted(rows))


def append_snapshot(name, items, fields):
    """Referrers och paths är 14-dagarssummor. Spara dagens ögonblicksbild."""
    path = OUT / f"{name}.csv"
    cols = ["fetched"] + fields
    old = []
    if path.exists():
        with path.open(newline="") as f:
            old = [r for r in csv.DictReader(f) if r["fetched"] != TODAY]
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(old)
        w.writerows({"fetched": TODAY, **{k: it.get(k, "") for k in fields}} for it in items)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    views = get("views")
    clones = get("clones")
    referrers = get("popular/referrers")
    paths = get("popular/paths")

    raw = OUT / "raw" / TODAY
    raw.mkdir(parents=True, exist_ok=True)
    for name, data in [("views", views), ("clones", clones),
                       ("referrers", referrers), ("paths", paths)]:
        (raw / f"{name}.json").write_text(json.dumps(data, indent=2) + "\n")

    merge_daily("views", views["views"])
    merge_daily("clones", clones["clones"])
    append_snapshot("referrers", referrers, ["referrer", "count", "uniques"])
    append_snapshot("paths", paths, ["path", "title", "count", "uniques"])


if __name__ == "__main__":
    main()
