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

class NewBackpack(Storage):
	empCount = 0
	"""docstring for NewBackpack"""
	def __init__(self, name):
		#init the JsonParse object to handle json object
		self.jsonParser = JsonParser()
		self.name = name
		self._id = str(uuid.uuid1())
		self.backpackObject = {'_id':self._id, 'name':self.name, 'items':[]}
		NewBackpack.empCount += 1
	#Implementing the inheritend save method 
	def putIn(self, name, item):
		#Constructing and appending the new object to the backpack
		self.backpackObject['items'].append({'_id':str(uuid.uuid1()),'name':name, 'item':item})
		
		#TODO: check if the backpack object file exists, if not create one and save the obejct
		
		#TODO: if backpack exists then load it, deserilaise it to json, append new object to the back pack
		#then save it to the file
		return
		
	#Implementing the inhereted delete function
	def takeOut(self):
		print('Delete function is working')

	#Implementing the inhereted
	def lookFor(self):
		print('Find function is working')

		#This function will find the object in storage
	def showAllItems(self):
		return self.backpackObject

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
		
		

		
		