"""Prepara a pasta de fotos corporais para leitura: HEIC->JPG, quadros de vídeo, pranchas comparativas e tabela EXIF+SHA256.

Uso: python prepara_fotos.py <PASTA_SAUDE>/FOTOS/MES_EXEMPLO [pasta_saida]
Saída (padrão: pasta temporária) = DADO DE SAÚDE: apagar ao terminar. Nunca grava na pasta de origem.
"""
import hashlib, subprocess, sys, tempfile
from pathlib import Path
import pillow_heif
from PIL import Image, ImageOps

pillow_heif.register_heif_opener()
src = Path(sys.argv[1])
out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(tempfile.mkdtemp(prefix="fotos_"))
out.mkdir(parents=True, exist_ok=True)
H = 900  # altura de cada foto na prancha


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def sheet(paths, name):
    ims = [Image.open(p) for p in paths]
    ims = [i.resize((int(i.width * H / i.height), H)) for i in ims]
    s = Image.new("RGB", (sum(i.width for i in ims), H))
    x = 0
    for i in ims:
        s.paste(i, (x, 0))
        x += i.width
    s.save(out / name, quality=85)


jpgs = []
print("arquivo | dimensões | data/hora EXIF | sha256[:16]")
for f in sorted(src.iterdir()):
    ext = f.suffix.lower()
    if ext in (".heic", ".jpg", ".jpeg", ".png"):
        im = Image.open(f)
        when = im.getexif().get_ifd(0x8769).get(36867, "?")  # DateTimeOriginal
        print(f"{f.name} | {im.size} | {when} | {sha(f)}")
        im = ImageOps.exif_transpose(im).convert("RGB")
        im.thumbnail((1000, 1400))
        j = out / (f.stem + ".jpg")
        im.save(j, quality=88)
        jpgs.append(j)
    elif ext in (".mov", ".mp4"):
        print(f"{f.name} | vídeo | {f.stat().st_mtime:.0f} (mtime) | {sha(f)}")
        # ffmpeg corrige a rotação sozinho; 1 quadro/s basta para postura
        subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-vf", "fps=1,scale=-2:700",
                        "-y", str(out / f"{f.stem}_q%d.jpg")], check=True)

for n in range(0, len(jpgs), 5):
    sheet(jpgs[n:n + 5], f"prancha_{n // 5 + 1}.jpg")
print("saída:", out)
