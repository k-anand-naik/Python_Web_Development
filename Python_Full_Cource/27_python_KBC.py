def play_kbc():
    # List to store questions, options, and correct answers
    questions = [
        {
            "question": "Who is known as the Father of the Indian Constitution?",
            "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Dr. B.R. Ambedkar", "D. Sardar Patel"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Rome", "D. Paris"],
            "answer": "D"
        },
        {
            "question": "Which is the largest mammal?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
            "answer": "B"
        }
    ]
    
    # Prize money for each correct answer
    prize_money = [1000, 2000, 5000, 10000]
    total_amount = 0
    
    print("Welcome to KBC!")
    
    # Loop through each question
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # Get the user's answer
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        # Check if the answer is correct
        if user_answer == q['answer']:
            print("Correct answer!")
            total_amount += prize_money[i]
            print(f"You have won: {total_amount} INR")
        else:
            print("Incorrect answer!")
            print(f"You're taking home: {total_amount} INR")
            break
    else:
        # If all questions are answered correctly
        print(f"Congratulations! You've answered all questions correctly and won: {total_amount} INR")
    
    print("Thank you for playing KBC!")

# Call the function to start the game
play_kbc()
