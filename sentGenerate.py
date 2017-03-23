from tkinter import *
from collections import Counter
import re

# 1) This N-gram Viewer enables to set value N.(N cannot exceed 3)
# 2) According to the value, N grams are presented 
# 3) If you click any pair of N gram (or any unique word in case of unigram), its approximated probablity will show up 


# 4) is the most advanced technology in this program. Its algorithm employs Simple(Unsmoothed) N-gram Model.
# Since this is my first trial for the N-gram Model, this algorithm can be revised later on.
# I hope to see Smoothed N gram Model in this program...

# This program ONLY accept files that are written in txt.(plain text)
# All headers and footers must be removed 
# Opening a Corpus data that is too big can be overloading...


# This program will get better if you get rid of all the global variables and make classes for the whole app.
# ,

root = Tk()
root.title("N-gram Viewer for Text files")
root.geometry('900x500+200+100')

######################################## Open and Save Files
#ONLY one file at one time can be processed
#the saved file will be written in the following format ,..

file_read = '' 
def openfiles():
    global file_read 
    open_name= filedialog.askopenfilename(defaultextension = '.txt')
    f = open(open_name, encoding='UTF8')
    file_read = f.read() #불러온 파일을 file_read 전역변수에 남긴다 
    f.close()
    filepath_spt = open_name.split('/')
    fileShow_label.config(text=filepath_spt[-1]) #fileShow_label에 부른 파일 이름이 뜨게 만들어야함 
    #file 을 불러서 ngram을 만들기 위한 준비를 해야함

# proabable sentences 들이 저장되게 만들어야 한다
def savefile():
    name= filedialog.asksaveasfilename(defaultextension='.txt',
        filetypes = (("파이썬파일", "*.py"),
                     ("텍스트파일", "*.txt"),
                     ("모든파일", "*.*"))) 
    open(name,'w').write(ngram_listbox.get(0, END)) #현재는 ngram listbox가 저장됨



menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=openfiles)
filemenu.add_command(label="저장", command=savefile) #여기에 추가해서 probable senteces 도 저장하게 만들어볼까
filemenu.add_separator()
filemenu.add_command(label="종료", command=root.destroy)
filemenu.add_separator()

"""
N gram pairs and Frequency
(N gram pair) \t (Freq)
...
# and most probable sentences will be added in the end
Most Probable sentences
(sentence1) \n
(sentence2) \n
...
"""

########################################### Setting labels, boxes etc ##################################################
## grid method will be used for the location for the buttons and labels
#그리드 셀크기를 알아야할거같은

########################################### 1st Column

## Set the label "File Name"
file_label = Label(root, text="File Name", width=10)
file_label.grid(row = 0, column = 0,  padx = 60, pady = 20)

## Set a Show-up label for the file (after opening a file, the file name will pop up)
fileShow_label = Label(root, text="FileName", fg = '#000fff000' , width=20)
fileShow_label.grid(row = 1, column = 0,  padx = 60, pady = 20)

## Set the label "Choose N for N gram"
chooseN_label = Label(root, text="Choose N for N gram", width=15)
chooseN_label.grid(row = 2, column = 0, padx = 60, pady = 20)

## Set the radiobutton for N

MODES = [("Unigram", 1), ("Bigram", 2), ("Trigram", 3)]
v = IntVar() 
v.set(1) # initialize

r = 0
for text, mode in MODES:
    rad = Radiobutton(root, text=text, indicatoron = 0, width = 20, variable=v, value=mode) 
    rad.grid(row = 3+r , column = 0 , padx = 60, pady = 10)
    r += 1

# Set function that extracts Ngram from the selected file
# set freq_list


def ngram(x):
    return ' '.join(x)

def extract_ngram():
    global freq_list
    freq_list = []

    sen_list = re.split('[.;!?\n]',file_read) # split a sentence by the mark . # not only by '.', ',?!' should be added
    sen_trim = []
    for i in sen_list:
        sen_trim.append(i.strip(' \n0123456789')) # trim those sentences
        
    fin_comp = [] #final components. an element is a list which consists of trimmed words in one sentence 
    
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
            fin_comp.append(b)
            
        # 5 lines above will be substituted for regular expression which is simpler

    cnt = Counter()

    if (v.get()) == 1: # Unigram
        for i in fin_comp:
            for k in i:
                cnt[k] += 1              
    elif (v.get()) == 2: #Bigram
        for i in fin_comp:
            temp02 = list(zip(i,i[1:]))
            temp12 = list(map(ngram, temp02))
            for k in temp12:
                cnt[k] += 1        
    else: #Trigram
        for i in fin_comp:
            temp03 = list(zip(i,i[1:],i[2:]))
            temp13 = list(map(ngram, temp03))
            for k in temp13:
                cnt[k] += 1                   

    freq_list = cnt.most_common()
    for i in freq_list:
        ngram_listbox.insert(END,i[0])
                 
#For the probablity, count all the tokens
#    for i in freq_list:
#        allword_num = allword_num + i[-1]


## Set Run Button

run_button = Button(root, text = "Run", width = 5, height = 2, command = extract_ngram)
run_button.grid(row = 6, column = 0, padx = 60, pady = 40)


########################################### 2nd Column

## Set the label "N grams"
nGrams_label = Label(root, text="N grams", width=15)
nGrams_label.grid(row = 0, column = 1, padx =60, pady = 20)

## Set a list box for N gram pairs

# Add a vertical scroll bar to the list box

"""
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
"""

#scroll for ngram textbox
ngram_yScroll = Scrollbar(root, orient=VERTICAL)
ngram_yScroll.grid(row = 1, column = 2, rowspan = 4, pady = 10,  sticky = SW+NW)

#function that calculates the probability for the selected Ngram
def prob_cal(event):
    widget = event.widget
    sel = widget.curselection()
    word = widget.get(sel[0])
    word_num = 0
    allword_num = 0
    for i in freq_list:
        allword_num = allword_num + i[-1]
    for i in freq_list: #prob_cal 에서 확률계산하지 말고 아예 extract ngram에서 계
        if i[0] == word:
            word_num = i[-1]  
    prob = word_num / allword_num
    prob = round(prob,10)
    probShow_label.config(text = str(prob))
    
#ngram text box
ngram_listbox = Listbox(root, width = 15, height = 15, yscrollcommand = ngram_yScroll.set)
ngram_listbox.bind('<<ListboxSelect>>',prob_cal)
ngram_listbox.grid(row = 1, column = 1, rowspan = 4, pady = 10,  sticky = N+S+E+W)

ngram_yScroll['command'] = ngram_listbox.yview

## Set a label for probability
prob_label = Label(root, text="Probability", width=15)
prob_label.grid(row = 5, column = 1, padx =60)

## Set a Show-up label for probability
probShow_label = Label(root, text="Prob", fg = '#000fff000' , width=15)
probShow_label.grid(row = 6, column = 1,  padx = 60 )


########################################### 3rd Column



## Set a label for Most probable sentences

sent_label = Label(root, text="Most Probable Sentences", width= 20)
sent_label.grid(row = 0, column = 3, padx = 60 )

## Set a listbox for Most probable sentences

sent_yScroll = Scrollbar(root, orient=VERTICAL)
sent_yScroll.grid(row = 1, column = 4, rowspan = 6, pady = 20,  sticky = SW+NW)

sent_listbox = Listbox(root, width = 15, height = 20, yscrollcommand = sent_yScroll.set)
sent_listbox.grid(row = 1, column = 3, rowspan = 6, pady = 10,  sticky= N+S+E+W)


mainloop()
