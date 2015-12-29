# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

import time,codecs,math,os,unicodedata
from anki.js import jquery
from aqt.utils import showInfo
from anki.utils import ids2str
from anki.hooks import addHook
from aqt.webview import AnkiWebView

class AnkiLevel:
  

     def __init__(self, mw):
       if mw:
         self.menuAction = QAction("Anki Level", mw)
         mw.connect(self.menuAction, SIGNAL("triggered()"), self.displayResult)
         mw.form.menuTools.addSeparator()
         mw.form.menuTools.addAction(self.menuAction)

     def generateHTML(self):
     	 matureCards =  mw.col.db.scalar("select count() from cards where ivl >= 20")
         int(matureCards)
         #deckname = mw.col.decks.name(self.did).rsplit('::',1)[-1]
         #if saveMode: cols = _wide
         #else: cols = _thin
         self.html  = "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"/>\n"
         self.html += "<html><head><title>Anki Kanji Grid</title></head><body bgcolor=\"#FFF\">\n"
         self.html += "Your Anki Level is<br>\n"
         self.html += "<b>hello world</b></body></html>\n"

     #Method called if "Submit" is clicked
     def displayResult(self):
         self.generateHTML();

         self.win = QDialog(mw)
         self.wv = AnkiWebView()
         vl = QVBoxLayout()
         vl.setMargin(0)

         vl.addWidget(self.wv)
         self.wv.stdHtml(self.html)


         self.win.setLayout(vl)
         self.win.resize(500, 400)
         self.win.show()
         return 0

     #This funcion is not used in 1.x.x version
     def mainFunction(self):
       
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
       submitButton = QPushButton("Submit")
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
            self.displayResult()

    
    

if __name__ != "__main__":
    # Save a reference to the toolkit onto the mw, preventing garbage collection of PyQT objects
    if mw: mw.ankilevel = AnkiLevel(mw)
else:
    print "This is a plugin for the Anki Spaced Repition learning system and cannot be run directly."
    print "Please download Anki2 from <http://ankisrs.net/>"