from pytube import YouTube


def download():
        
    choice=input('Do you want audio or video?(a/v)')
    
    if choice == 'a':
        link =input('Please give me the fucking link')
        yt = Youtube(link)
        stream = yt.streams.filter(only_audio=True).all()
        stream.download()
    
    if choice == 'v':
        link =input('Please give me the fucking link')
        yt = YouTube(link)
    
        stream = yt.streams.filter(progressive=True).first()
        stream.download()
    
    


