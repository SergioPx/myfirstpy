import vlc
import pafy

def try_me():
    '''
    Docstring obligado 
    '''

    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    # url of the video

    
    # creating pafy object of the video
    video = pafy.new(url)
    
    # getting best stream
    best = video.getbest()
    
    # creating vlc media player object
    media = vlc.MediaPlayer(best.url)
    
    # start playing video
    media.play()
    
try_me()
