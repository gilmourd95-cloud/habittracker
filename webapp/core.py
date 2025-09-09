# pylama: ignore=W191
from web import application
from web.template import render

URLS = (
	"/(.*)", "Home",
	"favicon.ico", "Favicon"
)
RENDER = render("templates", base="layout")

class Favicon:
	def GET(self):
		return open("favicon.ico", "rb").read()

class Home:
	def GET(self, name):
		return RENDER.index()


application = application(URLS, globals())
