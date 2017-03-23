#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 23:59:54 2017

@author: josuhee
"""

## Written by Suhee Jo #################################################################################
# Randome Sentence Generator with N grams
# Python 2.7
# 
# -> Tokenization with regular expression
# -> Move to Python 2.7 
# -> Using PyQt instead of tkinter (0)
# -> Sentence generation with nltk 
#######################################################################################################


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from collections import Counter
import re
import nltk
from nGramTokenizer import NgramTokenizer

# import nGramTokenizer

##############################################################

class SentenceGenerator(QtWidgets.QMainWindow): #Class for your GUI. In this case, SentenceGenerator inherited class from QMainWindow.
    def __init__(self): #Initialization of SentenceGenerator
        super(SentenceGenerator,self).__init__() #Initialization of QMainWindow
        self.setupUi() #Set up layout & signals and slots
        #self.tokenizer = nGramTokenizer()

    def setupUi(self):
        
        ################## Main Window
        
        self.setGeometry(200, 100, 900, 500)
        self.setObjectName("SentenceGenerator")
        
        
        ################## Menu Bar
        
        #New file action
                   
        open_file = QtWidgets.QAction("File Open", self)
        open_file.triggered.connect(self.file_open)
        open_file.setStatusTip('Opening File')
        '''
        file.addAction("New")
        file.triggered.connect(self.func_name)
        '''
        
        #Save file action

        save_file = QtWidgets.QAction("File Save", self)
        save_file.triggered.connect(self.file_save)
        save_file.setStatusTip('Saving File')
        
        #Menu bar
        
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction(open_file)
        file.addAction(save_file)
        
        ################## File status
        #File Name
        fileName_label = QtWidgets.QLabel("File Name", self)
        fileName_label.move(80, 30)
        fileName_label.resize(71, 20)
        
        #File Name (Green)
        self.fileNameG_label = QtWidgets.QLabel("File Name", self) #Other function (not setupUi) refers this label. so self.objectname
        self.fileNameG_label.move(80,80) #Sinch there is QtCore, fileNameG_label.setGeometry(QtCore.QRect(520, 120, 91, 41))
        self.fileNameG_label.resize(60, 16)
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.green)
        self.fileNameG_label.setPalette(palette)
        
        
        ################## Choose N for Ngrams
        #N for N grams
        n_label = QtWidgets.QLabel("N for N grams", self)
        n_label.move(80, 130)
        n_label.resize(121, 16)
        
        #Group box for radiobutton
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(50, 170, 161, 191)) 
        self.groupBox.setTitle("")
        
        #unigram
        self.uni_radioButton = QtWidgets.QRadioButton("Unigram" , self.groupBox)
        self.uni_radioButton.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.uni_radioButton.toggled.connect(lambda:NgramTokenizer.ngram_extract(self.uni_radioButton)) # connection to the n gram tokenizer 
        #bigram
        self.bi_radioButton = QtWidgets.QRadioButton("Bigram" , self.groupBox)
        self.bi_radioButton.setGeometry(QtCore.QRect(10, 80, 100, 20))    
        self.bi_radioButton.toggled.connect(lambda:NgramTokenizer.ngram_extract(self.bi_radioButton))
        #trigram
        self.tri_radioButton = QtWidgets.QRadioButton("Trigram" , self.groupBox)
        self.tri_radioButton.setGeometry(QtCore.QRect(10, 140, 100, 20))
        self.tri_radioButton.toggled.connect(lambda:NgramTokenizer.ngram_extract(self.tri_radioButton))
        ################## Run Button
        #Run button        
        run_button = QtWidgets.QPushButton("Run",self)
        run_button.move(60,390)
        run_button.resize(113,32)
        run_button.clicked.connect(self.btn_clicked)
	  
        
        ################## N Grams List
        #N grams
        nGrams_label = QtWidgets.QLabel("N grams", self)
        nGrams_label.setGeometry(QtCore.QRect(400, 30, 71, 20))
        
        #N grams listbox
        self.nGrams_listWidget = QtWidgets.QListWidget(self)
        self.nGrams_listWidget.setGeometry(QtCore.QRect(320, 100, 231, 231))
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.nGrams_listWidget.addScrollBarWidget(self.scrollArea, QtCore.Qt.AlignRight)

        ################## Probability status        
        #Probability
        prob_label = QtWidgets.QLabel("Probability", self)
        prob_label.setGeometry(QtCore.QRect(400, 360, 81, 16))      
        
        
        #Prob(Green)
        self.probG_label = QtWidgets.QLabel("Prob", self)
        self.probG_label.setGeometry(QtCore.QRect(400, 400, 91, 16))   
        self.probG_label.setPalette(palette)
        
        
        ################## Sentences List
        #Sentences
        sent_label = QtWidgets.QLabel("Sentences", self)
        sent_label.setGeometry(QtCore.QRect(700, 30, 81, 16))        
        
        #Sentences listbox
        self.sent_listWidget = QtWidgets.QListWidget(self)
        self.sent_listWidget.setGeometry(QtCore.QRect(630, 100, 231, 321))
        self.scrollArea_2 = QtWidgets.QScrollArea(self)
        self.sent_listWidget.addScrollBarWidget(self.scrollArea_2, QtCore.Qt.AlignRight)
        
        
        ################## Open File
    def file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "/Users", "Text files (*.txt)") 
        name = unicode(name[0])
        file = open(name, 'r')
        with file: # with statement guarantees the file is closed
            text = file.read()
            self.tokenizer = NgramTokenizer(text) # Class instanciation
                
        ################## Save File
    def file_save(self):
        pass
        ################## Run Button Clicked
    
    def button_clicked(self): # add ngrams to the n gramslist 
        
        
if __name__ == "__main__": # Checking if the script is run directly
    app = QtWidgets.QApplication(sys.argv) #sys.argv contains arguments on the command line
    mywindow = SentenceGenerator()
    mywindow.show()
    app.exec_() 

