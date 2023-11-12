import socket
import time
import sys
import argparse
import requests

def tcp_ping(host, port, timeout=1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    start_time = time.time()
    try:
        s.connect((host, port))
        elapsed_time = time.time() - start_time
        s.close()
        return round(elapsed_time * 1000) 
    except socket.error:
        return None
def main():

    parser = argparse.ArgumentParser(description="TCP Ping Tool")
    parser.add_argument("host", type=str, help="Target IP address")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port")
    
    args = parser.parse_args()

    try:
        response = requests.get(f"http://ip-api.com/json/{args.host}")
        response.raise_for_status()
        data = response.json()

        if data['status'] == 'success':
            print(f"\033[1;32mCountry: \033[0m{data['country']}")
            print(f"\033[1;32mCountry Code: \033[0m{data['countryCode']}")
            print(f"\033[1;32mRegion Name: \033[0m{data['regionName']}")
            print(f"\033[1;32mCity: \033[0m{data['city']}")
            print(f"\033[1;32mTimezone: \033[0m{data['timezone']}")
            print(f"\033[1;32mAS: \033[0m{data['as']}")
        else:
            print("Không thể lấy thông tin IP. Lỗi:", data['message'])
    except requests.RequestException as e:
        print(f"Xảy ra lỗi khi kết nối tới dịch vụ IP API: {e}")
    print("---------------------------------------------------------")
    time.sleep(2.5)
    attempted = 0
