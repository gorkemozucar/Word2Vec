from gensim.models.fasttext import load_facebook_vectors
import os

def load_model():
    print("Model yükleniyor (bu işlem birkaç dakika sürebilir)...")
    model_path = 'cc.tr.300.bin/cc.tr.300.bin'
    
    if not os.path.exists(model_path):
        raise FileNotFoundError("cc.tr.300.bin dosyası bulunamadı. Lütfen dosyanın doğru konumda olduğundan emin olun.")
    
    try:
        # Load the FastText model directly
        model = load_facebook_vectors(model_path)
        print("Model başarıyla yüklendi!")
        return model
    except Exception as e:
        raise Exception(f"Model yüklenirken hata oluştu: {str(e)}")

def find_similar_words(model, word, n=10):
    try:
        # Get the most similar words
        similar_words = model.most_similar(word, topn=n)
        print(f"\n'{word}' kelimesine en yakın {n} kelime:")
        for i, (similar_word, similarity) in enumerate(similar_words, 1):
            print(f"{i}. {similar_word} (benzerlik: {similarity:.4f})")
    except KeyError:
        print(f"Üzgünüm, '{word}' kelimesi sözlükte bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")

def main():
    try:
        # Load the model
        model = load_model()
        
        while True:
            # Get input from user
            word = input("\nBir kelime girin (çıkmak için 'quit' yazın): ").strip().lower()
            
            if word == 'quit':
                print("Güle güle!")
                break
                
            if word:
                find_similar_words(model, word)
            else:
                print("Lütfen geçerli bir kelime girin.")
    except Exception as e:
        print(f"Program başlatılırken bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    main() 