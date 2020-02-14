'''
you need beautiful soup4 and lxma downloaded in order to run this script


in bash --> apt-get install python3-bs4 
need lmxl installed as well

------------
in window 
https://www.youtube.com/watch?v=aIPqt-OdmS0&t=378s

------------------
for url in soup.find_all('a'):
    print(url.get('href'))

'''
import bs4 as bs
import urllib.request
import string  
import sys
import operator
import re
from urllib.parse import urlparse



def computeWordFrequencies(lst : list ) -> dict:
    d = dict()
    for token in lst:
        if token in d:
            d[token] += 1 
        else:
            d[token] = 1
    return d
def print_map(token : dict,count : int) -> None:
   sorted_d = dict( sorted(token.items(), key=operator.itemgetter(1),reverse=True))
   j = 0 
   for i in sorted_d:
        if j == count:
            break;
        else:
            print(i,sorted_d[i], sep = '\t', end = "\n")
        j += 1

"""
1 . How many unique pages did you find? Uniqueness is established by the URL, 
but discarding the fragment part. So, for example, 
http://www.ics.uci.edu#aaa and http://www.ics.uci.edu#bbb are the same URL
it returns the total of the links in the original list
 """
def total_pages_count(lst : list) -> int:
    # Already removed duplicate from the list
    #lst = list(dict.fromkeys(lst))
    print(len(lst))

'''
2 . What is the longest page in terms of number of words? (HTML markup doesn’t count as words)
function : it will tokenize the content of each page and returns the length of all the text in the page
'''
def tokenize_with(text : "str") -> int:
    data = []
    data = re.split('[^a-z]+',text.lower())
    data = list(filter(None, data))
    return len(data)

'''
3 . What are the 50 most common words in the entire set of pages? (Ignore English stop words,
Submit the list of common words ordered by frequency.
Function: it takes a page content, tokenize remove the stopwords and return a list
'''
def tokenize_without_stopwords(text : "str") -> list:
    data = []
    newList = []
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
                 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

    data = re.split('[^a-z]+',text.lower())
    data = list(filter(None, data))
    for i in data:
        if i not in stop_words:
            newList.append(i)
    #c = set(data) - set(stop_words)   list(c)
    return newList

""" 
4 . How many subdomains did you find in the ics.uci.edu domain? 
Submit the list of subdomains ordered alphabetically and the
number of unique pages detected in each subdomain. The content of this list should be 
lines containing URL, number, for example:
http://vision.ics.uci.edu, 10 (not the actual number here)
"""
def find_sub_domain(list_url : list) -> dict:
    
    d = dict()
    for url in list_url:
        parsed = urlparse(url)
        if parsed.netloc in d:
            d[parsed.netloc] += 1
        else:
            d[parsed.netloc] = 1
    return d


""" 
Main starts from here
"""
try:
    url = []
    d = dict()
    file = open("urlText.txt","r")
    str3 = file.read()
    url = re.split('[\n]+',str3.lower())
    # removing duplicate from the list of urls
    url = list(dict.fromkeys(url))
    # filter for any empty slots
    url = list(filter(None, url))


    # question 4
    d = find_sub_domain(url)
    print("\n---\tproblem 4---\n")
    print_map(d, len(d))

    #-----------------------
    list_url = []
    dic_problem2 = dict()
    dic_problem3 = dict()
    for link in url:
        sause = urllib.request.urlopen(link)
        soup = bs.BeautifulSoup(sause,'lxml')
        # GET THE TITLE OF THE PAGE
        str1 = soup.title.string.strip()
        str2 =""
        # GET ALL THE PARAGRAPHS IN THE HTMLA
        for para in soup.find_all('p'):
            str2 += str(para.text)
        # PUTTING THEM ALL TOGHTHER 
        word = str1+str2
# question 2
        largest_num_page = tokenize_with(word)
        dic_problem2[link] = largest_num_page
# question 3
        list_url.extend(tokenize_without_stopwords(word))
        dic_problem3 = computeWordFrequencies(list_url)



    # OUT OF LOOP
    print("\n---\tproblem 1---\n")
    total_pages_count(url)  # QUESTION 1 : TOTAL COUNT
    print("\n---\tproblem 2---\n")
    
    print_map(dic_problem2, 1)  #print question 2
    print("\n---\tproblem 3---\n")
    
    print_map(dic_problem3, 50) # question 3
    
    

except OSError:
    print('Failed to open the file successfully')
except ValueError:
    print('Failed to read from the file successfully; it is not a text file')
except UnboundLocalError:
    print("try again.")        
finally:
    file.close()










""" sause = urllib.request.urlopen("https://wics.ics.uci.edu/ics-banquet/")
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
    print(i) """


'''
#x = soup.get_text()

token_map = computeWordFrequencies(lst)
print_map(token_map)
'''

