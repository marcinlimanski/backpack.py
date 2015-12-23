# Import module backpack
import backpack

myBackpack = backpack.NewBackpack('myBackpack')

def testClassInit():
	if(myBackpack._name == 'myBackpack'):
		print('Passed: testClassInit')
	else:
		print('FAILED: testClassInit')

def testBackpackMultiInstance():
	myBackpack = backpack.NewBackpack('myBackpack')

def testBackpackPutInMethod():



testClassInit()


