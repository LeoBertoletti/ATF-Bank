import requests
from openpyxl import Workbook

# Faz a requisição GET na API do Github
response = requests.get('https://api.github.com/repositories')

# Cria um arquivo Excel e adiciona uma planilha
workbook = Workbook()
worksheet = workbook.active
worksheet.title = 'Repositórios'

# Adiciona cabeçalhos das colunas
worksheet.append(['ID', 'Nome', 'Descrição', 'JSON'])

# Variáveis para contar os repositórios com e sem a palavra "JSON" na descrição
count_with_json = 0
count_without_json = 0

# Percorre os repositórios e adiciona as informações na planilha
for repo in response.json():
    description = repo['description']
    if description is not None:
        has_json = 'Sim' if 'json' in description.lower() else 'Não'
    else:
        has_json = 'Não'
    if has_json == 'Sim':
        count_with_json += 1
    else:
        count_without_json += 1

# Adiciona a quantidade de repositórios com e sem "JSON" na descrição
worksheet.append(['Total com JSON', '', '', count_with_json])
worksheet.append(['Total sem JSON', '', '', count_without_json])

# Salva o arquivo Excel
workbook.save('repos.xlsx')
