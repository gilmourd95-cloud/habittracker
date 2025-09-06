# pylama: ignore=W191
from web import application
from web.template import render

URLS = ("/(.*)", "home")
RENDER = render("templates")


class home:
	def GET(self, name):
		return RENDER.base(title="", head="", body=f"Hello, {name or 'World'}!")


app = application(URLS, globals())
if "__main__" == __name__:
	application.run()
else:
    application = app.wsgifunc()
