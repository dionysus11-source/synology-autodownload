from selenium import webdriver
import requests
import copy
from selenium.webdriver.common.by import By

class TorrentDownloader:
    google_search_url = "https://www.google.com/search?q=%ED%86%A0%EB%A0%8C%ED%8A%B8%EC%94%A8"
    
    def __init__(self,keyword, category):
        self.__keyword = keyword
        self.__category= category
        arg = ["--disable-blink-features=AutomationControlled"," --headless",'--no-sandbox',
            "--single-process", "--disable-dev-shm-usage", "--disable-gpu", "--disable-infobars"]
        options = self.__add_argument(arg)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        try:
            self.__driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=options)
            #self.__driver = webdriver.Chrome(executable_path='./chromedriver',options=options)
            self.__driver.set_page_load_timeout(60)
        except:
            print('exception occured', flush=True)
        	
    
    def __del__(self):
        try:
            self.__driver.quit()
        except:
            print('exception occured', flush=True)

    def __add_argument(self,arg):
        options = webdriver.ChromeOptions()
        for item in arg:
            options.add_argument(item)
        return options
                
    @property
    def keyword(self):
        return copy.deepcopy(self.__keyword)
    
    @property
    def category(self):
        return copy.deepcopy(self.__category)

    def __search_keyword(self, url):
        self.__driver.get(url)
        self.__driver.implicitly_wait(time_to_wait=5)
        latest_link = self.__driver.find_elements_by_class_name('tit > a')
        for link in latest_link:
            if self.__keyword in link.text:
                print(link.text, flush=True)
                return link

    def __save_file(self, link):
        self.__driver.get(link.get_attribute('href'))
        self.__driver.implicitly_wait(time_to_wait=5)
        file_download_link = self.__driver.find_element_by_class_name('bbs_btn1').get_attribute('href')
        res = requests.get(file_download_link)
        foldername = '/app/download/'
        filename = '{}.torrent'.format(self.keyword)
        with open(foldername+filename, 'wb') as f:
            f.write(res.content)
        print('download success', flush=True)
    @property
    def __torrent_site_url(self):
        self.__driver.get(TorrentDownloader.google_search_url)
        self.__driver.implicitly_wait(time_to_wait=5)
        print(TorrentDownloader.google_search_url, flush=True)
        return self.__driver.find_element(By.TAG_NAME,'cite')

    def start(self):
        torrentqq_url = self.__torrent_site_url
        query = torrentqq_url.text + "/topic/index?category1=4&category2={}&page=".format(self.__category)
        maximum_page = 10
        for i in range(1, maximum_page):
            checking_url = query + str(i)
            print(checking_url, flush=True)
            link = self.__search_keyword(checking_url)
            if link is not None:
                print("find torrent file!", flush=True)
                self.__save_file(link)
                return True
        return False
