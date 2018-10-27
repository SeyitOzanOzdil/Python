# -*- coding: utf-8 -*-
import os
import re
from textblob import Word

vocabulary = []
sportClass = {}
businessClass = {}
politicsClass = {}
testClass = []
stopWords = ["a", "about", "above", "above", "across", "after", "afterwards", 
             "again", "against", "all", "almost", "alone", "along", "already", 
             "also","although","always","am","among", "amongst", "amoungst", 
             "amount",  "an", "and", "another", "any","anyhow","anyone",
             "anything","anyway", "anywhere", "are", "around", "as",  "at", 
             "back","be","became", "because","become","becomes", "becoming", 
             "been", "before", "beforehand", "behind", "being", "below", 
             "beside", "besides", "between", "beyond", "bill", "both", 
             "bottom","but", "by", "call", "can", "cannot", "cant", "co", 
             "con", "could", "couldnt", "cry", "de", "describe", "detail", 
             "do", "done", "down", "due", "during", "each", "eg", "eight", 
             "either", "eleven","else", "elsewhere", "empty", "enough", "etc",
             "even", "ever", "every", "everyone", "everything", "everywhere", 
             "except", "few", "fifteen", "fify", "fill", "find", "fire", 
             "first", "five", "for", "former", "formerly", "forty", "found", 
             "four", "from", "front", "full", "further", "get", "give", "go", 
             "had", "has", "hasnt", "have", "he", "hence", "her", "here", 
             "hereafter", "hereby", "herein", "hereupon", "hers", "herself", 
             "him", "himself", "his", "how", "however", "hundred", "i","i’d", 
             "i’ll", "i’m" ,"i’ve", "ie","if", "in", "inc", "indeed", 
             "interest", "into", "is", "it", "its", 
             "itself", "keep", "last", "latter", "latterly", "least", "less", 
             "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill",
             "mine", "more", "moreover", "most", "mostly", "move", "much", 
             "must", "my", "myself", "name", "namely", "neither", "never", 
             "nevertheless", "next", "nine", "no", "nobody", "none", 
             "noone", "nor", "not", "nothing", "now", "nowhere", "of", 
             "off", "often", "on", "once", "one", "only", "onto", "or", 
             "other", "others", "otherwise", "our", "ours", "ourselves", 
             "out", "over", "own","part", "per", "perhaps", "please", 
             "put", "rather", "re", "same", "see", "seem", "seemed", 
             "seeming", "seems", "serious", "several", "she", "should", "show",
             "side", "since", "sincere", "six", "sixty", "so", "some", 
             "somehow", "someone", "something", "sometime", "sometimes", 
             "somewhere", "still", "such", "system", "take", "ten", "than", 
             "that", "the", "their", "them", "themselves", "then", "thence", 
             "there", "thereafter", "thereby", "therefore", "therein", 
             "thereupon", "these", "they", "thickv", "thin", "third", "this", 
             "those", "though", "three", "through", "throughout", "thru", 
             "thus", "to", "together", "too", "top", "toward", "towards", 
             "twelve", "twenty", "two", "un", "under", "until", "up", "upon", 
             "us", "very", "via", "was", "we", "well", "were", "what", 
             "whatever", "when", "whence", "whenever", "where", "whereafter", 
             "whereas", "whereby", "wherein", "whereupon", "wherever", 
             "whether", "which", "while", "whither", "who", "whoever", "whole",
             "whom", "whose", "why", "will", "with", "within", "without", 
             "would", "yet", "you", "your", "yours", "yourself", "yourselves"]

def cleanString(string):
    string = re.sub(r"\'s", "", string)
    string = re.sub(r"\'ve", "", string)
    string = re.sub(r"n\'t", "", string)
    string = re.sub(r"\'re", "", string)
    string = re.sub(r"\'d", "", string)
    string = re.sub(r"\'ll", "", string)
    string = re.sub(r",", "", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", "", string)
    string = re.sub(r"\)", "", string)
    string = re.sub(r"\?", "", string)
    string = re.sub(r"'", "", string)
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"[0-9]\w+|[0-9]","", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()

def cleanStopWords(data):
    for i in range(len(data)):
        if(data[i] in stopWords):
            data[i] = ""
    data = filter(None, data)
    return data

def preProcessData(data):
    for i in range(len(data)):
        data[i] = cleanString(data[i])
        data[i] = Word(data[i]).lemmatize().encode('ascii')
    
    data = " ".join(data).split(" ")
    data = cleanStopWords(data)
    return data

def fillData(category, data):
    if(category == "test"):
        del testClass[:]
        for word in data:
            if(word in vocabulary):
                testClass.append(word)
        return
    
    if(category == "sport"):
        for word in data:
            if(word in sportClass.keys()):
                sportClass[word] += 1
            else:
                sportClass[word] = 1
                
    elif(category == "business"):
        for word in data:
            if(word in businessClass.keys()):
                businessClass[word] += 1
            else:
                businessClass[word] = 1
                
    elif(category == "politics"):
        for word in data:
            if(word in politicsClass.keys()):
                politicsClass[word] += 1
            else:
                politicsClass[word] = 1
    
    for word in data:
        if(word not in vocabulary):
            vocabulary.append(word)
        
def naiveBayes(fileName):
    
    nVocabulary = len(vocabulary)
    nSport = len(sportClass.keys())
    nBusiness = len(businessClass.keys())
    nPolitics = len(politicsClass.keys())
    
    pSport = 1.0/3
    pBusiness = 1.0/3
    pPolitic = 1.0/3
    
    for word in testClass:
        if(word in sportClass.keys()):
            pSport = (pSport*((sportClass[word] + 1.0 )/(nSport+nVocabulary)))*10**4
        else:
            pSport = (pSport*( 1.0 / (nSport+nVocabulary)))*10**4
            
        if(word in businessClass.keys()):
            pBusiness = (pBusiness * ((businessClass[word] + 1.0)/(nBusiness+nVocabulary)))*10**4
        else:
            pBusiness = (pBusiness * (1.0 / (nBusiness+nVocabulary)))*10**4
            
        if(word in politicsClass.keys()):
           pPolitic = (pPolitic * ((politicsClass[word] + 1.0)/(nPolitics+nVocabulary)))*10**4
        else:
            pPolitic = (pPolitic * (1.0 / (nPolitics+nVocabulary)))*10**4
    
    classType = "sport"
    if(pSport < pBusiness):
        classType = "business"
    if((classType == "sport" and pPolitic > pSport) or (classType == "business" and pPolitic > pBusiness)):
        classType = "politic"
    print pSport, pBusiness, pPolitic
    print (fileName, classType)
    print "/n"
    return
        
def readFile(category):
        path = "datasets/" + category + "/"
        files = os.listdir(path)    
        datasets = [path + file for file in files]
        data = []
        for dataset in datasets:
            f= open(dataset)
            data = f.read().split(" ")
            data = preProcessData(data)
            fillData(category, data)
            if(category == "test"):
                naiveBayes(dataset)

def main():
    categories = ["sport", "business", "politics", "test"]
    for category in categories:
        readFile(category)
    
main()


