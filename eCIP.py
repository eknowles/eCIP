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
        self.Small = 124
                
        self.ui.lsize.setValue(int(self.Large))
        self.ui.msize.setValue(int(self.Medium))
        self.ui.ssize.setValue(int(self.Small))
        
        self.FTargetName = "Processed"
        self.Target = ""
        self.Prefix = ""
        
        self.ui.Target_LineEdit.setText(self.Target)
        
        self.ui.Target_Button.clicked.connect(self.SelectFolder)
        self.ui.Run_Button.clicked.connect(self.ProcessImages)
        
    def AddLine(self, detail):
        print str(detail)
        self.ui.plainTextEdit.insertPlainText(detail + "\n")
        
    def ProcessImages(self, target):
        self.AddLine("Started Batch...")
        
        if not os.path.isdir(self.FTargetName):
            self.AddLine("Creating new folder called '" + self.FTargetName + "'")
            os.mkdir(self.FTargetName)
            
        self.Prefix = str(self.ui.prefixedit.text())
            
        l = self.ui.lsize.value()
        m = self.ui.msize.value()
        s = self.ui.ssize.value()
        
        if not self.Target == "":
            print "Not Empty"
            for infile in glob.glob("*.jpg"):
                name, ext = os.path.splitext(infile)
                self.AddLine("Converting file " + str(infile))
                im = Image.open(infile)
                im.resize((l,l), Image.ANTIALIAS).save(join(os.curdir, "Processed", self.Prefix + "_" + name + "_L" + ext), "JPEG", quality=self.quality_val)
                im.resize((m,m), Image.ANTIALIAS).save(join(os.curdir, "Processed", self.Prefix + "_" + name + "_M" + ext), "JPEG", quality=self.quality_val)
                im.resize((s,s), Image.ANTIALIAS).save(join(os.curdir, "Processed", self.Prefix + "_" + name + "_S" + ext), "JPEG", quality=self.quality_val) 
            
            QtGui.QMessageBox.information(self
                    , "Done"
                    , "Everything went better than expected..."
                    , QtGui.QMessageBox.Ok)     
            self.AddLine("Batch Complete.")
            
        else:
            print "Empty"
            QtGui.QMessageBox.information(self
                    , "Woops"
                    , "You havn't selected a folder yet!"
                    , QtGui.QMessageBox.Ok)  
            self.AddLine("Error: Empty Target Folder. Use the Select Folder button at the top to choose a folder to process.")
            
    def SelectFolder(self):
        fname = QtGui.QFileDialog.getExistingDirectory(self, "Select the folder containing images", 
        "C:/",
        QtGui.QFileDialog.ShowDirsOnly
        | QtGui.QFileDialog.DontResolveSymlinks)
        
        self.ui.Target_LineEdit.setText(fname)
        self.Target = fname
        os.chdir(str(fname))

def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
    
    