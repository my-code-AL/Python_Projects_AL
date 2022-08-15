from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

urls = [
    'https://www.youtube.com/c/VICENews',
    'https://www.youtube.com/c/StarWars',
    'https://www.youtube.com/c/wsj',
    'https://www.youtube.com/c/BBCNews',
    'https://www.youtube.com/c/Freecodecamp'
]

def main():
   
    driver = webdriver.Chrome(executable_path='/Users/alaincourtines/Desktop/Projects/chromedriver')
    for url in urls:
        driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
        #content stores all the content of the youtube page encoding it and striping it
        content = driver.page_source.encode('utf-8').strip()
        #make a beautiful soup object that can parse the HTML from the internet
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a', id = 'video-title')
        views = soup.findAll('span',class_='style-scope ytd-grid-video-renderer')
        vid_urls = soup.findAll('a',id='video-title')
        print('Channel: {}'.format(url))
        i = 0
        j=0
        for title in titles:
            print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text, views[i].text, views[i+1].text),vid_urls[j].get('href'))
            i+=2
            j+=1

    


#main()