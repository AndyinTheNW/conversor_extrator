import os
from pdfminer.high_level import extract_text

def convert_pdf_to_txt(pdf_path, txt_dir):
    filename = os.path.basename(pdf_path)
    txt_filename = os.path.splitext(filename)[0] + ".txt"
    txt_path = os.path.join(txt_dir, txt_filename)
    text = extract_text(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

def convert_pdfs_in_folder(folder_path, output_folder):
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        convert_pdf_to_txt(pdf_path, output_folder)

# Diretório contendo os arquivos PDF
input_folder = "C:/epson_py/guias"

# Diretório de saída para os arquivos TXT
output_folder = os.path.join(input_folder, "guias_txt")
os.makedirs(output_folder, exist_ok=True)

convert_pdfs_in_folder(input_folder, output_folder)
