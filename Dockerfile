FROM python:2-alpine

MAINTAINER John Harris <john@johnharris.io>

COPY . /app

WORKDIR /app

EXPOSE 5000

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
