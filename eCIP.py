# -*- coding: utf-8 -*-
import glob,os,sys
from PIL import Image
from PyQt4 import QtCore,QtGui
from windowUi import Ui_MainWindow
from os.path import join

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.quality_val = 95
        self.Large = 900
        self.Medium = 400
        self.Small = 150
                
        self.ui.lsize.setValue(int(self.Large))
        self.ui.msize.setValue(int(self.Medium))
        self.ui.ssize.setValue(int(self.Small))
        
        self.Target = ""
        self.Prefix = ""
        
        self.ui.Target_LineEdit.setText(self.Target)
        
        self.ui.Target_Button.clicked.connect(self.SelectFolder)
        self.ui.Run_Button.clicked.connect(self.ProcessImages)
        
    def ProcessImages(self, target):
        
        if not os.path.isdir("Processed"):
            os.mkdir("Processed")
        
        self.Prefix = str(self.ui.prefixedit.text())
            
        l = self.ui.lsize.value()
        m = self.ui.msize.value()
        s = self.ui.ssize.value()
        
        if not self.Target == "":
            print "Not Empty"
            for infile in glob.glob("*.jpg"):
                print "+-----------------------------------------------------------------------+"
                print "+ Converting file " + str(infile)
                #file, ext = os.path.splitext(infile)
                im = Image.open(infile)
                #Resize            
                im.resize((l,l), Image.ANTIALIAS).save(join(os.curdir, "Processed", self.Prefix + infile + "_L.jpg"), "JPEG", quality=self.quality_val)
                print "+ Saved " + infile + "_L.jpg"
                im.resize((m,m), Image.ANTIALIAS).save(join(os.curdir, "Processed", self.Prefix + infile + "_M.jpg"), "JPEG", quality=self.quality_val)
                print "+ Saved " + infile + "_M.jpg"
                im.resize((s,s), Image.ANTIALIAS).save(join(os.curdir, "Processed", self.Prefix + infile + "_S.jpg"), "JPEG", quality=self.quality_val) 
                print "+ Saved " + infile + "_S.jpg" 
                print " "
            
            QtGui.QMessageBox.information(self
                    , "Done"
                    , "Everything went better than expected..."
                    , QtGui.QMessageBox.Ok)     
        else:
            print "Empty"
            QtGui.QMessageBox.information(self
                    , "Woops"
                    , "You havn't selected a folder yet!"
                    , QtGui.QMessageBox.Ok)  
            
    def SelectFolder(self):
        fname = QtGui.QFileDialog.getExistingDirectory(self, "Select the folder containing images", 
        "C:/",
        QtGui.QFileDialog.ShowDirsOnly
        | QtGui.QFileDialog.DontResolveSymlinks)
        
        self.ui.Target_LineEdit.setText(fname)
        print fname
        self.Target = fname
        os.chdir(str(fname))

def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
    
    