import sys
from app.pdf_reader import extract_text_from_pdf
from app.summarizer import summarize_text
from app.flashcard_maker import generate_flashcards
from app.anki_exporter import export_to_anki

def process_pdf(pdf_path):
    print("📄 Extracting text...")
    raw_text = extract_text_from_pdf(pdf_path)

    print("🧠 Summarizing...")
    summary = summarize_text(raw_text)

    print("📚 Generating flashcards...")
    flashcards = generate_flashcards(summary)

    print("🔁 Exporting to Anki...")
    export_to_anki(flashcards, "study_flashcards.apkg")

    print("✅ Done! Your flashcards are ready.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app/main.py yourfile.pdf")
    else:
        process_pdf(sys.argv[1])
