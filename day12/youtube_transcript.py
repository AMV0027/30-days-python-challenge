from flask import Flask, render_template, request
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
summarizer = pipeline('summarization')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_video = request.form['youtube_video']
        video_id = youtube_video.split("=")[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        result = " ".join([i['text'] for i in transcript])
        
        num_iters = int(len(result)/1000)
        summarized_text = []
        for i in range(0, num_iters + 1):
            start = i * 1000
            end = (i + 1) * 1000
            out = summarizer(result[start:end])
            out = out[0]['summary_text']
            summarized_text.append(out)

        youtube_video = str(youtube_video.replace("/watch?v=", "/embed/"))
        print(youtube_video)
        
        return render_template('index.html', youtube_video=youtube_video, summarized_text=summarized_text, transcript_text = result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
