import json
import torrent_see

downloader = torrent_see.TorrentDownloader("산다")
downloader.download_torrent_file()

with open('schedule.json','r') as f:
    json_data = json.load(f)



