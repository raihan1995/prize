FROM python:3.6
WORKDIR /service1
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5001
ENTRYPOINT ["python3", "app.py"]