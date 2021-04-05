FROM python:3.6
WORKDIR /service3
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5003
ENTRYPOINT ["python3", "app.py"]