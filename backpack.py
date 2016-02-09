#Marcin Limanski (13.12.2015) backpack module
import uuid
import json

#TODO: Check how to implement interfaces 

#Abstract class
class Storage():
	"""docstring for Storage"""
	#This method will show backpack id
	def showId(self):
		raise NotImplementedError( "Should have implemented this" )
	#This method will show backpack name
	def showName(self):
		raise NotImplementedError( "Should have implemented this" )
	#Implementing the inheritend save method 
	def putIn(self, name , item):
		raise NotImplementedError( "Should have implemented this" )
	#Implementing the inhereted delete method
	def takeOut(self, name):
		raise NotImplementedError( "Should have implemented this" )
	#Implementing the inhereted
	def lookFor(self, name):
		raise NotImplementedError( "Should have implemented this" )
	#This method will find the object in storage
	def showAllItems(self):
		raise NotImplementedError( "Should have implemented this" )
	#This method will allow to change the name of the backpack
	def changeName(self, newBackpackName):
		raise NotImplementedError( "Should have implemented this" )

class BackpackStorage(Storage):
	def __init__(self):
		self.name = 'defaultBackpack'
		self.jsonParser = None
		self.newBackpackAttributes = None
		self.errorMessageHandler = None
		self.backpackTools = None

	#This method will show backpack id
	def showId(self):
		return self.newBackpackAttributes._id
	#This method will show backpack name
	def showName(self):
		return self.newBackpackAttributes._name

	#Implementing the inheritend save method 
	def putIn(self, name , item):
		#Constructing and appending the new object to the backpack
		if(type(name) is str):
			if(name in self.newBackpackAttributes.backpackItems):
				self.errorMessageHandler.itemExistsInBackpack(name)
			else:
				self.newBackpackAttributes.backpackItems[name] = item;
		else:
			self.errorMessageHandler.invalidType()
		
	#Implementing the inhereted delete method
	def takeOut(self, name):
		if(type(name) is str):
			if(name in self.newBackpackAttributes.backpackItems):
				del self.newBackpackAttributes.backpackItems[name]
			else:
				self.errorMessageHandler.itemExistsInBackpack(name)
		else:
			self.errorMessageHandler.invalidType()

	#Implementing the inhereted
	def lookFor(self, name):
		if(type(name) is str):
			if(name in self.newBackpackAttributes.backpackItems):
				print(self.newBackpackAttributes.backpackItems[name])
			else:
				self.errorMessageHandler.itemExistsInBackpack(name)
		else:
			self.errorMessageHandler.invalidType()
		

	#This method will find the object in storage
	def showAllItems(self):
		return self.newBackpackAttributes.backpackItems

	#This method will allow to change the name of the backpack
	def changeName(self, newBackpackName):
		self.newBackpackAttributes._name = newBackpackName
		return
		

#Init the backpack Attributes
class Backpack(BackpackStorage):
	empCount = 0
	"""docstring for Backpack"""
	def __init__(self, name = 'defaultBackpack'):
		self.name = name
		self.jsonParser = JsonParser()
		self.newBackpackAttributes = BackpackAttributes(self.name)
		self.errorMessageHandler = ErrorMessageHandler()
		self.backpackTools = BackpackTools()
		Backpack.empCount += 1

	#This method is used to save the backpack in local storage
	def saveBackpack(self):
		self.jsonParser.encode(self.backpackTools.objectConcatination(self.newBackpackAttributes._id,
		 																self.newBackpackAttributes._name
		 																,self.newBackpackAttributes.backpackItems), 
																		self.newBackpackAttributes._name)
	def loadBackpack(self, filePath):
		dataObject = self.jsonParser.decode(filePath)
		self.name = dataObject['name']
		self.newBackpackAttributes._id = dataObject['_id']
		self.newBackpackAttributes.backpackItems = dataObject['items']

class BackpackTools():
	"""docstring for BackpackTools"""
	#Concatinating the backpack object to be then saved
	def objectConcatination(self, objectId, objectName, objectItems):
		print(type(objectId))
		print(type(objectName))
		print(type(objectItems))
		if((type(objectName) is str) and (type(objectItems) is dict)):
			backpackObject = {'_id':objectId, 'name':objectName, 'items':objectItems}
			return backpackObject

#Init the backpack Attributes
class BackpackAttributes():
	def __init__(self, name):
		self._name = name
		self._id = str(uuid.uuid1())
		self.backpackItems = {}

class ErrorMessageHandler():
	def invalidType(self):
		print('Invalid item type: expected a string')
		return

	def itemExistsInBackpack(self, name):
		print('Item: '+ str(name)+', already exists in the backpack')
		return
		
class JsonParser():
	"""docstring for JsonParser"""
	#This method will take in a string and retrun a json object 
	def decode(self, filePath):
		#Split this method to two parts
		print(filePath)
		try:
			with open('./'+filePath +'.json', 'r+') as data_file:   
    				data = json.load(data_file)
    				data_file.close()
    				return data
		except IOError as e:
		    print "I/O error({0}): {1}".format(e.errno, e.strerror)
	#This method will take json object and convert it to string
	def encode(self, dataObject, fileName, path = './'):
		#Split this method to two parts
		try:
		    fo = open(fileName+'.json', 'w+')
		    fo.write(json.dumps(dataObject))
		    fo.close()
		except IOError as e:
		    print "I/O error({0}): {1}".format(e.errno, e.strerror)


#####################backpack.py test########################################
if __name__ == '__main__':
	myBackpack = Backpack('myBackpack')
	
	
	#print(myBackpack.showAllItems())
	#myBackpack.putIn('marcin12', 3123)
	#print(myBackpack.showAllItems())
	#myBackpack.saveBackpack()
	
	myBackpack.loadBackpack('myBackpack')
	print(myBackpack.showAllItems())
	myBackpack.putIn('marcin2', 3123)
	#myBackpack.saveBackpack()

	myBackpack.takeOut('marcin12')

	print(myBackpack.showAllItems())
	print(myBackpack.showName())
	print(myBackpack.showId())
	myBackpack.saveBackpack()
	
		