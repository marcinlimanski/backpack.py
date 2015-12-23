#Marcin Limanski (13.12.2015) backpack module
import uuid
import json

class Storage():

	#This function will show backpack id
	def showId(self):
		return
	#This function will show backpack name
	def showName(self):
		return
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
		self.__jsonParser = JsonParser()
		self._id = str(uuid.uuid1())
		self._backpackObject = {'_id':self._id, 'name':self._name}
		self._backpackItems = {}

class ErrorMessageHandler():
	def invalidType(self):
		print('Invalid item type: expected a string')
		return

	def itemExistsInBackpack(self, name):
		print('Item: '+ str(name)+', already exists in the backpack')
		return
		
#Init the backpack Attributes
class NewBackpack(Storage):
	empCount = 0
	"""docstring for NewBackpack"""
	def __init__(self, name):
		self.name = name
		self.newBackpackAttributes = BackpackAttributes(self.name)
		self.errorMessageHandler = ErrorMessageHandler()
		NewBackpack.empCount += 1

	#This function will show backpack id
	def showId(self):
		return self.newBackpackAttributes._id
	#This function will show backpack name
	def showName(self):
		return self.newBackpackAttributes._name

	#Implementing the inheritend save method 
	def putIn(self, name , item):
		#Constructing and appending the new object to the backpack
		if(type(name) is str):
			if(name in self.newBackpackAttributes._backpackItems):
				self.errorMessageHandler.itemExistsInBackpack(name)
			else:
				self.newBackpackAttributes._backpackItems[name] = item;
		else:
			self.errorMessageHandler.invalidType()
		
	#Implementing the inhereted delete function
	def takeOut(self, name):
		if(type(name) is str):
			if(name in self.newBackpackAttributes._backpackItems):
				del self.newBackpackAttributes._backpackItems[name]
			else:
				self.errorMessageHandler.itemExistsInBackpack(name)
		else:
			self.errorMessageHandler.invalidType()

	#Implementing the inhereted
	def lookFor(self, name):
		if(type(name) is str):
			if(name in self.newBackpackAttributes._backpackItems):
				print(self.newBackpackAttributes._backpackItems[name])
			else:
				self.errorMessageHandler.itemExistsInBackpack(name)
		else:
			self.errorMessageHandler.invalidType()
		

	#This function will find the object in storage
	def showAllItems(self):
		return self.newBackpackAttributes._backpackItems

	#This function will concatinait the _backpackItems with _backpackObject, 
	#encode it in to json format and save it to local storage
	def saveBackpack(self):
		return

class PickABackpack(Storage):
	"""docstring for PickBackpack"""
	def __init__(self, name):
		self.name = name

	#This function will show backpack id
	def showId(self):
		return
	#This function will show backpack name
	def showName(self):
		return

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
		
		

		
		