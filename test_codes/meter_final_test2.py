import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method = 'rtu', port='/dev/ttyUSB0', timeout=1, stopbit=1, bytesize=8, parity='E', baudrate=9600)
client.connect()

AllReg=client.read_holding_registers(0x64 , 0x70,unit=1)
print (AllReg.registers)
time.sleep(1
