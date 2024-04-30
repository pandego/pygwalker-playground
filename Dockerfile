FROM python:3.11-slim

WORKDIR /app

RUN apt update -y && apt install -y curl wget nano build-essential make

COPY . .

RUN pip install poetry==1.8.2
RUN poetry config virtualenvs.create false
RUN poetry install -vvv

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]