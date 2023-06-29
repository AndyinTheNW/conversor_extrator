# README

Este documento contém uma explicação detalhada do funcionamento dos arquivos `extractor.py` e `converter.py`, que trabalham em conjunto para realizar a conversão de arquivos PDF para TXT e extração de suas informações.

## Sobre o conversor de PDF para TXT

Este código em Python é um conversor de arquivos PDF para arquivos de texto (TXT). Ele utiliza a biblioteca `pdfminer` para extrair o texto dos arquivos PDF e salvá-lo em um arquivo TXT correspondente.

### Utilização

1. Certifique-se de ter o Python instalado em seu sistema.

2. Instale a biblioteca `pdfminer` executando o comando a seguir:

   ```
   pip install pdfminer.six
   ```

3. Defina o diretório que contém os arquivos PDF a serem convertidos:

   ```python
   input_folder = "caminho/do/diretorio"
   ```

4. Defina o diretório de saída onde os arquivos TXT serão armazenados:

   ```python
   output_folder = "caminho/do/diretorio/de/saida"
   ```

5. Execute o código para converter os arquivos PDF em arquivos TXT:

   ```python
   python nome_do_arquivo.py
   ```

   Certifique-se de substituir "nome_do_arquivo.py" pelo nome do arquivo em que o código está salvo.

6. Os arquivos TXT resultantes serão salvos no diretório de saída especificado.

Certifique-se de adaptar o código e os caminhos de diretório conforme necessário para o seu caso específico.

**Observação:** Este código foi escrito em Python 3 e requer as bibliotecas `os` e `pdfminer.high_level` para funcionar corretamente.

## Sobre o extrator de informações de arquivos .txt

Este código realiza a extração de informações de um arquivo de texto (.txt) com base em padrões definidos. O objetivo é extrair informações específicas de um documento no formato definido e armazená-las em um dicionário.

### Funcionalidades

O código possui a seguinte funcionalidade principal:

- `extract_information_from_txt(txt_path)`: Essa função recebe o caminho do arquivo de texto como entrada e retorna um dicionário contendo as informações extraídas do arquivo. As informações extraídas incluem Razão Social, Endereço, CNPJ/CPF/Insc. Est., UF, Telefone, Município, Tributo, Descrição do Tributo, Chave, Data de Vencimento, UF Favorecida, Nº de Controle, Código da Receita, Nº Documento de Origem, Período de Referência, Valor Principal, Atualização Monetária, Juros, Multa, Total a Recolher e Código de Barras.

### Uso

Para utilizar o código, siga as etapas abaixo:

1. Defina o caminho do arquivo de texto que deseja extrair as informações, atribuindo-o à variável `txt_path`.
2. Chame a função `extract_information_from_txt(txt_path)` e passe o caminho do arquivo de texto como argumento.
3. A função retornará um dicionário contendo as informações extraídas.
4. Utilize as informações conforme necessário.

Exemplo de uso:

```python
txt_path = r"C:\epson_py\guias_pdf\guias_txt\13 - GNRE - DIÁRIA - MT.txt"
information = extract_information_from_txt(txt_path)

for key, value in information.items():
    print(f"{key}: {value}")
```

Certifique-se de ter as bibliotecas necessárias instaladas, como a biblioteca `re` para expressões regulares.

### Observações

- Certifique-se de que o arquivo de texto a ser processado esteja no formato correto e contenha as informações esperadas.
- O código utiliza expressões regulares para encontrar padrões específicos no texto. Portanto, é importante que os padrões estejam corretamente definidos e sejam compatíveis com o conteúdo do arquivo de texto.
- As informações extraídas são armazenadas em um dicionário, onde as chaves representam os nomes das informações e os valores correspondem aos dados extraídos.
- O código está configurado para processar um arquivo de texto específico neste exemplo. Certifique-se de atualizar o caminho do arquivo (`txt_path`) para o arquivo desejado.


