FROM debian

# Settar o diretorio
WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y python3.11-venv && \
    rm -rf /var/lib/apt/lists/*

# copiar o conteudo para o diretorio App
COPY write-rabbit.py /app
COPY requirements.txt /app
COPY .env /app

RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Ativa o ambiente virtual e atualiza os pacotes
RUN /app/venv/bin/python -m pip install --upgrade pip
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# settar variaveis 
# ENV RABBITMQ_URL="" \
#     RABBITMQ_USERNAME="" \
#     RABBITMQ_PASSWORD="" \
#     RABBITMQ_QUEUE="" \
#     RABBITMQ_PREFETCH=1

# Rodar scripts
CMD ["python3", "./write-rabbit.py"]