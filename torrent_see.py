from selenium import webdriver
import requests

class TorrentDownloader:
    def __init__(self, keyword):
        self.url = "https://www.google.com/search?q=%ED%86%A0%EB%A0%8C%ED%8A%B8%EC%94%A8"
        self.keyword = keyword
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("headless")
        self.driver = webdriver.Chrome(executable_path='./chromedriver',options=options)

    def find_keyword(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(time_to_wait=5)
        latest_link = self.driver.find_elements_by_class_name('tit > a')
        for link in latest_link:
            if self.keyword in link.text:
                print(link.text)
                return link

    def save_torrent_file(self, link):
        self.driver.get(link.get_attribute('href'))
        self.driver.implicitly_wait(time_to_wait=5)
        file_download_link = self.driver.find_element_by_class_name('bbs_btn1').get_attribute('href')
        res = requests.get(file_download_link)
        foldername = '/app/'
        filename = '{}.torrent'.format(self.keyword)
        with open(foldername+filename, 'wb') as f:
            f.write(res.content)
        print('download success')

    def download_torrent_file(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(time_to_wait=5)

        torrentqq_url = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite')
        query = torrentqq_url.text + "/topic/index?category1=4&category2=16&page="
        for i in range(1, 10):
            checking_url = query + str(i)
            print(checking_url)
            link = self.find_keyword(checking_url)
            if link is not None:
                print("find torrent file!")
                self.save_torrent_file(link)
                break

        self.driver.close()