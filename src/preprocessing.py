import re

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import (
    StopWordRemoverFactory
)


# =========================
# SASTRAWI INITIALIZATION
# =========================

stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

stopword_remover_factory = StopWordRemoverFactory()
stopword_remover = stopword_remover_factory.create_stop_word_remover()


# =========================
# TEXT PREPROCESSING
# =========================

def clean_text(text):
    """Bersihkan teks dari karakter yang tidak diperlukan."""

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def remove_stopwords(text):
    """Hapus kata umum yang tidak terlalu informatif."""

    return stopword_remover.remove(text)


def stemming(text):
    """Normalisasi kata ke bentuk dasarnya."""

    return stemmer.stem(text)


def preprocess_text(text):
    """Menjalankan seluruh pipeline preprocessing."""

    text = clean_text(text)
    text = remove_stopwords(text)
    text = stemming(text)

    return text


# =========================
# SENTENCE SEGMENTATION
# =========================

def sentences_segmentation(text):
    """Memisahkan teks menjadi beberapa kalimat."""

    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    return [sentence.strip() for sentence in sentences if sentence.strip()]


# =========================
# PREPARE SENTENCES
# =========================

def prepare_sentences(text):
    """
    Memisahkan teks menjadi kalimat,
    kemudian melakukan preprocessing
    pada setiap kalimat.
    """

    original_sentences = sentences_segmentation(text)

    processed_sentences = [
        preprocess_text(sentence)
        for sentence in original_sentences
    ]

    return original_sentences, processed_sentences


# =========================
# TEST
# =========================

if __name__ == "__main__":

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