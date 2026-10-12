import sys, requests, pathlib, datetime, urllib.parse

judul = sys.argv[1] if len(sys.argv)>1 else "Arti Angka 11:11"
kategori = sys.argv[2] if len(sys.argv)>2 else "numerologi"

prompt = f"""Kamu penulis blog Sanka-Maya (sanka-maya.blogspot.com), niche numerologi.
Tulis artikel 800 kata bahasa Indonesia santai.
Judul: {judul}
Kategori: {kategori}
Format: HTML Blogger (<h2>, <h3>, <p>, <ul><li>). Jangan pakai <html><head>.
Struktur: hook 2 paragraf, 3-4 H2, penutup + disclaimer hiburan.
Akhir: 3 keyword SEO."""

# API GRATIS TANPA KEY - Pollinations AI
try:
    # Pollinations itu ChatGPT gratis tanpa daftar
    encoded = urllib.parse.quote(prompt)
    url = f"https://text.pollinations.ai/{encoded}?model=openai"
    r = requests.get(url, timeout=90)
    artikel = r.text
    print("Pollinations OK")
except Exception as e:
    print("Error:", e)
    artikel = f"<h2>{judul}</h2><p>Gagal generate, coba lagi. Kategori {kategori}</p>"

# Simpan
pathlib.Path("artikel").mkdir(exist_ok=True)
safe = "".join(c if c.isalnum() else "-" for c in judul)[:40]
path = f"artikel/{safe}.html"
pathlib.Path(path).write_text(artikel, encoding="utf-8")
print(f"Saved {path}")
