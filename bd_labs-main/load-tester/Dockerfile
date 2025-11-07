FROM python:3.10-slim
WORKDIR /app

RUN pip install --no-cache-dir requests

COPY load_test.py /app/load_test.py

ENV TARGET_URL="http://flask-alb-225328286.eu-central-1.elb.amazonaws.com/owner"
ENV WORKERS=20

CMD ["python", "/app/load_test.py"]
