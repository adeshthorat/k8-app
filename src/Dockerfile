FROM python:3.9-slim
#this will create /app directory in docker container
WORKDIR /app 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#copy code from cur path to docker working directory
COPY k8app.py .

CMD ["python", "k8app.py"]
