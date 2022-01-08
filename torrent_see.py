from selenium import webdriver
import sys
import requests

url = "https://www.google.com/search?q=%ED%86%A0%EB%A0%8C%ED%8A%B8%EC%94%A8"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("headless")
driver = webdriver.Chrome(executable_path='./chromedriver',options=options)
driver.get(url)
driver.implicitly_wait(time_to_wait=5)

torrentqq_url = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite')

keyword = '놀면'
if sys.argv[1] is not None:
    keyword = sys.argv[1]
query = torrentqq_url.text + "/topic/index?category1=4&category2=16&page="

def check_page(url):
    driver.get(url)
    driver.implicitly_wait(time_to_wait=5)
    latest_link = driver.find_elements_by_class_name('tit > a')
    for link in latest_link:
        if keyword in link.text:
            print(link.text)
            return link

def save_torrent_file(link):
    driver.get(link.get_attribute('href'))
    driver.implicitly_wait(time_to_wait=5)
    file_download_link = driver.find_element_by_class_name('bbs_btn1').get_attribute('href')
    res = requests.get(file_download_link)
    foldername = '/app/'
    filename = '{}.torrent'.format(keyword)
    with open(foldername+filename, 'wb') as f:
        f.write(res.content)
    print('download success')

for i in range(1, 10):
    checking_url = query + str(i)
    print(checking_url)
    link = check_page(checking_url)
    if link is not None:
        print("find torrent file!")
        save_torrent_file(link)
        break

driver.close()