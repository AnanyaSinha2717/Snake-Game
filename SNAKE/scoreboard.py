from turtle import Turtle
with open('data.txt', mode='r+') as file:
    content = file.read()
    High_score = int(float(content))


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = High_score
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score} High score : {self.high_score}', align='center',
                   font=('Courier', 18, 'normal'))

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def score_calc(self):
        self.score += 1
        self.update_scoreboard()
