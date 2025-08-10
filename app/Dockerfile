FROM python:3.13-alpine
# Создаём непривилегированного пользователя
RUN addgroup -S groupapp && adduser -S userapp -G groupapp

RUN pip install --upgrade pip

EXPOSE 4000

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

USER userapp

CMD ["python", "main.py"]