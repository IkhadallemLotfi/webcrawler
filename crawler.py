import requests
import re
import redis

r = requests.get('http://journalseek.net/comp.htm')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser')

results = soup.find_all('a', class_ ="boldlink")

k=0
i=0
while i< len(results) : # liste des lien vers les catégories des articles 
#while i < 1 :
    r = requests.get(results[i].get('href')) 

    soup = BeautifulSoup(r.text,'html.parser') # on récupère le contenu de la page qui contient les articles
    resultsArticles = soup.find_all('a', class_ ="link" ) # on recheche le lien vers l'article
    
    k=0
    while k < len(resultsArticles) :
    #while k < 6 :
        print('\n \n')
        r2 = requests.get(resultsArticles[k].get('href'))
        soup2 = BeautifulSoup(r2.text,'html.parser')

        titre = soup2.find('p',class_="heading2")

        nextPart = soup2.find_all('dd')

        InfoLinks = nextPart[0].find_all('a',class_="link")

        categoryLinks = nextPart[1].find_all('a',class_="link")
        
        sousTitre = titre.next_sibling.next_sibling

        if len(sousTitre.contents) > 1 :
            auteur = sousTitre.contents[0].next_sibling
            ISSN = auteur.next_sibling
            
            #print(auteur.text)
        else :
            ISSN = sousTitre.contents[0]

        
        if len(ISSN) > 30 :
            ISSN_printed = ISSN.string[20:29]
            ISSN_electronic = ISSN.string[50:-1]
            print(ISSN_electronic)
            print(ISSN_printed)
        else :
            ISSN = ISSN.string[10:-1]
            print(ISSN)


        description = sousTitre.next_sibling.next_sibling
        
        j=0
        while j < len(InfoLinks) :
            #print(InfoLinks[j].get('href'))
            j=j+1

        j=0
        while j < len(categoryLinks) :
            #print(categoryLinks[j].get('href'))
            j=j+1

        #print(titre.text.encode("utf-8"))
        
        
        #print(description.text)
        k=k+1
    print(len(resultsArticles))

    i=i+1