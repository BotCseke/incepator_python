from question_mode import Question
from data import question_data
from Quiz_Brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question[question_text,question_answer]
    question_bank.append(new_question)
quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()