from transformers import pipeline

# Load a stronger question-generation model
question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")

def generate_flashcards(text):
    flashcards = []

    # Split text into manageable sentences
    sentences = text.split(". ")
    
    for sentence in sentences:
        clean_sentence = sentence.strip()
        if len(clean_sentence.split()) > 8:  # skip very short lines
            # Format for highlight-style question generation
            highlighted_input = f"highlight: {clean_sentence} </s>"
            
            # Generate multiple questions
            results = question_generator(
                highlighted_input,
                max_length=64,
                do_sample=True,
                top_k=50,
                num_return_sequences=2,  # Change this number to get more per sentence
            )
            
            for result in results:
                question = result['generated_text']
                flashcards.append((question, clean_sentence))

    return flashcards

