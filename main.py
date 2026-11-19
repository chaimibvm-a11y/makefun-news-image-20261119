"""News-image entry (Python 3.13, stdlib only): copies the entry.png beside
this file to /output/entry.png. Run locally with:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

# The image sums up Thursday 19 November 2026: Trump-Xi-Putin in Shenzhen,
# Gaza ground operation, Anthropic's record IPO, Crimean Bridge, Voyager 1,
# and the GTA VI launch, under the masthead "WORLD NEWS".
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copyfile(src, dst)
