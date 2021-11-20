import requests
from bs4 import BeautifulSoup
import lxml
#import sys

url="https://realpython.github.io/fake-jobs/"
page=requests.get(url)

#print(page.text)
#sys.stdout.write(page.text)
soup=BeautifulSoup(page.content,"lxml")
results=soup.find(id="ResultsContainer")
print(results)