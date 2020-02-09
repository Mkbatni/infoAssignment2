'''
you need beautiful soup4 and lxma downloaded in order to run this script


in bash --> apt-get install python3-bs4 
for url in soup.find_all('a'):
    print(url.get('href'))

'''
import bs4 as bs
import urllib.request
import string  
import sys
import operator
import re



def computeWordFrequencies(lst : list ) -> dict:
    d = dict()
    for token in lst:
        if token in d:
            d[token] += 1 
        else:
            d[token] = 1
    return d

def tokenize_with_stopwords(text : "str") -> list:
    data = []
    data = re.split('[^a-z]+',text.lower())
    data = list(filter(None, data))
    
    return data


def tokenize_without_stopwords(text : "str") -> int:
    data = []
    newList = []
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
                 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
   
    
            
    data = re.split('[^a-z]+',text.lower())
    data = list(filter(None, data))
    
    c = set(data) & set(stop_words)
    return len(data) - len(c)
    
def print_map(token : dict) -> None:
   sorted_d = dict( sorted(token.items(), key=operator.itemgetter(1),reverse=False))
   j = 0 
   for i in sorted_d:
        if j == 50:
            break;
        else:
            print(i,sorted_d[i], sep = '\t', end = "\n")
        j += 1




sause = urllib.request.urlopen("https://wics.ics.uci.edu/ics-banquet/")
soup = bs.BeautifulSoup(sause,'lxml')
str1 = soup.title.string.strip()
str2 =""
for para in soup.find_all('p'):
    str2 += str(para.text)
word = str1+str2
# ---- -------- ------- ----- ------

sause2 = urllib.request.urlopen("http://www.informatics.uci.edu/undergrad/bs-informatics")
soup2 = bs.BeautifulSoup(sause2,'lxml')

st1 = soup2.title.string.strip()
st2 =""
for para in soup2.find_all('p'):
    st2 += str(para.text)
word2 = st1+st2




# problem 2

largest_num_page = tokenize_without_stopwords(word)
print("largest text in a page is",largest_num_page)


#problem 3

lst1 = []
lst2 = []
lst1 = tokenize_with_stopwords(word)
lst2 = tokenize_with_stopwords(word2)
c = set(lst1) & set(lst2)
for i in c:
    print(i)
'''
#x = soup.get_text()

token_map = computeWordFrequencies(lst)
print_map(token_map)
'''
