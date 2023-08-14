import time
import turtle
from turtle import Screen
from pista import Pista
from jogador import Jogador
from carro import CarroConfig
from pontuacao import Pontuacao


#Criando a Tela do Game
tela = Screen()
tela.bgcolor('beige')
#Criando a Resolução
tela.setup(600,600)
#Iniciando o Marcador no Zero
tela.tracer(0)
#Colocando Titulo
tela.title("Tartaruga")
#Pegando a Posição da Tela
tela.listen()
#Chamando as Funções
pista = Pista()
jogador = Jogador()
carro_config = CarroConfig()
pontuacao = Pontuacao()

#Adicioonando o Teclado e marcando a Posição na tela
tela.onkey(jogador.mover_direita,'Right')
tela.onkey(jogador.mover_esquerda,'Left')

#Verificando se o Jogo estiver ativado é para continuar atualizando os Frames
jogo_on = True

while jogo_on == True:
    time.sleep(0.1)
    carro_config.aparecer_carro()
    carro_config.mover_carro()
    if jogador.xcor() > 120 or jogador.xcor() <-120:
        turtle.write(f"Game Over",align='center',font=('arial',40,'bold'))
        jogo_on=False
    for carrinho in carro_config.carros:
        if abs(jogador.xcor() - carrinho.xcor()) <1 and jogador.distance(carrinho)< 65:
            turtle.write(f"Game Over ",align='center',font=('arial',40,'bold'))
            jogo_on=False
        if carrinho.ycor() < -230:
            pontuacao.aumentar_pontucao()
            carrinho.hideturtle()
            carro_config.carros.remove(carrinho)
    tela.update()

#Fechando o Jogo no botão de fechar
tela.exitonclick()