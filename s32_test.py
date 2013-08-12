'''
Test code for protoboard with:
* Sainsmart 3.2"
'''

from fbtft import *


prerequisites()

ensure_no_spi()
ensure_fbtft()


#  Adapter board
#  -------------
#      WR      RESET    LED-A
#    GPIO31    GPIO29    3V3

#  P5 header
#  ---------
#  Facing RCA, upside
#  
#  GND  GPIO31  GPIO29  3V3
#  GND  GPIO30  GPIO28  5V0


GPIOS = "reset:29,dc:2,wr:31,db00:11,db01:9,db02:10,db03:22,db04:27,db05:17,db06:4,db07:3,db08:7,db09:8,db10:25,db11:24,db12:23,db13:18,db14:14,db15:15"


for rotate in [0,1,2,3]:
	with FBTFTdevice("sainsmart32", dev={ 'rotate':rotate, 'gpios':GPIOS }, autoload=True) as dev:
		console_test()
		if rotate == 0:
			fbtest()
			startx_test()
#			bl_power_test(dev)
		if rotate % 2:
			mplayer_test(320, 240)
		else:
			mplayer_test(240, 320)


# flexfb
for rotate in [0,1,2,3]:
	if rotate == 0:
		flexfb_drv_args = { 'chip':'ssd1289', 'buswidth':16 }
	elif rotate == 1:
		flexfb_drv_args = { 'chip':'ssd1289', 'buswidth':16, 'init':"-1,0x00,0x0001,-1,0x03,0xA8A4,-1,0x0C,0x0000,-1,0x0D,0x080C,-1,0x0E,0x2B00,-1,0x1E,0x00B7,-1,0x01,0x2B3F,-1,0x02,0x0600,-1,0x10,0x0000,-1,0x11,0x6068,-1,0x05,0x0000,-1,0x06,0x0000,-1,0x16,0xEF1C,-1,0x17,0x0003,-1,0x07,0x0233,-1,0x0B,0x0000,-1,0x0F,0x0000,-1,0x41,0x0000,-1,0x42,0x0000,-1,0x48,0x0000,-1,0x49,0x013F,-1,0x4A,0x0000,-1,0x4B,0x0000,-1,0x44,0xEF00,-1,0x45,0x0000,-1,0x46,0x013F,-1,0x30,0x0707,-1,0x31,0x0204,-1,0x32,0x0204,-1,0x33,0x0502,-1,0x34,0x0507,-1,0x35,0x0204,-1,0x36,0x0204,-1,0x37,0x0502,-1,0x3A,0x0302,-1,0x3B,0x0302,-1,0x23,0x0000,-1,0x24,0x0000,-1,0x25,0x8000,-1,0x4f,0x0000,-1,0x4e,0x0000,-1,0x22,-3" }
	elif rotate == 2:
		flexfb_drv_args = { 'chip':'ssd1289', 'buswidth':16, 'init':"-1,0x00,0x0001,-1,0x03,0xA8A4,-1,0x0C,0x0000,-1,0x0D,0x080C,-1,0x0E,0x2B00,-1,0x1E,0x00B7,-1,0x01,0x2B3F,-1,0x02,0x0600,-1,0x10,0x0000,-1,0x11,0x6040,-1,0x05,0x0000,-1,0x06,0x0000,-1,0x16,0xEF1C,-1,0x17,0x0003,-1,0x07,0x0233,-1,0x0B,0x0000,-1,0x0F,0x0000,-1,0x41,0x0000,-1,0x42,0x0000,-1,0x48,0x0000,-1,0x49,0x013F,-1,0x4A,0x0000,-1,0x4B,0x0000,-1,0x44,0xEF00,-1,0x45,0x0000,-1,0x46,0x013F,-1,0x30,0x0707,-1,0x31,0x0204,-1,0x32,0x0204,-1,0x33,0x0502,-1,0x34,0x0507,-1,0x35,0x0204,-1,0x36,0x0204,-1,0x37,0x0502,-1,0x3A,0x0302,-1,0x3B,0x0302,-1,0x23,0x0000,-1,0x24,0x0000,-1,0x25,0x8000,-1,0x4f,0x0000,-1,0x4e,0x0000,-1,0x22,-3" }
	elif rotate == 3:
		flexfb_drv_args = { 'chip':'ssd1289', 'buswidth':16, 'init':"-1,0x00,0x0001,-1,0x03,0xA8A4,-1,0x0C,0x0000,-1,0x0D,0x080C,-1,0x0E,0x2B00,-1,0x1E,0x00B7,-1,0x01,0x2B3F,-1,0x02,0x0600,-1,0x10,0x0000,-1,0x11,0x6058,-1,0x05,0x0000,-1,0x06,0x0000,-1,0x16,0xEF1C,-1,0x17,0x0003,-1,0x07,0x0233,-1,0x0B,0x0000,-1,0x0F,0x0000,-1,0x41,0x0000,-1,0x42,0x0000,-1,0x48,0x0000,-1,0x49,0x013F,-1,0x4A,0x0000,-1,0x4B,0x0000,-1,0x44,0xEF00,-1,0x45,0x0000,-1,0x46,0x013F,-1,0x30,0x0707,-1,0x31,0x0204,-1,0x32,0x0204,-1,0x33,0x0502,-1,0x34,0x0507,-1,0x35,0x0204,-1,0x36,0x0204,-1,0x37,0x0502,-1,0x3A,0x0302,-1,0x3B,0x0302,-1,0x23,0x0000,-1,0x24,0x0000,-1,0x25,0x8000,-1,0x4f,0x0000,-1,0x4e,0x0000,-1,0x22,-3" }
	with FBTFTdevice("flexfb", devname="flexpfb", dev={ 'rotate':rotate, 'gpios':GPIOS }, drv=flexfb_drv_args) as dev:
		if rotate in [0,2]:
			mplayer_test(240, 320)
		else:
			mplayer_test(320, 240)
