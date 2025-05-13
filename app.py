from flask import Flask, render_template, request, jsonify
from word_similarity_bin import load_model, find_similar_words
import os

app = Flask(__name__)

# Load the model when the application starts
model = None
try:
    model = load_model()
except Exception as e:
    print(f"Model yüklenirken hata oluştu: {str(e)}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find_similar', methods=['POST'])
def find_similar():
    if model is None:
        return jsonify({'error': 'Model yüklenemedi. Lütfen daha sonra tekrar deneyin.'}), 500
    
    word = request.json.get('word', '').strip().lower()
    if not word:
        return jsonify({'error': 'Lütfen bir kelime girin.'}), 400
    
    try:
        similar_words = model.most_similar(word, topn=10)
        return jsonify({
            'word': word,
            'similar_words': [{'word': w, 'similarity': float(s)} for w, s in similar_words]
        })
    except KeyError:
        return jsonify({'error': f"'{word}' kelimesi sözlükte bulunamadı."}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 