from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input text from the form
        input_text = request.form['input_text']
        
        # Generate text using the model with the input text as the prompt
        generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
        generated_text = generator(input_text, do_sample=True, min_length=50)[0]['generated_text']
        
        # Pass the generated text and input text to the template
        return render_template('index.html', generated_text=generated_text, input_text=input_text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
