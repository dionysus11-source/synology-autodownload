import json
import TorrentDownloader 
import schedule
import time

def download(keyword):
    downloader = TorrentDownloader.TorrentDownloader(keyword)
    downloader.download_torrent_file()

with open('./download/schedule.json','r',encoding='utf-8') as f:
    json_data = json.load(f)

schedule.clear()

for data in json_data['data']:
    getattr(schedule.every(),data['week']).at(data['time']).do(download,data['keyword']).tag(data['name'])
print(schedule.jobs)
print('Start scheduling',flush=True )
while True:
    schedule.run_pending()
    time.sleep(1)