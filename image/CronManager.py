import json
import TorrentDownloader 
import schedule
import time
import datetime

def download(keyword, category):
    print('start download ' + keyword,flush=True)
    downloader = TorrentDownloader.TorrentDownloader(keyword, category)
    downloader.download_torrent_file()
    print('download complete ' + keyword,flush=True)
    print(datetime.datetime.now(),flush=True)
    print(schedule.jobs, flush=True)


with open('./download/schedule.json','r',encoding='utf-8') as f:
    json_data = json.load(f)

schedule.clear()

for data in json_data['data']:
    getattr(schedule.every(),data['week']).at(data['time']).do(download,data['keyword'],data['category']).tag(data['name'])
print(schedule.jobs,flush=True)
print('Start scheduling',flush=True )
while True:
    schedule.run_pending()
    time.sleep(1)