#!/usr/bin/env python3
"""探测可用的「主将流行度」数据源。"""
from __future__ import annotations

import urllib.error
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

URLS = [
    "https://json.edhrec.com/pages/commanders.json",
    "https://json.edhrec.com/pages/top/commanders.json",
    "https://json.edhrec.com/pages/commanders/top.json",
    "https://json.edhrec.com/pages/commanders/year.json",
    "https://edhrec.com/top/commanders",
    "https://edhrec.com/top",
    "https://www.mtggoldfish.com/metagame/commander",
    "https://api.scryfall.com/cards/search?q=is%3Acommander&order=edhrec&dir=asc",
]


def probe(url: str) -> None:
    request = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "application/json,text/html,*/*"})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            body = response.read()
            text = body.decode("utf-8", "replace")
            head = " ".join(text[:180].split())
            print(f"[{response.status}] {len(body):>8}B  {url}\n      {head}\n")
    except urllib.error.HTTPError as error:
        print(f"[HTTP {error.code}]           {url}\n      {error.reason}\n")
    except Exception as error:  # noqa: BLE001
        print(f"[ERR {type(error).__name__}]      {url}\n      {error}\n")


if __name__ == "__main__":
    for target in URLS:
        probe(target)
