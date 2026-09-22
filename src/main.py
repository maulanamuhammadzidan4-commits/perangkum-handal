from pathlib import Path

from summarizer import summarize


def read_file(file_path):
    """Membaca materi dari file teks."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File tidak ditemukan: {file_path}"
        )

    return path.read_text(encoding="utf-8")


def main():
    project_root = Path(__file__).parent.parent
    file_path = project_root / "data" / "materi.txt"

    try:
        materi = read_file(file_path)

        if not materi.strip():
            print("Materi kosong.")
            return

        ringkasan = summarize(
            materi,
            ratio=0.3
        )

        print(len(materi.split()), "kata dalam materi.")
        print(len(ringkasan.split()), "kata dalam ringkasan.")

        print("=" * 50)
        print("RINGKASAN MATERI")
        print("=" * 50)
        print()
        print(ringkasan)
        print()

    except FileNotFoundError as error:
        print(error)


if __name__ == "__main__":
    main()