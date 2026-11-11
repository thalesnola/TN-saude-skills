"""Extrai texto de laudos PDF para <pasta>/_texto/<nome>.txt (pdftotext; OCR só nas páginas sem texto).
Uso: python extrai_exame.py <pdf ou pasta> [...]   Idempotente: pula PDF cujo .txt é mais novo."""
import subprocess, sys, tempfile, pathlib

MIN_CHARS = 80  # página com menos que isso é tratada como imagem
# OCR calibrado (CLAUDE.md global): 300 dpi, cinza, psm 4, por. Texto cinza-claro de formulário não é lido.

def run(*a):
    return subprocess.run(a, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout

def paginas(pdf):
    n = int(next(l.split()[1] for l in run("pdfinfo", str(pdf)).splitlines() if l.startswith("Pages:")))
    for p in range(1, n + 1):
        t = run("pdftotext", "-enc", "UTF-8", "-layout", "-f", str(p), "-l", str(p), str(pdf), "-")
        if len(t.strip()) < MIN_CHARS:
            with tempfile.TemporaryDirectory() as d:
                run("pdftoppm", "-r", "300", "-gray", "-f", str(p), "-l", str(p), "-png", str(pdf), f"{d}/p")
                img = next(pathlib.Path(d).glob("p*.png"))
                t = run("tesseract", str(img), "-", "--psm", "4", "-l", "por")
            t = "[OCR — conferir contra o original]\n" + t
        yield p, t

def main(alvos):
    pdfs = [f for a in alvos for f in ([pathlib.Path(a)] if pathlib.Path(a).is_file() else pathlib.Path(a).rglob("*.pdf")) if "_texto" not in f.parts]
    for pdf in pdfs:
        out = pdf.parent / "_texto" / (pdf.stem + ".txt")
        if out.exists() and out.stat().st_mtime > pdf.stat().st_mtime:
            print("pula", pdf.name); continue
        out.parent.mkdir(exist_ok=True)
        ocr = 0
        with open(out, "w", encoding="utf-8") as f:
            for p, t in paginas(pdf):
                ocr += t.startswith("[OCR")
                f.write(f"\n===== PÁGINA {p} =====\n{t}")
        print(f"{pdf.name}: ok, {ocr} página(s) por OCR -> {out}")

if __name__ == "__main__":
    main(sys.argv[1:] or ["."])
