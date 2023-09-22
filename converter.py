import logging
from pdfminer.high_level import extract_text
from pathlib import Path

EXTENSAO_TXT = ".txt"

def configurar_logging():
    logging.basicConfig(
        filename="conversor.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8"
    )

def gerar_caminho_txt(caminho_pdf: Path, pasta_txt: Path) -> Path:
    nome_arquivo_txt = caminho_pdf.stem + EXTENSAO_TXT
    return pasta_txt / nome_arquivo_txt

def escrever_texto_em_arquivo(texto: str, caminho_txt: Path) -> None:
    with open(caminho_txt, "w", encoding="utf-8") as arquivo_txt:
        arquivo_txt.write(texto)

def converter_pdf_para_txt(caminho_pdf: Path, pasta_txt: Path) -> None:
    try:
        caminho_txt = gerar_caminho_txt(caminho_pdf, pasta_txt)
        texto = extract_text(caminho_pdf)
        escrever_texto_em_arquivo(texto, caminho_txt)
        logging.info(f"Conversão concluída: {caminho_pdf.name}")
    except Exception as e:
        logging.error(f"Erro ao converter o arquivo {caminho_pdf.name}: {str(e)}")

def converter_pdfs_na_pasta(caminho_pasta: Path, pasta_saida: Path) -> None:
    try:
        arquivos_pdf = [f for f in caminho_pasta.iterdir() if f.suffix == ".pdf"]

        if not arquivos_pdf:
            logging.warning("Nenhum arquivo PDF encontrado na pasta de entrada.")
            return

        for arquivo_pdf in arquivos_pdf:
            converter_pdf_para_txt(arquivo_pdf, pasta_saida)

        logging.info("Conversão de PDFs concluída.")
    except Exception as e:
        logging.error(f"Erro ao converter os PDFs: {str(e)}")

def criar_diretorio_saida(pasta_saida: Path) -> None:
    pasta_saida.mkdir(parents=True, exist_ok=True)
    logging.info(f"Diretório de saída criado: {pasta_saida}")

def verificar_arquivo_saida(caminho_arquivo: Path) -> Path:
    if caminho_arquivo.exists():
        nome_arquivo, extensao_arquivo = caminho_arquivo.stem, caminho_arquivo.suffix
        contador = 1
        novo_nome_arquivo = caminho_arquivo.parent / f"{nome_arquivo}_{contador}{extensao_arquivo}"
        while novo_nome_arquivo.exists():
            contador += 1
            novo_nome_arquivo = caminho_arquivo.parent / f"{nome_arquivo}_{contador}{extensao_arquivo}"
        return novo_nome_arquivo
    return caminho_arquivo

def main():
    pasta_entrada = Path("C:\\conversor_extrator\\guias")
    pasta_saida = pasta_entrada / "guias_txt"

    configurar_logging()

    try:
        criar_diretorio_saida(pasta_saida)
        converter_pdfs_na_pasta(pasta_entrada, pasta_saida)
    except Exception as e:
        logging.error(f"Erro ao processar os arquivos: {str(e)}")

if __name__ == "__main__":
    main()
