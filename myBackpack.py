# Import module backpack
import backpack
import json

myBackpack = backpack.Backpack('myBackpack')


myBackpack.putIn('marcin1', 3123)
myBackpack.putIn('marcin', 3123)

myBackpack.takeOut('marcin')
print(myBackpack.showAllItems())

myBackpack.changeName('marcinBackpack')

print(myBackpack.showName())

print(myBackpack.saveBackpack())

