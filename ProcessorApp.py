from PyQt5.QtCore import QThread, pyqtSignal
from youtube_dl import YoutubeDL
import requests

class Processor(QThread):
    chunks = pyqtSignal(int)
    info_video = pyqtSignal(str, str, str)

    def __init__(self, url, path):
        super().__init__()

        self.url = url
        self.path = path

    def run(self):
        try:
            with YoutubeDL({'quiet': True}) as ydl:
                meta = ydl.extract_info(self.url, download=False)
                video_title = meta.get('title', None)
                video_description = meta.get('description', None)
                video_thumbnails = meta['thumbnails'][3]['url']

                self.info_video.emit(video_title, video_description, video_thumbnails)

                dl_options = {
                    'format': 'best',
                    'outtmpl': self.path + "/" + video_title + ".mp4",
                    'progress_hooks': [self.progress]
                }

                with YoutubeDL(dl_options) as dl:
                    dl.download([self.url])
        except Exception as ex:
            print(ex)

    def progress(self, percent):
        if percent['status'] == 'downloading':
            result = round(percent['downloaded_bytes'] / percent['total_bytes'] * 100, 1)

            print(round(percent['downloaded_bytes'] / percent['total_bytes'] * 100, 1))
            self.chunks.emit(result)


