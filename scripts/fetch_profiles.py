#!/usr/bin/env python3
"""抓取每位主将的 EDHREC 档案：全时段套牌数/排名/咸度/Bracket 分布/玩法标签。"""
from __future__ import annotations

import json
import pathlib
import sys
import time
import urllib.error
import urllib.request



# --- 路径已改为相对本文件，便于他人 clone 后直接运行 ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
sys.stdout.reconfigure(encoding="utf-8")
DATA = pathlib.Path(ROOT / "data")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")


def fetch_json(url: str, tries: int = 3):
    for attempt in range(tries):
        request = urllib.request.Request(
            url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as error:
            if error.code in (403, 404):
                return None
            time.sleep(1.5 * (attempt + 1))
        except Exception:  # noqa: BLE001
            time.sleep(1.5 * (attempt + 1))
    return None


def extract(payload: dict) -> dict | None:
    card = (payload.get("container") or {}).get("json_dict", {}).get("card")
    if not card:
        return None
    return {
        "name": card.get("name"),
        "slug": card.get("slug"),
        "num_decks": card.get("num_decks"),
        "all_time_rank": card.get("rank"),
        "salt": card.get("salt"),
        "color_identity": card.get("color_identity"),
        "cmc": card.get("cmc"),
        "type_line": card.get("type_line"),
        "is_commander": card.get("is_commander"),
        "legal_commander": card.get("legal_commander"),
        "bracket_counts": payload.get("bracket_counts"),
        "tag_counts": payload.get("tag_counts"),
        "budget_counts": payload.get("budget_counts"),
    }


def main() -> int:
    candidates = json.loads((DATA / "edhrec_candidates.json").read_text(encoding="utf-8"))
    supplement = json.loads((DATA / "supplement_probe.json").read_text(encoding="utf-8"))

    targets: list[tuple[str, str]] = []
    for record in candidates:
        targets.append((record["name"], record["slug"]))
    for record in supplement:
        targets.append((record["name"], record["slug"]))

    seen: set[str] = set()
    profiles: dict[str, dict] = {}
    failed: list[str] = []

    for name, slug in targets:
        if slug in seen:
            continue
        seen.add(slug)
        payload = fetch_json(f"https://json.edhrec.com/pages/commanders/{slug}.json")
        if payload is None:
            failed.append(f"{name} ({slug})")
            continue
        data = extract(payload)
        if data is None:
            failed.append(f"{name} ({slug}) [无 card 字段]")
            continue
        data["edhrec_name"] = name
        profiles[name] = data
        time.sleep(0.25)

    (DATA / "commander_profiles.json").write_text(
        json.dumps(profiles, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ 成功 {len(profiles)} / 失败 {len(failed)}")
    for item in failed:
        print(f"  ✗ {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
