import moviepy.editor
# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip("C:\\Users\\alex\\Downloads\\videoplayback.mp4")
audio = video.audio
# Replace the parameter with the location along with filename
audio.write_audiofile("C:\\Users\\alex\\Desktop\\songs\\samle.mp3")

