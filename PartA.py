import string  
import sys
import operator
import re
'''
Method/Function: List<Token> tokenize(TextFilePath)
Write a method/function that reads in a text file and returns a list of the tokens in that file. For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization (so Apple, apple are the same token).
Method:        Map<Token,Count> computeWordFrequencies(List<Token>)
Write another method/function that counts the number of occurrences of each token in the token list.
Method:         void print(Frequencies<Token, Count>)
Finally, write a method that prints out the word frequency counts onto the screen. The print out should be ordered by decreasing frequency. (so, highest frequency words first)
What is it has ,
what kind of intepreter you use?
is the input way good?
'''
# O (N)
def print_map(token : dict) -> None:
   sorted_d = dict( sorted(token.items(), key=operator.itemgetter(1),reverse=True))
   for i in sorted_d:
        print(i,sorted_d[i], sep = '\t', end = "\n")
# O(n) 
def computeWordFrequencies(lst : list ) -> dict:
    d = dict()
    for token in lst:
        if token in d:
            d[token] += 1 
        else:
            d[token] = 1
    return d
# O(c)  not sure about implementation of read or split most linly O(n) if i guess  
#i for a pretty good timing on this function
def tokenize(TextFilePath : "file") -> 'String':
    data = []
    str  = []
    try:
        file = open(TextFilePath,"r")
        str3 = file.read()
        data = re.split('[^a-z0-9]+',str3.lower())
        data = list(filter(None, data))
    except OSError:
        print('Failed to open the file successfully')
    except ValueError:
        print('Failed to read from the file successfully; it is not a text file')
    except UnboundLocalError:
        print("try again.")        
    finally:
        file.close()
    return data
# O(n)
def print_list(lst : 'list') -> None:
    for i in lst:
        if type == 'list':
           print_list(i)
        elif i == "\n":
            print('words')
        else:
            print(i)

try:  
    lst = []
    input = (sys.argv[1])

    lines = tokenize(input)
    #lines = tokenize("test.txt")
    token_map = computeWordFrequencies(lines)
    print_map(token_map)
except UnboundLocalError:
        print("The file does not exist, try again.") 
