import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import pyfiglet

font = pyfiglet.figlet_format("Text summariser")
print(font)

def preprocess_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stopwords_list = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stopwords_list]
    return words, sentences

def compute_word_frequencies(words):
    freq_dist = FreqDist(words)
    return freq_dist

def score_sentences(sentences, word_freq):
    sentence_scores = {}
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        score = sum([word_freq[word] for word in words if word in word_freq])
        sentence_scores[sentence] = score
    return sentence_scores

def generate_summary(sentences, sentence_scores, num_sentences=3):
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:num_sentences])
    return summary


def text_summarization_tool(text):
    words, sentences = preprocess_text(text)
    word_freq = compute_word_frequencies(words)
    sentence_scores = score_sentences(sentences, word_freq)
    summary = generate_summary(sentences, sentence_scores)
    return summary
# Example usage:
input_text = input("Enter or paste  paragraph to summarize : ")
summary = text_summarization_tool(input_text)
print("\n\n--------------------------------------------------------\n\n")
print("Summary:\n", summary)
print("\n\n--------------------------------------------------------\n\n")

