quetions = [
    {
        'question':"What is the capital of England?",
        'options': ["A) Chatragram", "B) Dhaka", "C) Jessore", "D) London"],
        'answer': 'D'
    },
    {
        'question':"Which planet is known as red planet?",
        'options': ["A) Earth", "B) Mars", "C) Jupitor", "D) Venus"],
        'answer': 'B'
    },
    {
        'question':"Who wrote the pay 'Romio & juliot'?",
        'options': ["A) William Shakespear", "B) Charles Dickens", "C) Rabindranath Tagore", "D) Kazi Nazrul Islam"],
        'answer': 'A'
    },
    {
        'question':"What is longest ocean in Earth?",
        'options': ["A) Atlantic", "B) Indian", "C) Arctic", "D) Specific"],
        'answer': 'D'
    },
    {
        'question':"What is the chemical symboll of Water?",
        'options': ["A) CO2", "B) H2O", "C) O2", "D) Nacl"],
        'answer': 'B'
    }
]

score = 0


print(f"Welcome to the quiz game!")
print('---------------------\n')

for idx, question in enumerate(quetions,1):
    print(f"Q{idx} : {question['question']}")

    for option in question['options']:
        print(option)

    ans = input("Enter your answer (A/B/C/D) ").strip().upper()

    if ans == question['answer']:
        score += 1
        print(f'Correct\n')
    else:
        print(f"Wrong. the answer is {question['answer']}")

    
if score == len(quetions):
    print(f"Excellent! Perfact score")
elif score >= len(quetions) // 2:
    print(f"Good job")
else:
    print('Keep Practicing\n')

input('\n Press enter to exit....') 



#What it does:
#A list of 5 quiz questions is stored, each with:

#A question text
#Four answer options (A, B, C, D)
#The correct answer key
#The game starts with a welcome message.
#It loops through each question one by one:
#Displays the question and its options.
#Takes the user’s answer input, trims spaces, and converts it to uppercase.
#Compares the answer with the correct one:
#If correct, increases the score and prints "Correct"
#If wrong, shows the correct answer
#After all questions:
#If the user got all right, it says "Excellent! Perfect score"
#If the user got at least half, it says "Good job"
#Otherwise, it says "Keep Practicing"
#Finally, it waits for the user to press enter to exit.
