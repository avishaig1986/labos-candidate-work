FROM python:3.11.9-alpine3.19

# Create app directory
WORKDIR /app

COPY requirements.txt .
COPY app.py .
RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python3", "app.py"  ]
