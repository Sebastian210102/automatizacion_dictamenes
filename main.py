import pdfplumber
from pathlib import Path

INPUT_FOLDER = Path("input")

def leer_pdf(ruta_pdf):
    texto_completo = ""

    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                texto_completo += texto + "\n"

    return texto_completo


def main():
    for archivo in INPUT_FOLDER.iterdir():
        if archivo.suffix.lower() == ".pdf":
            texto = leer_pdf(archivo)
            print("=== TEXTO EXTRAÍDO ===")
            print(texto)


if __name__ == "__main__":
    main()
