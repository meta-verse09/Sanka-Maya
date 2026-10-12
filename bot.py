
import sys, requests, pathlib, urllib.parse, os

judul = sys.argv[1] if len(sys.argv)>1 else "Arti Angka 11:11"
# Bikin prompt gambar yang nyambung sama judul
prompt_gambar = f"mystical numerology illustration of {judul}, glowing numbers, cosmic, spiritual, high detail, 4k, blog thumbnail"

# 1. BIKIN ARTIKEL (dari Pollinations Text)
prompt_artikel = f"Tulis artikel blog 700 kata bahasa Indonesia santai tentang {judul}, format HTML Blogger <h2><p><ul>. Hook pembuka 2 paragraf."
try:
  url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt_artikel)}?model=openai"
  artikel = requests.get(url, timeout=120).text
except:
  artikel = f"<h2>{judul}</h2><p>Artikel tentang {judul}</p>"

# 2. BIKIN GAMBAR (dari Pollinations Image)
try:
  # model flux paling bagus buat ilustrasi
  img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt_gambar)}?width=1280&height=720&model=flux&nologo=true"
  img_data = requests.get(img_url, timeout=120).content
  pathlib.Path("artikel").mkdir(exist_ok=True)
  safe = "".join(c if c.isalnum() else "-" for c in judul)[:30]
  img_path = f"artikel/{safe}.jpg"
  pathlib.Path(img_path).write_bytes(img_data)
  print(f"Gambar jadi: {img_path}")

  # 3. Sisipin gambar ke atas artikel biar langsung kepake di Blogger
  tag_gambar = f'<div style="text-align:center"><img src="{safe}.jpg" alt="{judul}" style="width:100%;border-radius:12px" /></div>\n'
  artikel_final = tag_gambar + artikel
except Exception as e:
  print(f"Gambar gagal: {e}")
  artikel_final = artikel
  safe = "".join(c if c.isalnum() else "-" for c in judul)[:30]

# 4. SIMPAN ARTIKEL
pathlib.Path(f"artikel/{safe}.html").write_text(artikel_final, encoding="utf-8")
print("DONE - artikel + gambar siap")
