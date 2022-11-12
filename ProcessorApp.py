from PyQt5.QtCore import QThread, pyqtSignal
from youtube_dl import YoutubeDL


class Processor(QThread):
    chunks = pyqtSignal(int)
    info_video = pyqtSignal(str, str, str, str)

    def __init__(self, url, path, check_status, type_file):
        super(Processor, self).__init__()

        self.url = url
        self.path = path
        self.check_status = check_status
        self.type_file = type_file

    def run(self) -> None:
        type_video = self.type_file['video']
        try:
            if self.check_status == 0:
                with YoutubeDL({'quiet': True}) as ydl:
                    meta = ydl.extract_info(self.url, download=False)
                    video_title = meta.get('title', None)
                    video_description = meta.get('description', None)
                    video_thumbnails = meta['thumbnails'][3]['url']

                    self.info_video.emit(video_title, video_description, video_thumbnails, type_video)

                    dl_options = {
                        'format': 'best',
                        'outtmpl': self.path + "/" + video_title + ".mp4",
                        'progress_hooks': [self.progress]
                    }

                    with YoutubeDL(dl_options) as dl:
                        dl.download([self.url])
            else:
                type_audio = self.type_file['audio']
                with YoutubeDL({'quiet': True}) as ydl:
                    meta = ydl.extract_info(self.url, download=False)
                    video_title = meta.get('title', None)
                    video_description = meta.get('description', None)
                    video_thumbnails = meta['thumbnails'][3]['url']

                    self.info_video.emit(video_title, video_description, video_thumbnails, type_audio)

                    audio = YoutubeDL({'format': 'bestaudio',
                                       'postprocessors': [{
                                           'key': 'FFmpegExtractAudio',
                                           'preferredcodec': 'mp3',
                                           'preferredquality': '192',
                                       }],
                                       'outtmpl': self.path + "/" + video_title + ".mp4",
                                       'progress_hooks': [self.progress]
                                       })
                    audio.extract_info(self.url)

        except Exception as ex:
            print(ex)

    def progress(self, percent):
        if percent['status'] == 'downloading':
            result = round(percent['downloaded_bytes'] / percent['total_bytes'] * 100, 1)

            print(round(percent['downloaded_bytes'] / percent['total_bytes'] * 100, 1))
            self.chunks.emit(int(result))
