import webapp2
from google.appengine.ext import ndb
import db_models
import json

class Channel(webapp2.RequestHandler)
	def post(self):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Request must be a JSON request."
			return
		new_channel = db_models.Channel()
		name = self.request.get('name', default_value=None)
		mods = self.request.get_all('mods[]', default_value=None)
		topics = self.request.get_all('topics[]', default_value=None)
		if name:
			new_channel.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Invalid Request"
		if mods:
			for mod in mods:
			new_channel.mods.append(ndb.Key(db_models.Mod, in(mod)))
		if topics:
			new_channel.topics = topics	
		for topic in new_channel.topics	
			print topic
		key = new_channel.put()
		out = new_channel.to_dict()
		self.response.write(json.dumps(out))
		return

class ChannelMods(webapp2.RequestHandler):
	def put(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Request must be a JSON request."
			return
		if 'cid' in kwargs:
			channel = ndb.Key(db_models.Channel, int(kwargs['mid']))
			if not channel:
				self.response.status = 404
				self.response.status_message = "Channel not found"
				return
		if 'mid' in kwargs:
			mod = ndb.Key(db_models.Mod, int(kwargs['mid']))
			if not channel:
				self.response.status = 404
				self.response.status_message = "Mod not found"
				return
		if mod not in channel.mods:
			channel.mods.append(mod)
			channel.put()
		self.response.write(json.dumps(channel.to_dict()))
		return
