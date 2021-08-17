import time
from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]
    print(f'Connected to {device}')
    return device, client


if __name__ == '__main__':
    device, client = connect()

    while True:
        print('Logging Start')

        device.shell(f'ps -p $(pidof com.speel.SerialTester) -o etime,NAME,%CPU,%MEM >> /sdcard/Download/res_log.txt')
        time.sleep(60)