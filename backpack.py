import uuid
import json

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
	#This function will find the object in storage
	def showAllItems(self):
		return

#Init the backpack Attributes
class BackpackAttributes():
	def __init__(self, name):
		self._name = name
		self._jsonParser = JsonParser()
		self._id = str(uuid.uuid1())
		self._backpackObject = {'_id':self._id, 'name':self._name}
		self._backpackItems = {}

class NewBackpack(Storage):
	empCount = 0
	"""docstring for NewBackpack"""
	def __init__(self, name):
		self.name = name
		self.newBackpackAttributes = BackpackAttributes(self.name)
		#init the JsonParse object to handle json object
		NewBackpack.empCount += 1
	#Implementing the inheritend save method 
	def putIn(self, name , item):
		#Constructing and appending the new object to the backpack
		if(type(name) is str):
			if(name in self.newBackpackAttributes._backpackItems):
				print('This name already exists in backpack: ' + str(name))
			else:
				self.newBackpackAttributes._backpackItems[name] = item;
		else:
			print('Invalid item type: expected a string')
		return
		
	#Implementing the inhereted delete function
	def takeOut(self, name):
		if(type(name) is str):
			if(name in self.newBackpackAttributes._backpackItems):
				del self.newBackpackAttributes._backpackItems[name]
			else:
				print('Item: ' + str(name) + ' does not exists')
		else:
			print('Invalid item type: expected a string')
		return

	#Implementing the inhereted
	def lookFor(self):
		print('Find function is working')

		#This function will find the object in storage
	def showAllItems(self):
		return self.newBackpackAttributes._backpackItems

class PickABackpack(Storage):
	empCount = 0
	"""docstring for PickBackpack"""
	def __init__(self, name):
		PickBackpack.empCount += 1
	#Implementing the inheritend save method 
	def putIn(self, object):
		return
		
	#Implementing the inhereted delete function
	def takeOut(self):
		print('Delete function is working')

	#Implementing the inhereted
	def lookFor(self):
		return

	#This function will find the object in storage
	def showAllItems(self):
		return

class JsonParser():
	"""docstring for JsonParser"""
	#This method will take in a string and retrun a json object 
	def decode(self):
		print('Decoding json works')
		return
	#This method will take json object and convert it to string
	def encode(self):
		print('Encoding json works')
		return

	def formatCheck(self, object):
		try:
		    json_object = json.loads(object)
		except ValueError, e:
		    return False
		return True
		
		

		
		