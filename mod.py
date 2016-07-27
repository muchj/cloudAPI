import webapp2
from google.appengine.ext import ndb
import db_models
import json

class AddRecipe(webapp2.RequestHandler):
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Request must be a JSON request."
			return

		newRecipe = db_models.Recipe()
		styleName = self.request.get('styleName', default_value=None)
		recipeName = self.request.get('recipeName', default_value=None)
		topics = self.request.get_all('topics[]', default_value=None)

		#malts = self.request.get_all('malts[]', default_value=None)
		#hops = ndb.StructuredProperty(Hop, repeated=True)
		
		if styleName:
			newRecipe.styleName = styleName
		else:
			self.response.status = 402
			self.response.status_message = "Invalid request, styleName is required."

		if recipeName:
			newRecipe.recipeName = recipeName
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, recipeName is required."

		#if topics:
		#	newRecipe.topics = topics
		#for topic in newRecipe.topics:
		#	print topic
		#if malts:
		#	for m in malts:
		#		newRecipe.malts = db_models.Malt(maltName = m.maltName, maltWeight = m.maltWeight)

		newRecipe.put()
		out = newRecipe.to_dict()
		self.response.write(json.dumps(out))
		
	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Request must be a JSON request."
			return
		if 'id' in kwargs:
			out = ndb.Key(db_models.Recipe, int(kwargs['id'])).get().to_dict()
			self.response.write(json.dumps(out))
		else:
			q = db_models.Recipe.query()
			keys = q.fetch(keys_only=True)
			results = { 'keys' : [x.id() for x in keys]}
			self.response.write(json.dumps(results))

			#styles = q.fetch()
			#stylesOut = { 'style names: ' : [x.styleName() for x in styles]}
			#self.response.write(json.dumps(stylesOut))
	

class Mod(webapp2.RequestHandler):
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Request must be a JSON request."
			return
		new_mod = db_models.Mod()
		nick = self.request.get('nick', default_value=None)
		email = self.request.get('email', default_value=None)
		name = self.request.get('name', default_value=None)
		if nick:
			new_mod.nick = nick
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request, Nickname is required."
		if email:
			new_mod.email = email
		if name:
			new_nod.name = name
		key = new_mod.put()
		out = new_mod.to_dict()
		self.response.write(json.dumps(out))
		return

	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Request must be a JSON request."
			return
		if 'id' in kwargs:
			out = ndb.Key(db_models.Mod, int(kwargs['id'])).get().to_dict()
			self.response.write(json.dumps(out))
		else:
			q = db_models.Mod.query()
			keys = q.fetch(keys_only=True)
			results = { 'keys' : [x.id() for x in keys]}
			self.response.write(json.dumps(results))

class ModSearch(webapp2.RequestHandler):
	def post(self):
		'''
		Search for moderators
		POST body Variables:
		nick - String. Nickname
		email - String. Email address
		'''
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Request must be a JSON request."
			return
		q = db_models.Mod.query()
		if self.request.get('nick', None):
			q = q.filter(db_models.Mod.nick == self.request.get('nick'))
		if self.request.get('email', None):
			q = q.filter(db_models.Mod.email == self.request.get('email'))
		key = q.fetch(keys_only=True)
		results = { 'keys' : [x.id() for x in keys]}
		self.response.write(json.dumps(results))