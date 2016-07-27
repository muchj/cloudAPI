from google.appengine.ext import ndb

class Model(ndb.Model):
	def to_dict(self):
		d = super(Model, self).to_dict()
		d['key'] = self.key.id()
		return d

class Update(Model):
	date_time = ndb.DateTimeProperty(required=True)
	user_count = ndb.IntegerProperty(required=True)
	message_count = ndb.IntegerProperty(required=True)

class Channel(Model):
	name = ndb.StringProperty(required=True)
	topics = ndb.StringProperty(required=True)
	mods = ndb.KeyProperty(repeated=True)
	updates = ndb.StructuredProperty(Update, repeated=True)

	def to_dict(self):
		d = super(Channel,self).to_dict()
		d['mods'] = [m.id() for m in d['mods']]
		return d

class Mod(Model):
	nick = ndb.StringProperty(required=True)
	email = ndb.StringProperty()
	name = ndb.StringProperty()


class Malt(Model):
	maltName = ndb.StringProperty()
	maltWeight = ndb.FloatProperty()

class Hop(Model):
	hopName = ndb.StringProperty()
	hopWeight = ndb.FloatProperty()
	hopAcid = ndb.FloatProperty()

class Recipe(Model):
	styleName = ndb.StringProperty()
	recipeName = ndb.StringProperty()	
	malts = ndb.KeyProperty(repeated=True)
	hops = ndb.KeyProperty(repeated=True)

	def to_dict(self):
		d = super(Recipe,self).to_dict()
		d['malts'] = [m.id() for m in d['malts']]
		return d

