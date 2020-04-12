import threading
import os
import moviepy.editor


def convert(vid,i):
    global path_of_videos
    vid = path_of_videos + '\\'+vid
    print(" in convert function ",vid)
    video = moviepy.editor.VideoFileClip(vid)
    audio = video.audio
    # Replace the parameter with the location along with filename
    audio.write_audiofile(f"C:\\Users\\alex\\Desktop\\songs2\\audio{i}.mp3")


path_of_videos = input("Enter path of videos")

videos = os.listdir(path_of_videos)
print(videos)
i=0

for vid in videos:
    if vid.endswith(".mp4"):
        print(f"{i} : {vid} \n")
        threading.Thread(target=convert, args=(vid,i,)).start()
        i+=1

print("All video is converted to audio")

# C:\Users\alex\Desktop\videos



