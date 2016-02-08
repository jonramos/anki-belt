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

globcomment = "" 
globlevel = 0
globbelt = "" 

class AnkiLevel:
  

     def __init__(self, mw):
       if mw:
         self.menuAction = QAction("Anki Level", mw)
         mw.connect(self.menuAction, SIGNAL("triggered()"), self.displayResult)
         mw.form.menuTools.addSeparator()
         mw.form.menuTools.addAction(self.menuAction)

     def setGloblevel(self, level):
         global globlevel    
         globlevel = level

     def setGlobComment(self, comment):
         global globcomment    
         globcomment = comment

     def setGlobBelt(self, belt):
         global globbelt    
         globbelt = belt

     def generateHTML(self, score):


         self.html  = "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\"/>\n"
         self.html += "<html><head><title>Anki Level</title></head><body class=\"loader\" bgcolor=\"#FFF\">\n"
         self.html += "<p style=\"font-size:150%;\" style=\"font-family:verdana;\" align=\"center\" font=\"Calibri\">\n"
         self.html += "Your score is: %s </br> Level: %s </p> <hr>\n" % (score, globlevel)
         self.html += "<p style=\"font-family:verdana;\" align=\"center\" font=\"Calibri\">\n"
         self.html += "This is your anki belt</p> <p align=\"center\">\n"
         self.html += "<img src=\" %s \" width=\"40\" height=\"20\" /></br></p>\n" % (globbelt)
         self.html += "<p> %s </p>\n" % (globcomment)
         self.html += "<hr><p style=\"font-size:90%;\"> <i>If you have some troubles or sugestions, visit my <a href=\"https://github.com/jonramos/anki-belt\">GitHub page. </a></i></p>\n"
         self.html += "</body></html>\n"

     def getScore(self):
         score =  mw.col.db.scalar("select count() from cards where ivl >= 20")
         int(score)
         if score <= 125:
            self.setGloblevel(1)
            self.setGlobComment("")
            self.setGlobBelt("http://s13.postimg.org/5oabse8cj/class_01.gif")
         elif score >= 126 and score <= 250:
            self.setGloblevel(2)
            self.setGlobComment("Nice! You are now level 2. Try adding more cards to grow up!")
            self.setGlobBelt("http://s27.postimg.org/amayllfun/class_02.gif")
         elif score >= 251 and score <= 400:
            self.setGloblevel(3)
            self.setGlobBelt("http://s16.postimg.org/sn648pboh/class_03.gif")
         elif score >= 401 and score <= 550:
            self.setGloblevel(4)
            self.setGlobBelt("http://s11.postimg.org/qgmeubo1r/class_04.gif")
         elif score >= 551 and score <= 800:
            self.setGloblevel(5)
            self.setGlobBelt("http://s30.postimg.org/sdlw758hp/class_05.gif")
         elif score >= 801 and score <= 1000:
            self.setGloblevel(6)
            self.setGlobBelt("http://s13.postimg.org/xowsvn5c3/class_06.gif")
         elif score >= 1001 and score <= 1250:
            self.setGloblevel(7)
            self.setGlobBelt("http://s27.postimg.org/x7k4a4vwf/class_07.gif")
         elif score >= 1251 and score <= 1500:
            self.setGloblevel(8)
            self.setGlobBelt("http://s17.postimg.org/kwglc3djf/class_08.gif")
         elif score >= 1501 and score <= 1750:
            self.setGloblevel(9)
            self.setGlobBelt("http://s7.postimg.org/ahkt12snb/class_09.gif")
         elif score >= 1751 and score <= 2000:
            self.setGloblevel(10)
            self.setGlobBelt("http://s30.postimg.org/p9yzn1py5/class_10.gif")
         elif score >= 2001 and score <= 2300:
            self.setGloblevel(11)
            self.setGlobBelt("http://s7.postimg.org/a63cobc7b/class_11.gif")
         elif score >= 2301 and score <= 2600:
            self.setGloblevel(12)
            self.setGlobBelt("http://s7.postimg.org/phd5ox9jb/class_12.gif")
         elif score >= 2601 and score <= 3000:
            self.setGloblevel(13)
            self.setGlobBelt("http://s2.postimg.org/l0cmuvqsl/class_13.gif")
         elif score >= 3001 and score <= 3400:
            self.setGloblevel(14)
            self.setGlobBelt("http://s17.postimg.org/70wwb8csb/class_14.gif")
         elif score >= 3401 and score <= 3800:
            self.setGloblevel(15)
            self.setGlobBelt("http://s2.postimg.org/vboznjihx/class_15.gif")
         elif score >= 3801 and score <= 4200:
            self.setGloblevel(16)  
            self.setGlobBelt("http://s2.postimg.org/8x7b7bfqd/class_16.gif")          
         elif score >= 4201 and score <= 5000:
            self.setGloblevel(17)
            self.setGlobComment("Almost there... The final level is near")
            self.setGlobBelt("http://s2.postimg.org/5u6l3y0rp/class_17.gif")
         elif score >= 5001:
            self.setGloblevel(18)
            self.setGlobComment("You are king now. You reached the max level! Congrats!!!!")
            self.setGlobBelt("http://s2.postimg.org/7ojflons5/class_18.gif")
         return score

     #Method called if "Submit" is clicked
     def displayResult(self):
      
       #Get the user score
       score = self.getScore()
      
       self.generateHTML(score);

       self.win = QDialog(mw)
       self.wv = AnkiWebView()
       vl = QVBoxLayout()
       vl.setMargin(0)

       vl.addWidget(self.wv)
       self.wv.stdHtml(self.html)


       self.win.setLayout(vl)
       self.win.resize(300, 250)
       self.win.show()
       return 0

     #This funcion will be used in a future version
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