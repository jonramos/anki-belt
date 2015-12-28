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
       #showInfo("card count: %d" % mw.col.db.scalar("select count() from cards where ivl >= 20"))
       
       #Create the main Dialog Box
       swin = QDialog(mw)

       #Create a Vertical box layout
       vl = QVBoxLayout()

       #Create a form to group other elements
       frm = QGroupBox("Settings")
       vl.addWidget(frm)

       il = QVBoxLayout()
       fl = QHBoxLayout()
       
       field = QLineEdit()
       field.setPlaceholderText("test")
       il.addWidget(QLabel("Please write a deck name or \"all\" to all decks"))
       fl.addWidget(field)

       il.addLayout(fl)
       frm.setLayout(il)

       hl = QHBoxLayout()
       vl.addLayout(hl)
       submitButton = QPushButton("Generate")
       hl.addWidget(submitButton)
       submitButton.connect(submitButton, SIGNAL("clicked()"), swin, SLOT("accept()"))
       closeButton = QPushButton("Close")
       hl.addWidget(closeButton)
       closeButton.connect(closeButton, SIGNAL("clicked()"), swin, SLOT("reject()"))
       

       #Format main Dialog Box
       swin.setLayout(vl)
       swin.setTabOrder(submitButton,closeButton)
       swin.setTabOrder(closeButton,field)
       swin.setLayout(vl)
       swin.resize(200, 150)

       if swin.exec_():
            mw.progress.start(immediate=True)
            if len(field.text().strip()) != 0: _pattern = field.text().lower()
            mw.progress.finish()
            self.win.show()

if __name__ != "__main__":
    # Save a reference to the toolkit onto the mw, preventing garbage collection of PyQT objects
    if mw: mw.ankilevel = AnkiLevel(mw)
else:
    print "This is a plugin for the Anki Spaced Repition learning system and cannot be run directly."
    print "Please download Anki2 from <http://ankisrs.net/>"