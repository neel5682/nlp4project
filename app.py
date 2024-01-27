
from flask import Flask, render_template, request
from main import record_text, speak_text, output_text_to_file
from index import extract_audio, generate_subtitles, add_subtitles_to_video

import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form['action']

        if action == 'record':
            recorded_text = record_text()
            if recorded_text:
                output_text_to_file(recorded_text)
        elif action == 'speak':
            text_to_speak = request.form['text_to_speak']
            speak_text(text_to_speak)
        elif action == 'subtitle':
            video_path = r"D:\Instagram VIDEO\VID_21921226_063754_345.mp4"  
            audio_path = "audio.wav"
            subtitles_path = "subtitles.txt"
            output_video_path = "video_with_subtitles.mp4"

            extract_audio(video_path, audio_path)
            generate_subtitles(audio_path, subtitles_path)
            add_subtitles_to_video(video_path, subtitles_path, output_video_path)
        elif action == 'audio':
            
            pass
        elif action == 'text':
            
            pass

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
