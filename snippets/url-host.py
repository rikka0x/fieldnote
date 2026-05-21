#!/usr/bin/env python3
"""Tiny URL host checker. No network calls."""

from urllib.parse import urlparse
import sys

for raw in sys.argv[1:]:
    url = raw if "://" in raw else "https://" + raw
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    print(f"{raw} -> {host or 'no-host'}")
