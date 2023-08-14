from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super().__init__()

        self.pontuacao =0
        self.penup()
        self.goto(-250,150)
        self.pontuacao_config()

    def pontuacao_config(self):
        self.clear()
        self.write(f"PONTUACAO : \n {self.pontuacao}",align='left',font=('arial',10,'bold'))

    def aumentar_pontucao(self):
        self.pontuacao += 1
        self.pontuacao_config()