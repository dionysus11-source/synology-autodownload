import TorrentDownloader
print('start test')

def test_download_success():
    downloader = TorrentDownloader.TorrentDownloader('영화가','16')
    result  = downloader.start()
    assert result == True, "success"
   