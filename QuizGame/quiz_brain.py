class QuizBrain:
    def __init__(self, qList):
        self.questionNumber = 0
        self.questionList = qList
        self.score = 0

    def next_question(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        answer = input(f"Q.{self.questionNumber} {currentQuestion.text} (True/False)?: ")
        self.checkAnswer(answer, currentQuestion.answer)

    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionList)

    def checkAnswer(self, guess, correct):
        if guess.lower() == correct.lower():
            self.score += 1
            print("Correct! You got the answer right!")

        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct}.")
        print(f"Your current score is: {self.score}/{self.questionNumber}")