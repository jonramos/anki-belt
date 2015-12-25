# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

def mainFunction():

    showInfo("card count: %d" % mw.col.db.scalar("select count() from cards where ivl >= 20"))



# create a new menu item based in parameter
action = QAction("My Anki Level", mw)
# set it to call a function when it's clicked
mw.connect(action, SIGNAL("triggered()"), mainFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)