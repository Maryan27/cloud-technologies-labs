import requests
import threading
import time
import random

URL = "http://flask-alb-225328286.eu-central-1.elb.amazonaws.com/owner"

THREADS = 150  
DELAY = 0.1  

def send_requests():
    while True:
        try:
            r = requests.get(URL, timeout=3)
            print(f"{r.status_code} - {len(r.text)} bytes")
            time.sleep(DELAY + random.random() * 0.2)
        except Exception as e:
            print("Error:", e)

for _ in range(THREADS):
    t = threading.Thread(target=send_requests)
    t.daemon = True
    t.start()

print(f"Запущено {THREADS} потоків для навантаження на {URL}")


while True:
    time.sleep(10)

