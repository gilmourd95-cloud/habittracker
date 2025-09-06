# pylama: ignore=W191
from web import application
from web.template import render

URLS = ("/(.*)", "home")
RENDER = render("templates")


class home:
	def GET(self, name):
		return RENDER.base(title="", head="", body=f"Hello, {name or 'World'}!")


if "__main__" == __name__:
	app = application(URLS, globals())
	app.run()
