# android_ui_autotest
Android Display Automatic Test Tool

//파일 업로드   
adb push everon_charger.apk /sdcard/Download   
adb push everon_installer.apk /sdcard/Download   
adb push watch_dog.apk /sdcard/Download   

//파일 다운로드   
adb pull /sdcard/Download/test_01.txt   

//root 권한   
adb root   

//어플 삭제   
adb shell pm uninstall com.speel.SerialTester   
adb shell pm uninstall com.everon.everon_installer   
adb shell pm uninstall com.everon.watchdog_proc   

//어플 설치   
adb shell pm install -r /sdcard/Download/everon_charger.apk   
adb shell pm install -r /sdcard/Download/everon_installer.apk   
adb shell pm install -r /sdcard/Download/watch_dog.apk   

//어플 실행   
adb shell am start -n com.speel.SerialTester/com.speel.SerialTester.startup   

//설치된 어플 리스트   
adb shell pm list package   

//실행 Activity 찾기   
adb shell pm dump com.speel.SerialTester   

//어플 강제 종료하기   
adb shell am force-stop com.speel.SerialTester   
adb shell am force-stop com.everon.watchdog_proc   

//파일삭제   
adb shell rm /sdcard/Download/everon_installer.apk   
adb shell rm /sdcard/Download/watch_dog.apk   
adb shell rm /sdcard/Download/everon_charger.apk   

//폴더삭제   
adb shell -r /sdcard/Download/test_folder   

//화면캡쳐(파일이름 변경해주어야함)   
adb shell screencap -p /sdcard/Download/screen_01.png & adb pull /sdcard/Download/screen_01.png C:\Users\hyeok\Desktop/screen_01.png
