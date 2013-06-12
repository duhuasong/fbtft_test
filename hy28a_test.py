'''
Test code for:
* HY28A
'''

from fbtft import *


prerequisites()

ensure_spi()
ensure_fbtft()

os.environ['DISPLAY'] = ":0"


for rotate in [0,1,2,3]:
#for rotate in [0]:
	with FBTFTdevice("hy28afb", dev={'rotate':rotate, 'gpios':"reset:25,led:18"}) as dev:
		console_test()
		ads7846args = { 'x_min':230, 'x_max':3850, 'y_min':190, 'y_max':3850, 'x_plate_ohms':60, 'pressure_max':255, 'gpio_pendown':17 }
		if rotate % 2:
			ads7846args['swap_xy'] = 1
		with ADS7846device(dev=ads7846args):
			x = startx_test(wait=False)
			time.sleep(3)
			if rotate == 1:
				call(["xinput", "--set-prop", 'ADS7846 Touchscreen', 'Evdev Axis Inversion', '0', '1'])
			if rotate == 2:
				call(["xinput", "--set-prop", 'ADS7846 Touchscreen', 'Evdev Axis Inversion', '1', '1'])
			if rotate == 3:
				call(["xinput", "--set-prop", 'ADS7846 Touchscreen', 'Evdev Axis Inversion', '1', '0'])
			while x.poll() == None:
				time.sleep(0.5)

		if rotate % 2:
			mplayer_test(320, 240)
		else:
			mplayer_test(240, 320)
		if rotate == 0:
			fbtest()
			bl_power_test(dev)
			blank_test(dev)

# flexfb
flexfb_drv_args = { 'width':240, 'height':320, 'regwidth':16, 'setaddrwin':1, 'init':"-1,0x00E5,0x8000,-1,0x0000,0x0001,-1,0x0001,0x0100,-1,0x0002,0x0700,-1,0x0003,0x1030,-1,0x0004,0x0000,-1,0x0008,0x0202,-1,0x0009,0x0000,-1,0x000A,0x0000,-1,0x000C,0x0000,-1,0x000D,0x0000,-1,0x000F,0x0000,-1,0x0010,0x0000,-1,0x0011,0x0007,-1,0x0012,0x0000,-1,0x0013,0x0000,-2,200,-1,0x0010,0x17B0,-1,0x0011,0x0031,-2,50,-1,0x0012,0x0138,-2,50,-1,0x0013,0x1800,-1,0x0029,0x0008,-2,50,-1,0x0020,0x0000,-1,0x0021,0x0000,-1,0x0030,0x0000,-1,0x0031,0x0505,-1,0x0032,0x0004,-1,0x0035,0x0006,-1,0x0036,0x0707,-1,0x0037,0x0105,-1,0x0038,0x0002,-1,0x0039,0x0707,-1,0x003C,0x0704,-1,0x003D,0x0807,-1,0x0050,0x0000,-1,0x0051,0x00EF,-1,0x0052,0x0000,-1,0x0053,0x013F,-1,0x0060,0x2700,-1,0x0061,0x0001,-1,0x006A,0x0000,-1,0x0080,0x0000,-1,0x0081,0x0000,-1,0x0082,0x0000,-1,0x0083,0x0000,-1,0x0084,0x0000,-1,0x0085,0x0000,-1,0x0090,0x0010,-1,0x0092,0x0000,-1,0x0093,0x0003,-1,0x0095,0x0110,-1,0x0097,0x0000,-1,0x0098,0x0000,-1,0x0007,0x0173,-3" }
with FBTFTdevice("flexfb", dev={ 'mode':3, 'startbyte':0x70 }, drv=flexfb_drv_args) as dev:
	mplayer_test(240, 320)