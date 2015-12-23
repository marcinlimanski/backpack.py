# Import module backpack
import backpack

myBackpack = backpack.NewBackpack('myBackpack')


myBackpack.putIn('marcin1', 3123)
myBackpack.putIn('marcin', 3123)

print(myBackpack.showAllItems())

myBackpack.takeOut('marcin')
print(myBackpack.showAllItems())

print(myBackpack.empCount)
