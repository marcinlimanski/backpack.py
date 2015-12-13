import uuid

#Marcin Limanski (13.12.2015) backpack module
class Storage():
	empCount = 0
	"""docstring for Storage"""
	def __init__(self):
		Storage.empCount += 1
	#This function will save a given object
	def putIn(self):
		return

	#This function will delete the object 
	def takeOut(self):
		return

	#This function will find the object in storage
	def lookFor(self):
		return

class Backpack(Storage):
	empCount = 0
	"""docstring for Backpack"""
	def __init__(self):
		Backpack.empCount += 1
	#Implementing the inheritend save method 
	def putIn(self, name):
		newID = IdGen()
		id = newID.generateID()
		print('Save funstion is working ' + name)
		print(type(id))

	#Implementing the inhereted delete function
	def takeOut(self):
		print('Delete function is working')

	#Implementing the inhereted
	def lookFor(self):
		print('Find function is working')

class IdGen():
	empCount = 0
	"""docstring for IdGen"""
	def __init__(self):
		IdGen.empCount += 1
	#Retruns a unique id based on the host ID and current time
	def generateID(self):
		return uuid.uuid1()
		
		