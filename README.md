# README - Conversor de PDF para TXT e Extrator de Informações

Este documento explica o funcionamento dos arquivos `extractor.py` e `converter.py`, que trabalham juntos para converter arquivos PDF em TXT e extrair informações desses arquivos.

## Conversor de PDF para TXT

O código em Python é um conversor de arquivos PDF para arquivos de texto (TXT) usando a biblioteca `pdfminer`. Ele permite extrair texto de arquivos PDF e salvar em TXT.

### Uso

1. Certifique-se de ter Python instalado.

2. Instale a biblioteca `pdfminer`:

   ```
   pip install pdfminer.six
   ```

3. Defina o diretório de entrada com arquivos PDF:

   ```python
   input_folder = "caminho/do/diretorio"
   ```

4. Escolha um diretório de saída para arquivos TXT:

   ```python
   output_folder = "caminho/do/diretorio/de/saida"
   ```

5. Execute o código:

   ```python
   python nome_do_arquivo.py
   ```

   Substitua "nome_do_arquivo.py" pelo nome do arquivo Python.

6. Os arquivos TXT gerados estarão no diretório de saída.

Adapte o código e caminhos conforme necessário.

**Nota:** O código é para Python 3 e requer as bibliotecas `os` e `pdfminer.high_level`.

## Extrator de Informações de Arquivos .txt

Este código extrai informações de um arquivo de texto (.txt) com base em padrões definidos, armazenando-as em um dicionário.

### Funcionalidades

- `extract_information_from_txt(txt_path)`: Recebe o caminho do arquivo de texto e retorna um dicionário com informações extraídas, como Razão Social, Endereço, CNPJ/CPF, entre outras.

### Uso

1. Defina o caminho do arquivo de texto em `txt_path`.

2. Chame a função `extract_information_from_txt(txt_path)` com o caminho como argumento.

3. O dicionário retornado contém as informações extraídas.

Exemplo:

```python
txt_path = "caminho/para/arquivo.txt"
information = extract_information_from_txt(txt_path)

for key, value in information.items():
    print(f"{key}: {value}")
```

Certifique-se de ter a biblioteca `re` instalada.

### Observações

- O arquivo de texto deve estar no formato correto com as informações esperadas.

- O código usa expressões regulares para encontrar padrões no texto, então defina padrões apropriados.

- As informações extraídas são armazenadas em um dicionário, onde as chaves são nomes das informações e os valores são os dados extraídos.

- O código é configurado para processar um arquivo de texto específico, então atualize `txt_path` conforme necessário.
