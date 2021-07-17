from pytube import YouTube
import os
import platform


# to install required packages
def packetInstaller():
    packets = ["pytube"]

    if platform.system() == "Windows":
        os.system('cmd /c "pip install ' + " ".join(packets) + '"')
    else:
        os.system("pip install " + " ".join(packets))


#takes the Desktop directory of the OS to save video.
def desktopDirectory():
    desktop =""
    if platform.system() == "Windows":
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    else:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    return desktop

# Video downloader
def videoDownloander(link):

    SAVE_PATH = desktopDirectory()

    for i in link:
        try:

            # object creation using YouTube
            # which was imported in the beginning
            print("Track :"+i)
            yt = YouTube(i)
        except:

            # to handle exception
            print("Connection Error")

        try:
            # downloading the video
            yt.streams.first().download(SAVE_PATH)
        except:
            print("Some Error!")
    print('Task Completed!')




if __name__ == '__main__':
    packetInstaller()
    list =[]
    link=""
    while True:
        link= input("Enter Youtube Links. Press -1 to quit")
        if link == "-1":
            break
        list.append(link)
    if len(list) > 0:
        print("Task begins. Please be patient...")
        videoDownloander(list)


