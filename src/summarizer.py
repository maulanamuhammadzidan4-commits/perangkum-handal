from sklearn.feature_extraction.text import TfidfVectorizer


def calculate_tfidf(processed_sentences):
    """
    Mengubah kalimat menjadi representasi TF-IDF.
    """

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(processed_sentences)

    return vectorizer, tfidf_matrix


def calculate_sentence_scores(tfidf_matrix):
    """
    Menghitung skor setiap kalimat berdasarkan
    total nilai TF-IDF kata-kata di dalamnya.
    """

    scores = tfidf_matrix.sum(axis=1)

    return scores.A1


def select_sentences(original_sentences, scores, ratio=0.3):
    """
    Memilih kalimat berdasarkan skor TF-IDF.

    ratio:
        Persentase kalimat yang akan diambil.
    """

    total_sentences = len(original_sentences)

    sentence_count = max(
        1,
        round(total_sentences * ratio)
    )

    ranked_indices = sorted(
        range(total_sentences),
        key=lambda i: scores[i],
        reverse=True
    )

    selected_indices = ranked_indices[:sentence_count]

    # Kembalikan urutan sesuai posisi kalimat asli
    selected_indices.sort()

    summary = [
        original_sentences[i]
        for i in selected_indices
    ]

    return summary


def summarize(text, ratio=0.3):
    """
    Fungsi utama untuk menghasilkan ringkasan.
    """

    from preprocessing import prepare_sentences

    original_sentences, processed_sentences = prepare_sentences(text)

    # Hindari error jika tidak ada kalimat
    if not processed_sentences:
        return ""

    # Hindari error jika semua kalimat kosong
    if not any(processed_sentences):
        return ""

    _, tfidf_matrix = calculate_tfidf(processed_sentences)

    scores = calculate_sentence_scores(tfidf_matrix)

    summary_sentences = select_sentences(
        original_sentences,
        scores,
        ratio
    )

    return " ".join(summary_sentences)


# =========================
# TEST
# =========================

if __name__ == "__main__":

    materi = """
    Python adalah bahasa pemrograman tingkat tinggi yang populer.
    Python banyak digunakan untuk pengembangan aplikasi.
    Python memiliki sintaks yang relatif mudah dipahami.
    Bahasa ini dapat digunakan untuk pengembangan web.
    Python juga banyak digunakan dalam bidang data science.
    Python memiliki banyak library yang membantu programmer.
    """

    ringkasan = summarize(materi, ratio=0.5)

    print("=== RINGKASAN ===")
    print(ringkasan)