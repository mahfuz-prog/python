import os
import datetime
import pytube

class YouTube:
    def __init__(self, url):
        self.url = url

    def video_info(self):
        if 'playlist' in self.url:
            return None
        
        obj = pytube.YouTube(self.url)
        print('-----------Video information-----------')
        print(f'Author name: {obj.author}')
        print(f'Video title: {obj.title}')
        print(f'Video description: {obj.description}')
        print(f'Video duration: {str(datetime.timedelta(seconds = obj.length))}')
        print(f'Publish date: {obj.publish_date}')
        print(f'Video views: {obj.views:,}')
        print(f'Thumbnail url: {obj.thumbnail_url}')
        print()

    def playlist_info(self):
        if 'watch?v=' in self.url:
            return None
        
        obj = pytube.contrib.playlist.Playlist(self.url)
        print('----------Playlist information-----------')
        print(f'Playlist url: {obj.playlist_url}')
        print(f'Author name: {obj.owner}')
        print(f'Playlist title: {obj.title}')
        print(f'Total videos in playlist: {obj.length}')
        print()
    
    def download_video(self, res='480p'):
        obj = pytube.YouTube(self.url)
        vid_obj = obj.streams.filter(adaptive=True, res=res, file_extension='mp4')[0]
        print('----------Video file-----------')
        print(f'Video title: {vid_obj.title}')
        print(f'Video file size: {vid_obj.filesize_mb} Mb')

        if 'Videos' in os.listdir():
            pass
        else:
            os.mkdir('Video only')

        print('Downloading...')
        vid_obj.download(filename=f'Video only/{vid_obj.default_filename}')
        print('Only video Downloaded')
        print()

    def download_audio(self, abr='160kbps'):
        obj = pytube.YouTube(self.url)
        audio_obj = obj.streams.filter(only_audio=True, abr=abr)[0]
        print('----------Audio file-----------')
        print(f'Audio title: {audio_obj.default_filename}')
        print(f'Audio file size: {audio_obj.filesize_mb} Mb')

        if 'Audio' in os.listdir():
            pass
        else:
            os.mkdir('Audio only')

        print('Downloading...')
        audio_obj.download(filename=f'Audio only/{audio_obj.default_filename}.mp3')
        print('Only audio Downloaded')
        print()

    def download(self, res='480p'):
        obj = pytube.YouTube(self.url)
        video = obj.streams.filter(res=res, file_extension='mp4')[0]
        print(f'Video title: {video.title}')
        print(f'Video file size: {video.filesize_mb} Mb')

        if 'Videos' in os.listdir():
            pass
        else:
            os.mkdir('Videos')

        print('Downloading...')
        video.download(filename=f'Videos/{video.default_filename}')
        print('Video Downloaded')

    def download_playlist(self, res='480p'):
        if 'index=' in self.url:
            obj = pytube.contrib.playlist.Playlist(self.url)
            self.url = obj.playlist_url
        
        obj = pytube.contrib.playlist.Playlist(self.url)
        print('----------Download playlist-----------')
        print(f'Total {len(obj.video_urls)} videos in playlist')
        i = 1
        for _ in obj.video_urls:
            self.url = _
            self.download(res=res)
            print(f'{i} video downloaded')
            print()
            i+=1

url = 'https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2'
youtube = YouTube(url)
# youtube.video_info()
# youtube.playlist_info()
# youtube.download_video(res='720p')
# youtube.download_audio(abr='160kbps')
# youtube.download(res='720p')
# youtube.download_playlist(res='720p')


# https://youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&si=RCEotNkCjIs0Baxg
# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2
# https://www.youtube.com/watch?v=vRapY8xJwn8&t=46s