#pip installs : beautifulsoup4; requests; mechanize
from bs4 import BeautifulSoup
import requests

import http.cookiejar as cookielib
import mechanize

browserInstance = None
cookies = None
def main():
    print('Sagres Requester: Get your subjects without opening any website')
    login = input('Type your username:')
    password = input('Type your password:')
    htmlPage = getHtml('http://sagres.uesb.br/PortalSagres/Modules/Diario/Aluno/Default.aspx',login,password)
    #htmlPage = loadHtmlFile()

    soup = BeautifulSoup(htmlPage,'lxml')
    subjectsCollumn = soup.find('div',class_='coluna-metade coluna-1')
    subjectList = soup.find_all('section',class_='webpart-aluno-item')
    for subject in subjectList :
        print(subject.find('a').text)
    
    #print(soup.prettify())




def getHtml(link, user, password) :
    try :
        cookies = cookielib.CookieJar()
        browserInstance = mechanize.Browser()
        browserInstance.set_cookiejar(cookies)

        browserInstance.open(link)

        browserInstance.select_form(nr=0)
        browserInstance.form['ctl00$PageContent$LoginPanel$UserName'] = user
        browserInstance.form['ctl00$PageContent$LoginPanel$Password'] = password
        browserInstance.submit()

        page = browserInstance.response().read()
        with open('sagres.html','w') as content:
            soup = BeautifulSoup(page,'lxml')
            content.writelines(soup.prettify())

        return page    
    except :
        print(f'Invalid request! Error:{browserInstance.response()}')

def loadHtmlFile() :
    with open('sagres.html','r') as content:
        return content.read()






if __name__ == '__main__' : main()