
import sys, requests, os, pathlib, urllib.parse

judul = sys.argv[1] if len(sys.argv)>1 else "Arti Angka 11:11"
kategori = sys.argv[2] if len(sys.argv)>2 else "numerologi"
HF_TOKEN = os.getenv("HF_TOKEN")

prompt = f"""Tulis artikel blog 800 kata, bahasa Indonesia santai ala Sanka-Maya.
Judul: {judul}
Kategori: {kategori}
Format HTML Blogger: <h2>, <h3>, <p>, <ul>. Jangan pakai <html><body>.
Hook pembuka 2 paragraf, isi 3-4 H2, penutup + disclaimer hiburan.
Akhiri dengan 3 keyword SEO."""

artikel = ""

# 1. COBA HUGGINGFACE DULU (Lebih stabil buat Indonesia)
if HF_TOKEN:
    try:
        print("Coba HuggingFace...")
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        payload = {"inputs": prompt, "parameters": {"max_new_tokens": 1500}}
        # Model gratis terbaik buat nulis Indo
        r = requests.post("https://api-inference.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct", headers=headers, json=payload, timeout=90)
        if r.status_code == 200:
            artikel = r.json()[0]['generated_text'][len(prompt):]
            print("HuggingFace SUKSES")
    except Exception as e:
        print(f"HF gagal: {e}")

# 2. FALLBACK KE POLLINATIONS (Gratis tanpa token)
if not artikel:
    try:
        print("Fallback ke Pollinations...")
        encoded = urllib.parse.quote(prompt)
        url = f"https://text.pollinations.ai/{encoded}?model=openai"
        r = requests.get(url, timeout=90)
        if r.status_code == 200 and len(r.text) > 100:
            artikel = r.text
            print("Pollinations SUKSES")
    except Exception as e:
        print(f"Pollinations gagal: {e}")

# 3. SIMPAN
if not artikel:
    artikel = f"<h2>{judul}</h2><p>AI lagi sibuk Bray, coba run lagi 1 menit lagi.</p>"

pathlib.Path("artikel").mkdir(exist_ok=True)
safe = "".join(c if c.isalnum() else "-" for c in judul)[:40]
pathlib.Path(f"artikel/{safe}.html").write_text(artikel, encoding="utf-8")
print("SELESAI - Artikel siap di folder artikel/")
