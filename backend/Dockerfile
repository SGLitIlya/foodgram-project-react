FROM python:3.11
WORKDIR /backend

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

COPY --from=ghcr.io/ufoscout/docker-compose-wait:latest /wait /wait

ADD entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

CMD /wait && /entrypoint.sh
