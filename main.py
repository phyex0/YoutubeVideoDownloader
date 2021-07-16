from pytube import YouTube
import os
import platform

def desktopDirectory():
    desktop =""
    if platform.system() == "Windows":
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    else:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    return desktop

def videoDownloander(link):

    SAVE_PATH = desktopDirectory()

    for i in link:
        try:

            # object creation using YouTube
            # which was imported in the beginning
            yt = YouTube(i)
        except:

            # to handle exception
            print("Connection Error")

        try:
            # downloading the video
            stream = yt.streams.first()
            stream.download(SAVE_PATH)
        except:
            print("Some Error!")
    print('Task Completed!')




if __name__ == '__main__':
    list =[]
    link=""
    while True:
        link= input("Enter Youtube Links. Press -1 to quit")
        if link == "-1":
            break
        list.append(link)
    if len(list) > 0:
        videoDownloander(list)


