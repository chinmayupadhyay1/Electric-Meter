import time
import numpy
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from bitstring import BitArray

def sign (RBdash):
	signdash=RBdash[0]
	print(signdash)
	return int(signdash)

def expo (RBdash):
	exp=RBdash[1:9]
	print(exp)
    	expdash= BitArray(bin=exp)
    	expdashdash=(expdash.uint)
	#print (int(expdashdash))
    	return int(expdashdash)
	

def mant (RBdash):
    	mant=RBdash[9:32]
    	mantdash="1."+mant
	print((mant))
	print(mantdash)
    	mantdashdash = binaryToDecimal(mantdash, len(mantdash))
	print((mantdashdash)) 
   	return float(mantdashdash)

def binaryToDecimal(binary, length) : 
      
    # Fetch the radix point  
    point = binary.find('.') 
  
    # Update point if not found  
    if (point == -1) : 
        point = length  
  
    intDecimal = 0
    fracDecimal = 0
    twos = 1
  
    # Convert integral part of binary  
    # to decimal equivalent  
    for i in range(point-1, -1, -1) :  
          
        # Subtract '0' to convert  
        # character into integer  
        intDecimal += ((ord(binary[i]) - 
                        ord('0')) * twos)  
        twos *= 2
  
    # Convert fractional part of binary  
    # to decimal equivalent  
    twos = 2
      
    for i in range(point + 1, length): 
          
        fracDecimal += ((ord(binary[i]) -
                         ord('0')) / twos);  
        twos *= 2.0
  
    # Add both integral and fractional part  
    ans = intDecimal + fracDecimal 
    return (ans)

def calc (x,y,z):
    res=pow((-1),x) * pow(2,(y-127)) * z
    return res

client = ModbusClient(method = 'rtu', port='/dev/ttyUSB0', timeout=1, stopbit=1, bytesize=8, parity='E', baudrate=9600)
client.connect()

n = "1.10010000001011100100010"
print(binaryTODecimal(n, len(n)))

while True:
    ActP=client.read_holding_registers(0x64, 0x02,unit=1)
    print ((ActP.registers))
    time.sleep(1)
    
##    Voltage=client.read_holding_registers(0x8c, 0x02,unit=1)
##    #print (Voltage.registers)
##    time.sleep(1)
##
##    Current=client.read_holding_registers(0x94, 0x02,unit=1)
##    #print (Current.registers)
##    time.sleep(1)
##
##    Frequency=client.read_holding_registers(0x9c, 0x02,unit=1)
##    #print (Frequency.registers)
##    time.sleep(1)
##
##    AptP=client.read_holding_registers(0x7c, 0x02,unit=1)
##    #print (AptP.registers)
##    time.sleep(1)
##
##    Wh=client.read_holding_registers(0x9e, 0x02,unit=1)
##    #print (Wh.registers)
##    time.sleep(1)










#    #ActivePower
#    firstActP=(ActP.registers[1])
#    secondActP=(ActP.registers[0])
#
#    R0=str(format(firstActP, '016b'))
#    R1=str(format(secondActP, '016b'))
#    RB=R0+R1
#
#    S=sign(RB)
#    E=expo(RB)
#    M=mant(RB)

#   finalActP=calc(S,E,M)
#
#    print(finalActP)
#    time.sleep(2)
 

#n = "1.10010000001011100100010"
#print(binaryToDecimal(n, len(n))








   
##    #Voltage
##    firstVol=(Voltage[1])
##    secondVol=(Voltage[0])
##
##    R0=str(format(firstVol, '016b'))
##    R1=str(format(secondVol, '016b'))
##    RB=R0+R1
##
##    S=sign(RB)
##    E=expo(RB)
##    M=mant(RB)
##
##    finalVoltage=calc(S,E,M)
##
##
##    #Current
##    firstCur=(Current[1])
##    secondVol=(Current[0])
##
##    R0=str(format(firstCur, '016b'))
##    R1=str(format(secondCur, '016b'))
##    RB=R0+R1
##
##    S=sign(RB)
##    E=expo(RB)
##    M=mant(RB)
##
##    finalCurrent=calc(S,E,M)
##
##
##    #Frequency
##    firstFre=(Frequency[1])
##    secondFre=(Frequency[0])
##
##    R0=str(format(firstFre, '016b'))
##    R1=str(format(secondFre, '016b'))
##    RB=R0+R1
##
##    S=sign(RB)
##    E=expo(RB)
##    M=mant(RB)
##
##    finalFrequency=calc(S,E,M)
##
##
##    #ApparentPower
##    firstAptP=(AptP[1])
##    secondAptP=(AptP[0])
##
##    R0=str(format(firstAptP, '016b'))
##    R1=str(format(secondAptP, '016b'))
##    RB=R0+R1
##
##    S=sign(RB)
##    E=expo(RB)
##    M=mant(RB)
##
##    finalAptP=calc(S,E,M)
##
##
##    #watt hour
##    firstWh=(Wh[1])
##    secondWh=(Wh[0])
##
##    R0=str(format(firstWh, '016b'))
##    R1=str(format(secondWh, '016b'))
##    RB=R0+R1
##
##    S=sign(RB)
##    E=expo(RB)
##    M=mant(RB)
##
##    finalWattHour=calc(S,E,M)
##
##
##    #PrintData
##    print("Active Power is " +str(finalActP)+ " Watts\n")
##    print("Voltage is " + str(finalVoltage)+ " volts\n")
##    print("Current is " + str(finalCurrent) + " Amps\n")
##    print("Frequency is " + str(finalFrequency)+ " Hertz\n")
##    print("Apparent Power is " + str(finalAptP) + " Watts\n")
##    print("Watt Hour is " +str(finalWattHour) + " Watts-Hours\n")
## 
