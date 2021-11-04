#requires notify2
import asyncio
import datetime
import time
import requests
from plyer import notification
import json

#notiTitle = 'titulo'
#notiBody = 'corpo'
#notiIcon = ''

def main () :
    print('Notification Creator!')
    notiTitle = input('Please type a title for your notification:')
    print('Choose a input option for the body of your notification.')
    inputChoice = inputWithNumericCheck('Type 1 to write a text message or 2 for request data from a url : ',[1,2])
    if(inputChoice == 1):
        notiBody = input('You chose to write a text message, type the message you want for your notification: ')
    if(inputChoice == 2):
        notiBody = dataRequest('You chose to get the data from a url, type the url containing the data: ')
    notiIcon = input('Type the path to and icon image or press enter to leave empty:')
    
    #teststr = ''
    #with open('CovidData.txt') as f:
    #    teststr = f.read()
    #with open('CovidData.txt', 'w') as f:
    #    f.write(covidDataRequest.text)
    notificationCreator(notiTitle,notiBody,notiIcon)


def inputWithNumericCheck(printText,numbers):
    while True :
        inputChoice = input(printText)
        if(inputChoice.isnumeric()):
            inputChoice = int(inputChoice)
            if(numbers == 0) :
                return inputChoice
            else:
                for idx,val in enumerate(numbers):
                    if(inputChoice == val) :
                        return inputChoice
                print('invalid number! try again.')
        else:
            print('invalid option! try again.')


def dataRequest(printText) :
    #https://httpbin.org/bytes/10
    while True:
        urltext = input(printText)
        try:
            webRequest = requests.get(urltext)
            print('Request Finished')
            if(len(webRequest.text) < 254):
                return webRequest.text
            else:
                print("Response over 254 characters!")
        except:
            inputChoice = input('Invalid Request, want to try another link? Y/N')
            if(inputChoice.lower() != 'y'):
                exit()
            

def notificationCreator(notiTitle,notiBody,notiIcon) :
    #if(covidDataRequest != None) :
    #    data = covidDataRequest.json()['Success']

    #jsonData = json.loads(datastr)['Success']

    #notification.notify(
    #    title = notiTitle,
    #    message = notiBody,
    #    app_icon = '',
    #    timeout = notiDuration
    #)
    notification.notify(
        title = ' '+notiTitle,
        message = ' '+notiBody,
        app_icon = ''+notiIcon,
        timeout = 8
    )
    print('Notification created!')





if __name__ == '__main__' : main()