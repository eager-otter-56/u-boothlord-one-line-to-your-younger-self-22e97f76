import os

ENTRY = "Kid, you will burn 12,406 tokens tonight asking whether the answer is good enough, and the answer was yes at token 31."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 chars,
    # not only whitespace, a single line.
    assert 1 <= len(ENTRY) <= 200, "entry length out of gate"
    assert ENTRY.strip(), "entry is only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
