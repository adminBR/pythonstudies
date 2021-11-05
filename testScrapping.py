#pip install beautifulsoup4
#pip install lxml
from bs4 import BeautifulSoup

htmlFile = None
def main() :
    with open('home.html', 'r') as content:
        htmlFile = content.read()
        soup = BeautifulSoup(htmlFile,'lxml')
        cards = soup.find_all('div',class_='card') #find all tags of the type "div" with the class name card. Obs: since python already have a object named class, we use class_

        for course in cards :
            course_name = course.h5.text
            course_price = course.a.text.split()[-1] # -1 represents the last position of the list, get the whole line and split off the last, since the value we want is the last word
            print(f'The course {course_name} costs {course_price}')
    
def learn1() :
    with open('home.html', 'r') as content:
            htmlFile = content.read()
            #print(htmlFile)
            soup = BeautifulSoup(htmlFile,'lxml')
            #print(soup.prettify())
            tags = soup.find('h5') #only first
            #print(tags)
            tags = soup.find_all('h5')
            print(tags[1])

if __name__ == '__main__' : main()