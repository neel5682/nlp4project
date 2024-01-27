import os
import moviepy.editor as mp
import speech_recognition as sr


image_magick_path = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\convert.exe"
os.environ["IMAGEMAGICK_BINARY"] = image_magick_path
def extract_audio(video_path, audio_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path, codec='pcm_s16le')
    audio_clip.close()

def generate_subtitles(audio_path, subtitles_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        subtitles = recognizer.recognize_google(audio_data, show_all=True)

        if 'alternative' in subtitles:
            text = ' '.join([alt['transcript'] for alt in subtitles['alternative']])
            with open(subtitles_path, 'w') as subtitle_file:
                subtitle_file.write(text)
        else:
            print("No subtitles generated.")

def add_subtitles_to_video(video_path, subtitles_path, output_path):
    video_clip = mp.VideoFileClip(video_path)
    subtitles_text = open(subtitles_path, 'r').read()

    subtitles = mp.TextClip(subtitles_text, fontsize=24, color='white', bg_color='black')
    subtitles = subtitles.set_pos('bottom').set_duration(video_clip.duration)

    video_with_subtitles = mp.CompositeVideoClip([video_clip, subtitles])
    video_with_subtitles.write_videofile(output_path, codec='libx264', audio_codec='aac', temp_audiofile='temp_audio.m4a', remove_temp=True)

   
    video_clip.close()

if __name__ == "__main__":
    video_path = r"D:\Instagram VIDEO\VID_20070815_053221_160.mp4"
    audio_path = "audio.wav"
    subtitles_path = "subtitles.txt"
    output_video_path = "video_with_subtitles.mp4"

    extract_audio(video_path, audio_path)
    generate_subtitles(audio_path, subtitles_path)
    add_subtitles_to_video(video_path, subtitles_path, output_video_path)

    print(f"Video with subtitles generated and saved to {output_video_path}")
