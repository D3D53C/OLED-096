# Author: Marc Steinebrunner
# KK Software

"""driver.py:	OLED class"""

__author__ = "Marc Steinebrunner"
__copyright__ = ""
__version__ = "Development v0.01"
__email__ = "info@time-track.eu"
__status__ = "Dev"

import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont


class OLED096:
    

    def __init__(self, DC = 23, SPI_PORT = 0,SPI_DEVICE = 0,RST = None ):
        # Raspberry Pi pin configuration:
        # on the PiOLED this pin isnt used
        # Note the following are only used with SPI:

        # 128x32 display with hardware I2C:
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
        self.disp.begin()

        # Clear display.
        self.disp.clear()
        self.disp.display()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.width = self.disp.width
        self.height = self.disp.height
        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = -2
        self.top = padding
        self.bottom = self.height-padding
        # Move left to right keeping track of the current x position for drawing shapes.
        self.x = 0


        self.image = Image.new('1', (self.width, self.height))

        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0,0,self.width, self.height), outline=0, fill=0)


        # Load default font.
        self.font = ImageFont.load_default()


    def clear(self):
         # Clear display.
        self.disp.clear()
        self.disp.display()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.

        # Draw a black filled box to clear the image.

        ImageDraw.Draw(Image.new('1', (self.disp.width, self.disp.height))).rectangle((0,0,self.width,self.height), outline=0, fill=0)

    def newText(self,String):
        self.draw.rectangle((0,0,self.disp.width,self.disp.height), outline=0, fill=0)
        # Draw Text on Left on Line 8
        self.draw.text((self.x, self.top+8),String, font=self.font, fill=255)
       
        # Display image.
        self.disp.image(self.image)
        self.disp.display()
        #time.sleep(.1)