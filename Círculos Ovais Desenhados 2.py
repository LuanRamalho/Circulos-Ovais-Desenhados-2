import turtle
import random

def desenhar_oval(x, y, largura, altura, cor):
    """Desenha um oval em uma posição e cor específica."""
    turtle.penup()
    turtle.goto(x, y - altura / 2)
    turtle.pendown()
    turtle.color(cor)
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(altura / 2, 90)  # Metade da altura
        turtle.circle(largura / 2, 90)  # Metade da largura
    turtle.end_fill()

def main():
    # Configurações iniciais
    turtle.speed("fastest")
    turtle.bgcolor("black")  # Fundo preto para destacar as cores

    # Geração de quantidade aleatória de ovais
    quantidade = random.randint(5, 20)  # Entre 5 e 20 ovais
    cores = ["red", "blue", "green", "yellow", "purple", "orange", "white", "pink"]

    for _ in range(quantidade):
        x = random.randint(-200, 200)  # Coordenada X
        y = random.randint(-200, 200)  # Coordenada Y
        largura = random.randint(50, 150)  # Largura do oval
        altura = random.randint(30, 100)  # Altura do oval
        cor = random.choice(cores)  # Cor aleatória
        desenhar_oval(x, y, largura, altura, cor)

    # Finaliza o desenho
    turtle.done()

if __name__ == "__main__":
    main()
