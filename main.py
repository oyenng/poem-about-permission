import sys
from pathlib import Path

POEM = """Permission Slip

Third grade, I forged Mom's signature,
perfect loops, went to the zoo.
She found out.

After, she signed slower,
where I could watch it land,
and made me ask out loud.

Forty now. Before I sign anything,
my hand stops, pen up,
and asks her first."""


def main() -> int:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")

    assert target.exists(), "entry.txt was not written"
    raw = target.read_bytes()
    text = raw.decode("utf-8")
    assert text == POEM
    assert 1 <= len(text) <= 280, f"length out of range: {len(text)}"
    assert len(text.strip()) > 0, "entry is whitespace only"

    print(f"chars: {len(text)}")
    print(f"bytes: {len(raw)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
