https://micropython.org/download/ESP32_GENERIC/
https://docs.micropython.org/en/latest/esp32/quickref.html

pip3 install esptool ampy
lsusb
ls -lsha /dev/ttyUSB*
stat /dev/ttyUSB*
sudo usermod -a -G dialout $USER
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
wget https://micropython.org/resources/firmware/ESP32_GENERIC-20241025-v1.24.0.bin
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20241025-v1.24.0.bin
sudo apt-get install minicom
ampy -p /dev/ttyUSB0 ls
ampy -p /dev/ttyUSB0 get boot.py
ampy -p /dev/ttyUSB0 put main.py