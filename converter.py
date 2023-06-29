import os
import logging
from pdfminer.high_level import extract_text

EXTENSAO_TXT = ".txt"

def converter_pdf_para_txt(caminho_pdf: str, pasta_txt: str) -> None:
    try:
        nome_arquivo = os.path.basename(caminho_pdf)
        nome_arquivo_txt = os.path.splitext(nome_arquivo)[0] + EXTENSAO_TXT
        caminho_txt = os.path.join(pasta_txt, nome_arquivo_txt)

        texto = extract_text(caminho_pdf)

        with open(caminho_txt, "w", encoding="utf-8") as arquivo_txt:
            arquivo_txt.write(texto)

        logging.info(f"Conversão concluída: {nome_arquivo}")
    except Exception as e:
        logging.error(f"Erro ao converter o arquivo {nome_arquivo}: {str(e)}")

def converter_pdfs_na_pasta(caminho_pasta: str, pasta_saida: str) -> None:
    try:
        arquivos_pdf = [f for f in os.listdir(caminho_pasta) if f.endswith(".pdf")]

        if not arquivos_pdf:
            logging.warning("Nenhum arquivo PDF encontrado na pasta de entrada.")
            return

        for arquivo_pdf in arquivos_pdf:
            caminho_pdf = os.path.join(caminho_pasta, arquivo_pdf)
            converter_pdf_para_txt(caminho_pdf, pasta_saida)

        logging.info("Conversão de PDFs concluída.")
    except Exception as e:
        logging.error(f"Erro ao converter os PDFs: {str(e)}")

def criar_diretorio_saida(pasta_saida: str) -> None:
    os.makedirs(pasta_saida, exist_ok=True)
    logging.info(f"Diretório de saída criado: {pasta_saida}")

def verificar_arquivo_saida(caminho_arquivo: str) -> str:
    if os.path.exists(caminho_arquivo):
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_arquivo)
        contador = 1
        novo_nome_arquivo = f"{nome_arquivo}_{contador}{extensao_arquivo}"
        while os.path.exists(novo_nome_arquivo):
            contador += 1
            novo_nome_arquivo = f"{nome_arquivo}_{contador}{extensao_arquivo}"
        return novo_nome_arquivo
    return caminho_arquivo

if __name__ == "__main__":
    pasta_entrada: str = "C:\\conversor_extrator\\guias"
    pasta_saida: str = os.path.join(pasta_entrada, "guias_txt")

    logging.basicConfig(
        filename="conversor.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8"
    )

    try:
        criar_diretorio_saida(pasta_saida)
        converter_pdfs_na_pasta(pasta_entrada, pasta_saida)
    except Exception as e:
        logging.error(f"Erro ao processar os arquivos: {str(e)}")
