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
stopword_remover = stopword_remover_factory.create_stopword_remover()


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