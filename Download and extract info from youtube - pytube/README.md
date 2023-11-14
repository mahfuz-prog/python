#### Download audio, video, full playlist, extract information from youtube using pytub

* Uncomment method to work
```python
youtube = YouTube(url)

youtube.download_video(res='720p')
# youtube.video_info()
# youtube.playlist_info()
# youtube.download_audio(abr='160kbps')
# youtube.download(res='720p')
# youtube.download_playlist(res='720p')
```


Packages:
```
pytube==15.0.0
```
