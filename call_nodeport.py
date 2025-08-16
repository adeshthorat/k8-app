import requests
import time
import threading
import subprocess

def keep_requesting(url):
    print(f"📡 Sending requests to {url}. Press ENTER to stop.")
    stop_event = threading.Event()

    def stop_on_enter():
        input()  # Wait until user hits Enter
        stop_event.set()

    threading.Thread(target=stop_on_enter, daemon=True).start()

    count = 1
    while not stop_event.is_set():
        try:
            response = requests.get(url, timeout=5)
            print(f"[{count}] {response.status_code} → {response.text}")
        except Exception as e:
            print(f"[{count}] ❌ Error: {e}")
        count += 1
        time.sleep(1)  # 1 second interval

    print("🛑 Stopped sending requests.")

if __name__ == "__main__":
    node_port = input("Enter NodePort: ").strip()
    node_ip = subprocess.getoutput("minikube ip")
    url = f"http://{node_ip}:{node_port}"
    keep_requesting(url)