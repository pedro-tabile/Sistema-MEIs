from datetime import datetime

# Converte string (data fornecida) para formato datetime e retorna resultado
def string_para_data(data: str):
    return datetime.strptime(data, '%d/%m/%Y')