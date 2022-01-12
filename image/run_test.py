import TorrentDownloader
print('start test')

def test_download_success():
    downloader = TorrentDownloader.TorrentDownloader('옥탑방')
    result  = downloader.download_torrent_file()
    assert result == True, "success"
   
def test_download_fail():
    downloader = TorrentDownloader.TorrentDownloader('테스트')
    result  = downloader.download_torrent_file()
    assert result == False, "success"
