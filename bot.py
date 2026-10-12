
import sys, requests, pathlib, urllib.parse
judul = sys.argv[1] if len(sys.argv)>1 else "Arti Angka 11:11"
prompt = f"Tulis artikel blog 700 kata bahasa Indonesia santai tentang {judul}, format HTML Blogger dengan H2 dan P"
try:
  url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt)}"
  r = requests.get(url, timeout=120)
  artikel = r.text
except:
  artikel = f"<h2>{judul}</h2><p>Artikel tentang {judul} dalam numerologi.</p>"

pathlib.Path("artikel").mkdir(exist_ok=True)
safe = "".join(c if c.isalnum() else "-" for c in judul)[:30]
pathlib.Path(f"artikel/{safe}.html").write_text(artikel, encoding="utf-8")
print("DONE")
