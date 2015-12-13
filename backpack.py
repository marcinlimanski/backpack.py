#Marcin Limanski (13.12.2015) backpack module
class Storage():
	"""docstring for Storage"""
	#This function will save a given object
	def save(self, name):
		print('Save funstion is working ' + name)

	#This function will delete the object 
	def delete(self):
		print('Delete function is working')

	#This function will find the object in storage
	def find(self):
		print('Find function is working')


class Backpack(Storage):
	empCount = 0
	"""docstring for Backpack"""
	def __init__(self):
		Backpack.empCount += 1
	#Implementing the inheritend save method 
	def putIn(self, name):
		self.save(name)		

	#Implementing the inhereted delete function
	def takeOut(self, ):
		delete()

	#Implementing the inhereted
	def lookFor(self, ):
		find()

		