import genanki
import uuid

def export_to_anki(flashcards, output_file):
    model_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF
    deck_id = uuid.uuid4().int & 0x7FFFFFFFFFFFFFFF

    my_model = genanki.Model(
        model_id,
        "Simple Model",
        fields=[{"name": "Question"}, {"name": "Answer"}],
        templates=[{
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}"
        }]
    )

    my_deck = genanki.Deck(deck_id, "Study Guide Deck")

    for q, a in flashcards:
        note = genanki.Note(model=my_model, fields=[q, a])
        my_deck.add_note(note)

    genanki.Package(my_deck).write_to_file(output_file)

