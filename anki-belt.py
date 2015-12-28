# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

from anki.hooks import addHook
from aqt.webview import AnkiWebView
from aqt.qt import *

class AnkiLevel:
  

     def __init__(self, mw):
       if mw:
         self.menuAction = QAction("Anki Level", mw)
         mw.connect(self.menuAction, SIGNAL("triggered()"), self.mainFunction)
         mw.form.menuTools.addSeparator()
         mw.form.menuTools.addAction(self.menuAction)

     def mainFunction(self):
       showInfo("card count: %d" % mw.col.db.scalar("select count() from cards where ivl >= 20"))
    


if __name__ != "__main__":
    # Save a reference to the toolkit onto the mw, preventing garbage collection of PyQT objects
    if mw: mw.ankilevel = AnkiLevel(mw)
else:
    print "This is a plugin for the Anki Spaced Repition learning system and cannot be run directly."
    print "Please download Anki2 from <http://ankisrs.net/>"