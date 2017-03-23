#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:18:00 2017

@author: josuhee
"""

import nltk
from collections import Counter
import re

class NgramTokenizer():
    def __init__(self, file_read):
        self.file_read = file_read
        self.freq_list = [] #Frequency list of selected n grams
        self.fin_comp = [] #A list of Tokens by sentence

    def ngram(self,x):
        return ' '.join(x)

    def tokenize(self):

        sen_list = re.split('[.;!?\n]', self.file_read) # split a sentence by the mark . # not only by '.', ',?!' should be added
        sen_trim = []
        for i in sen_list:
            sen_trim.append(i.strip(' \n0123456789')) # trim those sentences
     
        for x in sen_trim: # for every trimmed sentence
            a = x.split() # split into a list of words # Use regular expression
            if len(a) > 1:
                b = [] # for every x (that is a trimmed sentence), b, a parsed sentence, consists of trimmed words
                for index,word in enumerate(a):
                    word = word.lower()
                    b.append(word.strip(",'?!():-><[]")) # for every word in a, trimmed words go into b
                    if index == 0:
                        b.insert(0,"<s>")
                    elif index == (len(a)-1):
                        b.insert(len(b),"</s>")
                self.fin_comp.append(b)
                            
                            # 5 lines above will be substituted for regular expression which is simpler
               
    def ngram_extract(self,b):                       
                            
        cnt = Counter() #fin_comp가 없을 때 대비해서 try catch써놓기
                            
        if b.text() == "Unigram": # Unigram
            for i in self.fin_comp:
                for k in i:
                    cnt[k] += 1              
        elif b.text() == "Bigram": #Bigram
            for i in self.fin_comp:
                temp02 = list(zip(i,i[1:]))
                temp12 = list(map(self.ngram, temp02))
                for k in temp12:
                    cnt[k] += 1        
        else: #Trigram
            for i in self.fin_comp:
                temp03 = list(zip(i,i[1:],i[2:]))
                temp13 = list(map(self.ngram, temp03))
                for k in temp13:
                    cnt[k] += 1                   

        self.freq_list = cnt.most_common()
    
    def sentence_generator(self):
        pass
                 
#For the probablity, count all the tokens
#    for i in freq_list:
#        allword_num = allword_num + i[-1]
        
        
        
