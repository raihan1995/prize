FROM python:3.6
WORKDIR /service2
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5002
ENTRYPOINT ["python3", "app.py"]