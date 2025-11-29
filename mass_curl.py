#!/usr/bin/env python3
import argparse
import subprocess
from pathlib import Path

def load_urls(path: Path):
    urls = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            urls.append(line)
    return urls

def main():
    parser = argparse.ArgumentParser(
        description="Run curl against many URLs from a file."
    )

    # URL file (required)
    parser.add_argument(
        "url_file",
        help="File containing one URL per line",
    )

    # Everything after the URL file is passed to curl
    parser.add_argument(
        "curl_args",
        nargs=argparse.REMAINDER,
        help="Extra args passed directly to curl (e.g. -k -b 'cookie=1')",
    )

    args = parser.parse_args()

    url_path = Path(args.url_file)
    if not url_path.is_file():
        print(f"[-] URL file '{url_path}' not found")
        raise SystemExit(1)

    urls = load_urls(url_path)
    print(f"[*] Loaded {len(urls)} URLs")

    for url in urls:
        print(f"\n[*] Requesting: {url}")

        # Show headers + status + time, hide body
        cmd = [
            "curl",
            "-s",              # silent (no progress bar)
            "-D", "-",         # print response headers to stdout
            "-o", "/dev/null", # discard body
            "-w", "\nHTTP %{http_code} | time %{time_total}s\n",
        ] + args.curl_args + [url]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
        )

        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            # Uncomment if you want to see curl errors/warnings
            # print(result.stderr.strip())
            pass

if __name__ == "__main__":
    main()


