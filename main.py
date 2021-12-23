import os
from glob import glob
import moviepy.editor as mp

def extract_audio(video_path, save_dir):    
    name = video_path.split("\\")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)  
    
    videoclip = mp.VideoFileClip(video_path)
    audioclip = videoclip.audio
    audioclip.write_audiofile(f"{save_path}.mp3".format(path))

if __name__ == "__main__":
    video_paths = glob("videos/*")
    save_dir = "audios"

    for path in video_paths:
        extract_audio(path, save_dir)