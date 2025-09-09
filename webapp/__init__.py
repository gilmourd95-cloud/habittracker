# pylama: ignore=W191
from .core import application

__all__ = ["application"]

if "__main__" != __name__:
    application.wsgifunc()
