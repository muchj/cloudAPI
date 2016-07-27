import webapp2
import db_models
import mod
'''
ipa = db_models.Recipe(
		styleName='IPA',
		recipeName='Citra IPA',
		malts=[
			db_models.Malt(
				maltName='2 Row Pale',
				maltWeight=21.5),
			db_models.Malt(
				maltName='Munich I',
				maltWeight=4.0)
			],
		hops=[
			db_models.Hop(
				hopName='Simcoe',
				hopWeight=4.0,
				hopAcid=14.4),
			db_models.Hop(
				hopName='Citra',
				hopWeight=4.5,
				hopAcid=12.3)
			]
		)

ipa.put()

red = db_models.Recipe(
		styleName='Red Ale',
		recipeName='Ruby Red Ale',
		malts=[
			db_models.Malt(
				maltName='2 Row Pale',
				maltWeight=21.5),
			db_models.Malt(
				maltName='Crystal 60',
				maltWeight=4.0)
			],
		hops=[
			db_models.Hop(
				hopName='Magnum',
				hopWeight=2.0,
				hopAcid=18.0),
			db_models.Hop(
				hopName='Crystal',
				hopWeight=1.5,
				hopAcid=2.3)
			]
		)

red.put()

stout = db_models.Recipe(
		styleName='Stout',
		recipeName='Chocolate Stout',
		malts=[
			db_models.Malt(
				maltName='2 Row Pale',
				maltWeight=18.0),
			db_models.Malt(
				maltName='Roasted Barley',
				maltWeight=2.0),
			db_models.Malt(
				maltName='Chocolate',
				maltWeight=1.0)
			],
		hops=[
			db_models.Hop(
				hopName='Golding',
				hopWeight=6.0,
				hopAcid=8.3)			
			]
		)

stout.put()
'''


class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write('If this is up the database should be loaded with three recipes.')
	
			
app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

app.router.add(webapp2.Route(r'/addRecipe', 'mod.AddRecipe')) 
app.router.add(webapp2.Route(r'/mod/<id:[0-9]+><:/?>', 'mod.Mod')) 
app.router.add(webapp2.Route(r'/mod/search', 'mod.ModSearch')) 
app.router.add(webapp2.Route(r'/channel', 'channel.Channel')) 
app.router.add(webapp2.Route(r'/channel/<cid:[0-9]+>/mod/<mid:[0-9]+><:/?>', 'channel.ChannelMods')) 