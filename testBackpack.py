# Import module backpack
import backpack

myBackpack = backpack.NewBackpack('myBackpack');


myBackpack.putIn('marcin', 'dasd')
myBackpack.putIn('marcin', 'dasd')
myBackpack.putIn('marcin2', 322)

for i in range (0, 10, 1):
	myBackpack.putIn(i, i)

print(myBackpack.showAllItems())

print(id(myBackpack))

