questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris",
        "topic": "Geography"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "correct_answer": "Leonardo da Vinci",
        "topic": "Art"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Jupiter",
        "topic": "Science"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["O2", "H2O", "CO2", "NaCl"],
        "correct_answer": "H2O",
        "topic": "Science"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "choices": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "correct_answer": "William Shakespeare",
        "topic": "Literature"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["0", "1", "2", "3"],
        "correct_answer": "2",
        "topic": "Mathematics"
    },
    {
        "question": "Which element has the atomic number 1?",
        "choices": ["Helium", "Oxygen", "Hydrogen", "Carbon"],
        "correct_answer": "Hydrogen",
        "topic": "Science"
    },
    {
        "question": "What is the capital of Japan?",
        "choices": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
        "correct_answer": "Tokyo",
        "topic": "Geography"
    },
    {
        "question": "Who is known as the 'Father of Computers'?",
        "choices": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"],
        "correct_answer": "Charles Babbage",
        "topic": "Technology"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": ["Gold", "Iron", "Diamond", "Platinum"],
        "correct_answer": "Diamond",
        "topic": "Science"
    }
]



import random
import time

def run_quiz(questions, time_limit=0.1):
    score = 0
    total_questions = len(questions)

    # Shuffle the questions to make the quiz more interesting
    random.shuffle(questions)

    for q in questions:
        print(f"\nTopic: {q['topic']}")
        print(q['question'])

        # Print answer choices
        for i, choice in enumerate(q['choices'], 1):
            print(f"{i}. {choice}")

        # Start the timer
        start_time = time.time()

        # Get user's answer
        while True:
            user_answer = input(f"\nYour answer (1-{len(q['choices'])}): ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(q['choices']):
                break
            print("Invalid input. Please enter a number between 1 and", len(q['choices']))

        # Check if time's up
        if time.time() - start_time > time_limit:
            print("Time's up!")
        else:
            # Check if the answer is correct
            if q['choices'][int(user_answer)-1] == q['correct_answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Sorry, the correct answer was: {q['correct_answer']}")

        print(f"Time taken: {time.time() - start_time:.2f} seconds")

    # Print final score
    print(f"\nQuiz complete! Your score: {score}/{total_questions}")

if __name__=='__main__':
    run_quiz(questions)