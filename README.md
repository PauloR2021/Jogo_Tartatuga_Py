🐢 Jogo da Tartaruga

Jogo 2D desenvolvido em Python com a biblioteca Turtle. Você controla uma tartaruga numa pista de 5 faixas e precisa desviar dos carros que descem pela tela. Cada carro desviado vale um ponto. Se bater ou sair da pista, é Game Over.

🎮 Como jogar
Tecla	Ação
→ (seta direita)	Move a tartaruga uma faixa para a direita
← (seta esquerda)	Move a tartaruga uma faixa para a esquerda

Regras

Os carros aparecem no topo, em faixas aleatórias, e descem a cada frame.
Cada carro que passa da tartaruga e sai da tela soma +1 ponto.
O jogo termina (Game Over) quando:
a tartaruga colide com um carro; ou
a tartaruga sai dos limites da pista (x > 120 ou x < -120).
Para fechar a janela depois do fim de jogo, basta clicar nela.
🛠️ Tecnologias utilizadas
Tecnologia	Uso
Python 3.11	Linguagem principal
turtle (biblioteca padrão)	Janela, desenho da pista, sprites e captura de teclado
tkinter (dependência do turtle)	Interface gráfica por baixo do Turtle
random (biblioteca padrão)	Sorteio de faixa e cor dos carros
time (biblioteca padrão)	Controle da velocidade do loop do jogo

O projeto não usa nenhuma dependência externa: não há pip install.

🧩 Conceitos aplicados
Programação Orientada a Objetos: classes que herdam de Turtle (Pista, Jogador, Pontuacao) e uma classe de gerenciamento (CarroConfig).
Game loop: while com time.sleep(0.1) e tela.update().
Animação manual: tela.tracer(0) desliga a animação automática, e a tela só é redesenhada no tela.update().
Eventos de teclado: tela.listen() e tela.onkey().
Detecção de colisão por posição no eixo X e distance().
Modularização: cada elemento do jogo em seu próprio arquivo.
📁 Estrutura do projeto
Jogo_Tartatuga_Py/
├── main.py        # Configura a tela, executa o loop principal e trata colisões
├── jogador.py     # Classe Jogador: a tartaruga e seus movimentos
├── carro.py       # Classe CarroConfig: criação e movimentação dos carros
├── pista.py       # Classe Pista: desenha as linhas e faixas da pista
├── pontuacao.py   # Classe Pontuacao: placar na tela
├── README.md
└── .gitignore
Responsabilidade de cada módulo
main.py: cria a janela (600x600, fundo beige), instancia os objetos, registra as teclas e roda o loop. Também verifica colisão, saída da pista e pontuação.
jogador.py: Jogador é uma tartaruga (shape('turtle')) iniciada em (0, -220). Cada movimento lateral desloca 60 px, o equivalente a uma faixa.
carro.py: CarroConfig mantém a lista de carros. Cada carro é um quadrado com cor aleatória (8 opções) que nasce em uma de 5 posições x (-120, -60, 0, 60, 120) e desce 30 px por frame. Um novo carro surge quando o último passa da altura y = 20.
pista.py: Pista desenha as bordas e os tracejados que separam as faixas.
pontuacao.py: Pontuacao escreve o placar no canto superior esquerdo e o atualiza a cada ponto.
▶️ Como executar
Pré-requisitos
Python 3.8+ (desenvolvido com 3.11)
Tkinter disponível (já vem com o Python no Windows e no macOS)

No Linux, se necessário:

bash
sudo apt install python3-tk
Rodando
bash
# 1. Clone o repositório
git clone https://github.com/<seu-usuario>/Jogo_Tartatuga_Py.git

# 2. Entre na pasta
cd Jogo_Tartatuga_Py

# 3. Execute o jogo
python main.py
⚙️ Personalização

Alguns valores fáceis de ajustar:

O que mudar	Onde	Valor atual
Velocidade do jogo (menor = mais rápido)	main.py → time.sleep(...)	0.1
Velocidade de queda dos carros	carro.py → carro.forward(...)	30
Cores dos carros	carro.py → lista cores	8 cores
Distância de cada movimento lateral	jogador.py → ± 60	60
Cor de fundo	main.py → tela.bgcolor(...)	beige
🚀 Ideias de melhorias futuras
Aumentar a dificuldade conforme a pontuação cresce
Tela de início e opção de reiniciar após o Game Over
Recorde (high score) salvo em arquivo
Mais de um carro por vez na tela
Efeitos sonoros
👨‍💻 Autor

Desenvolvido por Paulo Ricardo, desenvolvedor back-end.
