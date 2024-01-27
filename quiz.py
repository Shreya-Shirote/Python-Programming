
import random

class Quiz:
    def __init__(self):
        self.questions = {
            'General Knowledge': [
                {'question': 'What is the capital of France?', 'options': ['A. Paris', 'B. Berlin', 'C. Madrid'], 'answer': 'A'},
                {'question': 'Which planet is known as the Red Planet?', 'options': ['A. Mars', 'B. Jupiter', 'C. Saturn'], 'answer': 'A'},
            ],
            'Science': [
                {'question': 'What is the chemical symbol for water?', 'options': ['A. Wo', 'B. Wt', 'C. H2O'], 'answer': 'C'},
                {'question': 'Which gas do plants absorb from the air?', 'options': ['A. Oxygen', 'B. Carbon dioxide', 'C. Nitrogen'], 'answer': 'B'},
            ],
            # Add more categories and questions as needed
        }
        self.score = 0

    def get_random_question(self, category):
        questions = self.questions.get(category)
        if questions:
            return random.choice(questions)
        else:
            return None

    def display_question(self, question_data):
        print(question_data['question'])
        for option in question_data['options']:
            print(option)
        user_answer = input("Your answer (enter the letter corresponding to your choice): ").upper()
        return user_answer

    def check_answer(self, question_data, user_answer):
        return user_answer == question_data['answer']

    def start_quiz(self):
        print("Welcome to the Quiz App!")

        for category in self.questions.keys():
            print(f"\nCategory: {category}")
            question_data = self.get_random_question(category)
            while question_data:
                user_answer = self.display_question(question_data)
                if self.check_answer(question_data, user_answer):
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is: {question_data['answer']}\n")
                question_data = self.get_random_question(category)

        print(f"Quiz completed! Your final score is: {self.score}/{sum(len(questions) for questions in self.questions.values())}")

# Create an instance of the Quiz class and start the quiz
quiz = Quiz()
quiz.start_quiz()
