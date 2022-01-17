import TorrentDownloader
print('start test')

def test_download_success():
    downloader = TorrentDownloader.TorrentDownloader('꼬리를','17')
    result  = downloader.download_torrent_file()
    assert result == True, "success"
   