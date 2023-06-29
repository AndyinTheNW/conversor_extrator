import re


# Endereço atual do arquivo txt: C:\conversor_extrator\guias\guias_txt\13 - GNRE - DIÁRIA - MT.txt

txt_path = r"C:\conversor_extrator\guias\guias_txt\13 - GNRE - DIÁRIA - MT.txt"

def extract_information_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as txt_file:
        content = txt_file.read()
    
    information = {}
    
    # Extração da Razão Social
    razao_social_match = re.search(r"Razão Social:\s+(.*)", content)
    if razao_social_match:
        information["Razão Social"] = razao_social_match.group(1)
    
    # Extração do Endereço
    endereco_match = re.search(r"Endereço:\s+(.*)", content)
    if endereco_match:
        information["Endereço"] = endereco_match.group(1)
    
    # Extração do CNPJ/CPF/Insc. Est.
    cnpj_match = re.search(r"CNPJ/CPF/Insc. Est.:\s+([\d.-]+)", content)
    if cnpj_match:
        information["CNPJ/CPF/Insc. Est."] = cnpj_match.group(1)
    
    # Extração do UF
    uf_match = re.search(r"UF:\s+([A-Z]{2})", content)
    if uf_match:
        information["UF"] = uf_match.group(1)
    
    # Extração do Telefone
    telefone_match = re.search(r"Telefone:\s+(\d+)", content)
    if telefone_match:
        information["Telefone"] = telefone_match.group(1)
    
    # Extração do Município
    municipio_match = re.search(r"Município:\s+(\d+)", content)
    if municipio_match:
        information["Município"] = municipio_match.group(1)
    
    # Extração do Tributo
    tributo_match = re.search(r"Tributo:\s+(\d+)\s+-\s+(.*)", content)
    if tributo_match:
        information["Tributo"] = tributo_match.group(1)
        information["Descrição do Tributo"] = tributo_match.group(2)
    
    # Extração da Chave
    chave_match = re.search(r"Chave:\s+(\d+)", content)
    if chave_match:
        information["Chave"] = chave_match.group(1)
    
    # Extração da Data de Vencimento
    vencimento_match = re.search(r"Documento Válido para pagamento até\s+([\d/]+)", content)
    if vencimento_match:
        information["Data de Vencimento"] = vencimento_match.group(1)
    
    # Extração do UF Favorecida
    uf_favorecida_match = re.search(r"UF Favorecida\s+([A-Z]{2})", content)
    if uf_favorecida_match:
        information["UF Favorecida"] = uf_favorecida_match.group(1)
    
    # Extração do Número de Controle
    num_controle_match = re.search(r"Nº de Controle\s+(\d+)", content)
    if num_controle_match:
        information["Nº de Controle"] = num_controle_match.group(1)
    
    # Extração do Código da Receita
    cod_receita_match = re.search(r"Código da Receita\s+(\d+)", content)
    if cod_receita_match:
        information["Código da Receita"] = cod_receita_match.group(1)
    
    # Extração do Número do Documento de Origem
    doc_origem_match = re.search(r"Nº Documento de Origem\s+(\d+)", content)
    if doc_origem_match:
        information["Nº Documento de Origem"] = doc_origem_match.group(1)
    
    # Extração do Período de Referência
    periodo_referencia_match = re.search(r"Período de Referência\s+([\d/]+)", content)
    if periodo_referencia_match:
        information["Período de Referência"] = periodo_referencia_match.group(1)
    
    # Extração do Valor Principal
    valor_principal_match = re.search(r"Valor Principal\s+R\$\s+([\d.,]+)", content)
    if valor_principal_match:
        information["Valor Principal"] = valor_principal_match.group(1)
    
    # Extração da Atualização Monetária
    atualizacao_monetaria_match = re.search(r"Atualização Monetária\s+R\$\s+([\d.,]+)", content)
    if atualizacao_monetaria_match:
        information["Atualização Monetária"] = atualizacao_monetaria_match.group(1)
    
    # Extração dos Juros
    juros_match = re.search(r"Juros\s+R\$\s+([\d.,]+)", content)
    if juros_match:
        information["Juros"] = juros_match.group(1)
    
    # Extração da Multa
    multa_match = re.search(r"Multa\s+R\$\s+([\d.,]+)", content)
    if multa_match:
        information["Multa"] = multa_match.group(1)
    
    # Extração do Total a Recolher
    total_recolher_match = re.search(r"Total a Recolher\s+R\$\s+([\d.,]+)", content)
    if total_recolher_match:
        information["Total a Recolher"] = total_recolher_match.group(1)
        
    # Extração do código de barras
    codigo_de_barras_match = re.search(r"Documento Válido para pagamento até\s+[\d/]+\s+([\d\s]+)", content)
    if codigo_de_barras_match:
        codigo_de_barras = codigo_de_barras_match.group(1).replace(" ", "")
        information["Código de Barras"] = codigo_de_barras

        
    return information

information = extract_information_from_txt(txt_path)

for key, value in information.items():
    print(f"{key}: {value}")
