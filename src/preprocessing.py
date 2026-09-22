import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import (
    StopWordRemoverFactory
)

# stemmer init
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

# stopword remover init
stopword_remover_factory = StopWordRemoverFactory()
stopword_remover = stopword_remover_factory.create_stop_word_remover()


def clean_text(text):
    """ Bersihkan teks dari karakter yang tidak diperlukan """

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)  # hapus karakter non-alfanumerik
    text = re.sub(r"\s+", " ", text)  # hapus spasi berlebih

    return text.strip()

def remove_stopwords(text):
    """ Hapus kata umum yang tidak penting """
    return stopword_remover.remove(text)

def stemming(text):
    """ Normalisasi kata ke bentuk dasar """
    return stemmer.stem(text)

def preprocess_text(text):
    """ Proses pipeline lengkap """
    text = clean_text(text)
    text = remove_stopwords(text)
    text = stemming(text)

    return text

def sentences_segmentation(text):
    """ Pisahkan teks menjadi kalimat """
    sentences = re.split(f"(?<=[.!?])\s+", text.strip())

    return sentences

def prepare_sentences(text):
    """ Preprocess setiap kalimat """
    original_sentences = sentences_segmentation(text)
    processed_sentences = [preprocess_text(sentences) for sentences in original_sentences]

    return original_sentences, processed_sentences

if __name__ == '__main__':
    materi = """
    Python adalah bahasa pemrograman.
    Python banyak digunakan untuk membuat aplikasi.
    Bahasa Python relatif mudah dipelajari.
    """

    original, processed = prepare_sentences(materi)

    for i in range(len(original)):
        print(f"Original : {original[i]}")
        print(f"Processed: {processed[i]}")
        print()