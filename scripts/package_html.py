"""Package an existing Vite build as a GameGen HTML ZIP (Python 3)."""
from pathlib import Path
import argparse
import re
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Destination mahjong-sixteen.zip")
    args = parser.parse_args()
    project = Path(__file__).resolve().parents[1]
    build = project / "dist"
    html = (build / "index.html").read_text(encoding="utf-8")
    if "/src/" in html or "%BASE_URL%" in html:
        raise SystemExit("index.html is a development entry; run npm run build first")
    poster = build / "poster.webp"
    if not poster.is_file() or poster.read_bytes() != (project / "public/poster.webp").read_bytes():
        raise SystemExit("Missing or outdated built poster; run npm run build first")
    for url in re.findall(r'(?:src|href)="([^"]+)"', html):
        if url.startswith(("https:", "http:", "data:")):
            continue
        if url.startswith("/") or not (build / url).is_file():
            raise SystemExit(f"Missing or non-relative entry asset: {url}")
    files = sorted(p for p in build.rglob("*") if p.is_file())
    output = args.output.resolve()
    if output.name != "mahjong-sixteen.zip":
        raise SystemExit("Use the game name: mahjong-sixteen.zip")
    if build == output.parent or build in output.parents:
        raise SystemExit("Output ZIP must be outside dist")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for file in files:
            archive.write(file, file.relative_to(build).as_posix())
    with zipfile.ZipFile(output) as archive:
        names = archive.namelist()
        assert "index.html" in names and "poster.webp" in names
        assert len(names) == len(set(names))
        assert not any(n.startswith(("dist/", "src/", "node_modules/", ".git/")) for n in names)
        assert archive.testzip() is None
        for file in files:
            assert archive.read(file.relative_to(build).as_posix()) == file.read_bytes()
    print(f"Verified {len(files)} runtime files: {output}")


if __name__ == "__main__":
    main()
