FROM python:latest
WORKDIR /app
COPY app.py
RUN pip install -r requirememts.txt
COPY . .

CMD["python", "app.py"]
