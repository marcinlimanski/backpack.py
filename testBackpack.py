# Import module backpack
import backpack

myBackpack = backpack.NewBackpack('myBackpack');
myBackpack2 = backpack.NewBackpack('myBackpack2');

myBackpack.putIn('marcin', 'dasd')
myBackpack.putIn('marcin', 'dasd')
myBackpack.putIn('marcin2', 322)

for i in range (0, 10, 1):
	myBackpack2.putIn(i, i)

print(myBackpack.showAllItems())
print(myBackpack2.showAllItems())

print(id(myBackpack))
print(id(myBackpack2))
