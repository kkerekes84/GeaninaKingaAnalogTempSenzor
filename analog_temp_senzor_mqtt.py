
import paho.mqtt.client as mqtt
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import spidev
import time
import os
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0,0)

CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

def readadc(adcnum):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    r = spi.xfer2([1,(8+adcnum)<<4,0])
    adcout = ((r[1]&3) << 8) + r[2]
    return adcout
print('Reading Analog Temp Values values, press Ctrl-C to quit...')

def on_connect(client,userdata,flags,rc):
    print("Connected with result code"+str(rc))
    client.subscribe("AnalogTempSensorGeaninaKinga")
    

def read_temp_in_Celsius(temp):
    print ("Analog port 0")
    analog0_value = mcp.read_adc(0)
    voltage = analog0_value * 3.3
    voltage /= 1024.0
    tempCelsius = (voltage-0.5)*100
    print ("ADC: ", analog0_value)
    print ("Voltage: ", voltage)
    print ("Temp: ", tempCelsius)
    
    
    if tempCelsius < temp:
       GPIO.setmode(GPIO.BCM)
       GPIO.setup(17, GPIO.OUT)
       GPIO.output(17, True)
       GPIO.output(4, False)
       print("Temperature is lower then: ",temp)
    else:
       GPIO.setup(4, GPIO.OUT)
       GPIO.output(4, True)
       GPIO.output(17, False)
       print("Temperature is equal or higher then: ",temp)
    
def on_message(client,userdata,msg):
       print(msg.topic+" "+str(msg.payload))
       print("Received message"+" "+str(msg.payload))
       temp=int(msg.payload)
       read_temp_in_Celsius(temp)
       
client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
GPIO.output(4, False)
GPIO.output(17, False)


client.username_pw_set("vajxtpme", "TwDLq6fSD0t4")
client.connect("tailor.cloudmqtt.com", 12359, 60)

client.loop_forever()
