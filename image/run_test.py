import TorrentDownloader
print('start test')

def test_download_success():
    downloader = TorrentDownloader.TorrentDownloader('어서와')
    result  = downloader.download_torrent_file()
    assert result == True, "success"
   