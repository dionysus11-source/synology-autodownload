from selenium import webdriver
import requests
import copy
from selenium.webdriver.common.by import By

class TorrentDownloader:
    google_search_url = "https://www.google.com/search?q=%ED%86%A0%EB%A0%8C%ED%8A%B8%EC%94%A8"
    
    def __init__(self,keyword):
        self.__keyword = keyword
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-infobars")

       #self.__driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=options)
        self.__driver = webdriver.Chrome(executable_path='./chromedriver',options=options)
        self.__driver.set_page_load_timeout(60)
    
    def __del__(self):
        self.__driver.close()
        
    @property
    def keyword(self):
        return copy.deepcopy(self.__keyword)
    
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
    
    def __get_torrent_site_url(self):
        self.__driver.get(TorrentDownloader.google_search_url)
        self.__driver.implicitly_wait(time_to_wait=5)
        print(TorrentDownloader.google_search_url, flush=True)
        return self.__driver.find_element(By.TAG_NAME,'cite')

    def download_torrent_file(self):
        torrentqq_url = self.__get_torrent_site_url()
        query = torrentqq_url.text + "/topic/index?category1=4&category2=16&page="
        for i in range(1, 10):
            checking_url = query + str(i)
            print(checking_url, flush=True)
            link = self.__search_keyword(checking_url)
            if link is not None:
                print("find torrent file!", flush=True)
                self.__save_file(link)
                return True
        return False
