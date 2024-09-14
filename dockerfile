# Use uma imagem base com Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Exponha a porta em que sua aplicação vai rodar
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
