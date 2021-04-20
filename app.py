from requests import get
import time,chime
from bs4 import BeautifulSoup
url = "https://www.binance.com/en/support/announcement/c-48"
# url = "https://www.binance.com/en/support/announcement/c-49?navId=49"

print("info : processing")
timeint = int(input("Enter time interval (in sec) : "))
def getLatestNews(url):    
    newList = []
    text = get(url).text
    html = BeautifulSoup(text,'html.parser')
    a = html.find_all("a",{'class':'css-1ej4hfo'})
    for ann in a:
        newList.append(ann.text)
    return newList 
announcements = getLatestNews(url)
filename = "lastannouncements.txt"

def writeToFile(filename,announcements):
    f=open(filename,'w+')
    for ele in announcements:
        f.write(ele+'\n')
    print("info : wrote to file")

# writeToFile(filename,announcements)

while True:
    # d = input("wait ? y/n")
    # if(d == "y"):
    #     time.sleep(timeint)
    # else:
    #     pass
    announcements = getLatestNews(url)
    f= open(filename,"r+")
    li = f.read()
    li = li.split('\n')[:-1]
    # print(li)
    li_set = set(li)
    announcements_set = set(announcements)
    if(len(li) == len(announcements)):
      
        if(li == announcements):
            print("info : there is no new post")
        else:
            print("info : there is a new post in announcements\a")
            for i in range(5):
                chime.success()   
            #     print("\a")
                time.sleep(1)     
            new_posts = announcements_set.difference(li_set)
            new_posts =list(new_posts)
            print("\n======================")
            print("These are new posts: ")
            for new_post in new_posts:
                print( "=> " + new_post) 
            print("======================\n")
            writeToFile(filename,announcements)
    else:
        print("info : both have different lenghts")
        print("info : there is a new post in announcements\a")
        for i in range(5):
            chime.success()   
        #     print("\a")
            time.sleep(1)     
        new_posts = announcements_set.difference(li_set)
        new_posts = list(new_posts)
        print("\n======================")
        print("These are new posts: ")
        for new_post in new_posts:
            print( "=> " + new_post) 
        print("======================\n")
        writeToFile(filename,announcements)
    
    time.sleep(timeint)