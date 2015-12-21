# Import module backpack
import backpack

myBackpack = backpack.NewBackpack('myBackpack');
<<<<<<< HEAD

=======
>>>>>>> 6705d1ad31e2370d6f8b0c464e37603be7363338

myBackpack.putIn('marcin', 'dasd')
myBackpack.putIn('marcin', 'dasd')
myBackpack.putIn('marcin2', 322)

for i in range (0, 10, 1):
	myBackpack.putIn(i, i)

print(myBackpack.showAllItems())
<<<<<<< HEAD
=======

>>>>>>> 6705d1ad31e2370d6f8b0c464e37603be7363338

print(id(myBackpack))

