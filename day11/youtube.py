from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        return True, None
    except Exception as e:
        return False, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    save_path = "C:/Users/amvk2/OneDrive/Documents/YoutubeDownload"
    os.makedirs(save_path, exist_ok=True)
    success, error_message = download_video(url, save_path)
    if success:
        return render_template('downloaded.html')
    else:
        return render_template('error.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
