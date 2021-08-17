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

    pst_init = '512 315'

    pst_chrgr_type = '724 359'
    pst_full_chrgr = '851 355'
    pst_member = '285 363'
    pst_terminate_chrgr = '843 474'
    pst_terminate_chck = '701 395'

    pst_skip_card_tag = '895 476'

    while True:
        print('Start Charger')

        device.shell(f'input tap {pst_init}')
        time.sleep(3)

        device.shell(f'input tap {pst_chrgr_type}')
        time.sleep(3)

        device.shell(f'input tap {pst_full_chrgr}')
        time.sleep(3)

        device.shell(f'input tap {pst_member}')
        time.sleep(15)

        #device.shell(f'input tap {pst_skip_card_tag}')
        #time.sleep(10)

        now = time.localtime()
        scan_name = "scan_%s-%s_%s:%s" %(now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
        device.shell(f'screencap -p /sdcard/Download/scan_{scan_name}.png')
        print('Saved screenshot!')
        time.sleep(3)

        device.shell(f'input tap {pst_terminate_chrgr}')
        time.sleep(3)

        device.shell(f'input tap {pst_terminate_chck}')
        print('Terminate Charger')
        time.sleep(20)


    
