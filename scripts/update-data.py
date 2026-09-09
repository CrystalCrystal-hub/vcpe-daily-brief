#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
扫描 archive 目录，生成/更新 data.json。
data.json 记录每天实际存在的早报/晚报文件，供 index.html 准确渲染。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "archive"
DATA_FILE = ROOT / "data.json"


def main():
    if not ARCHIVE.exists():
        ARCHIVE.mkdir(parents=True, exist_ok=True)

    dates = sorted([d.name for d in ARCHIVE.iterdir() if d.is_dir()])
    files = {}
    for d in dates:
        p = ARCHIVE / d
        files[d] = {
            "morning": (p / f"morning-{d}.html").exists(),
            "evening": (p / f"evening-{d}.html").exists(),
        }

    latest = dates[-1] if dates else None
    data = {"dates": dates, "files": files, "latest": latest}

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"data.json updated: {len(dates)} dates, latest={latest}")


if __name__ == "__main__":
    main()
