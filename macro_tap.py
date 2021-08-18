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
    
    #이전 버튼
    pst_back = '905 60'

    #init 화면 한가운데 버튼
    pst_init = '512 315'

    #충전타입 BType, CType 선택
    pst_chrgr_type = '724 359'

    #금액 설정
    pst_amount_chrgr = '143 355'

    #시간 설정
    pst_time_chrgr = '380 355'

    #용량 설정
    pst_vol_chrgr = '620 355'

    #설정에서 1번째 버튼
    pst_first_btn = '170 370'

    #설정에서 3번째 버튼
    pst_third_btn = '620 370'
    
    #설정에서 5번째 버튼
    pst_fifth_btn = '400 470'

    #설정 완료
    pst_complete_set = '850 430'
    
    #가득 충전
    pst_full_chrgr = '851 355'

    pst_member = '285 363'
    pst_terminate_chrgr = '843 474'
    pst_terminate_chck = '701 395'

    pst_skip_card_tag = '895 476'

    while True:
        print('Start Charger')

        device.shell(f'input tap {pst_init}')
        time.sleep(1)

        device.shell(f'input tap {pst_chrgr_type}')
        time.sleep(2)

        #================================================
        device.shell(f'input tap {pst_amount_chrgr}')
        time.sleep(2)

        device.shell(f'input tap {pst_first_btn}')
        time.sleep(1)

        device.shell(f'input tap {pst_third_btn}')
        time.sleep(1)

        device.shell(f'input tap {pst_fifth_btn}')
        time.sleep(1)

        device.shell(f'input tap {pst_complete_set}')
        time.sleep(1)

        #================================================
        #device.shell(f'input tap {pst_full_chrgr}')
        #time.sleep(3)
        #================================================

        device.shell(f'input tap {pst_member}')
        time.sleep(15)

        #device.shell(f'input tap {pst_skip_card_tag}')
        #time.sleep(10)

        now = time.localtime()
        scan_name = "%s_%s_%s_%s" %(now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
        device.shell(f'screencap -p /sdcard/Download/scan_{scan_name}.png')
        print('Saved screenshot!')
        time.sleep(3)

        device.shell(f'input tap {pst_terminate_chrgr}')
        time.sleep(3)

        device.shell(f'input tap {pst_terminate_chck}')
        print('Terminate Charger')
        time.sleep(20)


    
