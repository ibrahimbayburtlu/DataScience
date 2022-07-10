import pytube 

def downloadvideo(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    print(video.title)
    video.download()

print("Hello Youtube Download Program")
url = input("Enter the url:")
downloadvideo(url)