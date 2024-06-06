# cards/utils.py
import re

def chunk_document(text, chunk_size=1000):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i + chunk_size])

def generate_flashcard_text(client, chunk, number):
    prompt = f"""
    Analyze the text and generate exactly {number} questions with answers.
    Format each one as:
    question: ...
    answer: ...
    
    Here is the text to analyze:
    {chunk}
    """
    
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1500
    )
    
    # Extract questions and answers from the response using regex
    response_text = response.choices[0].text.strip()
    flashcards = {}
    
    qa_pairs = re.findall(r'question:\s*(.*?)\s*answer:\s*(.*?)(?=question:|$)', response_text, re.IGNORECASE | re.DOTALL)
    
    for question, answer in qa_pairs:
        question = question.strip().capitalize()
        answer = answer.strip().capitalize()
        flashcards[question] = answer

    return flashcards
