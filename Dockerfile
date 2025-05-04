FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY app /app/app
COPY run.py /app/run.py

WORKDIR /app
EXPOSE 5000

ENV SECRET_KEY=your-secure-key
ENV AWS_API_URL=http://ec2-13-49-46-41.eu-north-1.compute.amazonaws.com/api/predict/upload

CMD ["python", "/app/run.py"]