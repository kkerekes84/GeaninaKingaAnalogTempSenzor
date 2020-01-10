import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import spidev
import time
spi = spidev.SpiDev()
spi.open(0,0)

# Software SPI configuration:
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


def readadc(adcnum):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    r = spi.xfer2([1,(8+adcnum)<<4,0])
    adcout = ((r[1]&3) << 8) + r[2]
    return adcout
print('Reading Analog Temperature sensor values values, press Ctrl-C to quit...')

# Main program loop.
while True:
    
        print "---------------------------"
	print "Analog port 0"
        analog0_value = mcp.read_adc(0)
        voltage = analog0_value * 3.3
        voltage /= 1024.0
        tempCelsius = (voltage-0.5)*100
        print "ADC: ", analog0_value
        print "Voltage: ", voltage
        print "Temp: ", tempCelsius
        
        time.sleep(0.5)
        

