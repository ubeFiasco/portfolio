# Builds a single self-contained page (fonts inlined) for Artifact publishing.
import base64, re, pathlib, sys
root = pathlib.Path(__file__).parent
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / "dist" / "geoff-olegario.html"
s = (root / "index.html").read_text()
def inline(m):
    data = base64.b64encode((root / m.group(1)).read_bytes()).decode()
    return f'url("data:font/woff2;base64,{data}") format("woff2")'
s = re.sub(r'url\("(fonts/[^"]+\.woff2)"\) format\("woff2"\), url\("fonts/[^"]+\.woff"\) format\("woff"\)', inline, s)
s = re.sub(r'<!doctype html>\s*<html[^>]*>\s*<head>\s*', '', s, flags=re.I)
s = re.sub(r'<meta charset[^>]*>\s*<meta name="viewport"[^>]*>\s*', '', s)
s = s.replace('</head>\n<body data-lens="design">', '').replace('</body>\n</html>', '')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(s)
print(out, len(s))
