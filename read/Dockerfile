FROM debian

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y python3.11-venv && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY read-rabbit.py /app
COPY requirements.txt /app
COPY .env /app

RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

RUN /app/venv/bin/python -m pip install --upgrade pip
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# ENV RABBITMQ_URL="" \
#     RABBITMQ_USERNAME="" \
#     RABBITMQ_PASSWORD="" \
#     RABBITMQ_QUEUE="" \
#     RABBITMQ_PREFETCH=1

CMD ["python3", "./read-rabbit.py"]