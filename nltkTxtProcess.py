
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

import nltk
raw = "Hi happy hippy suhee hi"
tokens = nltk.word_tokenize(raw)
nltk.download()


        
        
text = nltk.corpus.genesis.words('english-kjv.txt') 
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)


text = "Hi happy hippy suhee hi Hi happy hippy suhee hi Hi happy hippy suhee hi Hi happy hippy suhee hi"
tigrams = nltk.trigrams(text)
cfd = nltk.ConditionalFreqDist(tigrams)


########### text generationxt.generate() ######################################

##1
sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven',
... 'and', 'the', 'earth', '.']

def generate_model(cfdist, word, num=15): ### 이부분 함수를 내가 만들어야할듯
    for i in range(num):
        print word,
        word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt') 
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

print cfd['living']
generate_model(cfd, 'living')

##2
import nltk 
text = nltk.Text(nltk.corpus.brown.words()) # Get text from brown 
text.generate()

##############################################

cfdist = ConditionalFreqDist((len(word), word) for word in word_tokenize(sent))

grams = list(nltk.trigrams(tokens))
cfdist = nltk.ConditionalFreqDist((gram[:-1] , gram[-1]) for gram in grams)



## generate model for trigram


def generate_model(cfdist, word_tuple, num=15): ### 이부분 함수를 내가 만들어야할듯
    for i in range(num):
        print ' '.join(word_tuple),
        word = cfdist[wordtuple].max()
        
        
################################# file read and sent split

f = open('/Users/josuhee/Documents/NgramViewer_text/pg100.text', encoding='UTF8')

    