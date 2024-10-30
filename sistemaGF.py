import numpy as np
import skfuzzy as fuzz 
from skfuzzy import control as ctrl
import random

def configurar_sistema_fuzzy():

    angulo = ctrl.Antecedent(np.arange(-90, 91, 1), 'angulo')
    velocidade_angular = ctrl.Antecedent(np.arange(-10, 11, 1), 'velocidade_angular')
    posicao_carro = ctrl.Antecedent(np.arange(-10, 11, 1), 'posicao_carro')
    velocidade_carro = ctrl.Antecedent(np.arange(-10, 11, 1), 'velocidade_carro')

    forca_carro = ctrl.Consequent(np.arange(-100, 101, 1), 'forca_carro')

    angulo.automf(names=['esquerda', 'vertical', 'direita'])
    velocidade_angular.automf(names=['esquerda', 'parado', 'direita'])
    posicao_carro.automf(names=['esquerda', 'centro', 'direita'])
    velocidade_carro.automf(names=['esquerda', 'parado', 'direita'])
    
    forca_carro.automf(names=['forte_esquerda', 'fraco_esquerda', 'neutro', 'fraco_direita', 'forte_direita'])

    rules = [
        ctrl.Rule(angulo['esquerda'] & velocidade_angular['esquerda'], forca_carro['forte_direita']),
        ctrl.Rule(angulo['direita'] & velocidade_angular['direita'], forca_carro['forte_esquerda']),
        ctrl.Rule(angulo['vertical'] & velocidade_angular['parado'], forca_carro['neutro']),
        ctrl.Rule(posicao_carro['esquerda'] & velocidade_carro['direita'], forca_carro['fraco_direita']),
        ctrl.Rule(posicao_carro['direita'] & velocidade_carro['esquerda'], forca_carro['fraco_esquerda'])
    ]

    controlador = ctrl.ControlSystem(rules)
    return controlador

controlador = configurar_sistema_fuzzy()

def simular_pendulo(angulo_atual, velocidade_angular_atual, posicao_carro_atual, velocidade_carro_atual):
    simulacao = ctrl.ControlSystemSimulation(controlador)
    simulacao.input['angulo'] = angulo_atual
    simulacao.input['velocidade_angular'] = velocidade_angular_atual
    simulacao.input['posicao_carro'] = posicao_carro_atual
    simulacao.input['velocidade_carro'] = velocidade_carro_atual

    simulacao.compute()

    return simulacao.output['forca_carro']

def obter_valores_usuario():
    angulo_atual = float(input("Digite o ângulo atual do pêndulo (em graus, de -90 a 90): "))
    velocidade_angular_atual = float(input("Digite a velocidade angular atual (em graus/segundo, de -10 a 10): "))
    posicao_carro_atual = float(input("Digite a posição atual do carro (em metros, de -10 a 10): "))
    velocidade_carro_atual = float(input("Digite a velocidade atual do carro (em metros/segundo, de -10 a 10): "))

    return angulo_atual, velocidade_angular_atual, posicao_carro_atual, velocidade_carro_atual

#algoritmo genético
def inicializar_populacao(tamanho_populacao):
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = {
            'regras': random.sample(range(1, 6), k=random.randint(1, 5)),  #seleciona regras de 1 a 5
            'parametros': {
                'angulo': random.uniform(-90, 90),
                'velocidade_angular': random.uniform(-10, 10),
                'posicao_carro': random.uniform(-10, 10),
                'velocidade_carro': random.uniform(-10, 10)
            }
        }
        populacao.append(individuo)
    return populacao

def calcular_erro(angulo_atual, forca_aplicada):
    return abs(angulo_atual - forca_aplicada)

def avaliar_individuo(individuo):
    erro_total = 0
    for _ in range(100):
        angulo_atual = individuo['parametros']['angulo']
        velocidade_angular_atual = individuo['parametros']['velocidade_angular']
        posicao_carro_atual = individuo['parametros']['posicao_carro']
        velocidade_carro_atual = individuo['parametros']['velocidade_carro']

        forca_aplicada = simular_pendulo(angulo_atual, velocidade_angular_atual, posicao_carro_atual, velocidade_carro_atual)
        erro = calcular_erro(angulo_atual, forca_aplicada)
        erro_total += erro

    return erro_total / 100

def selecao(populacao):
    return sorted(populacao, key=avaliar_individuo)[:len(populacao)//2]

def crossover(pai1, pai2):
    filho = {
        'regras': pai1['regras'][:len(pai1['regras']) // 2] + pai2['regras'][len(pai2['regras']) // 2:],
        'parametros': pai1['parametros']
    }
    return filho

def mutacao(individuo):
    if random.random() < 0.1:
        individuo['parametros']['angulo'] += random.uniform(-1, 1)
    return individuo

def executar_algoritmo_genetico(tamanho_populacao, numero_geracoes):
    populacao = inicializar_populacao(tamanho_populacao)

    for _ in range(numero_geracoes):
        populacao = selecao(populacao)
        nova_populacao = []

        while len(nova_populacao) < tamanho_populacao:
            pai1, pai2 = random.sample(populacao, 2)
            filho = crossover(pai1, pai2)
            nova_populacao.append(mutacao(filho))

        populacao = nova_populacao

    melhor_individuo = min(populacao, key=avaliar_individuo)
    return melhor_individuo

if __name__ == "__main__":

    angulo_atual, velocidade_angular_atual, posicao_carro_atual, velocidade_carro_atual = obter_valores_usuario()
        
    forca_aplicada = simular_pendulo(angulo_atual, velocidade_angular_atual, posicao_carro_atual, velocidade_carro_atual)
        
    print(f"Força aplicada no carro: {forca_aplicada:.2f} N")
    print("Executando resultados genéticos...")

    melhor_individuo = executar_algoritmo_genetico(tamanho_populacao=10, numero_geracoes=20)
    print("Melhor indivíduo encontrado:")
    print(f"Ângulo: {melhor_individuo['parametros']['angulo']:.2f} graus")
    print(f"Velocidade Angular: {melhor_individuo['parametros']['velocidade_angular']:.2f} graus/segundo")
    print(f"Posição do Carro: {melhor_individuo['parametros']['posicao_carro']:.2f} metros")
    print(f"Velocidade do Carro: {melhor_individuo['parametros']['velocidade_carro']:.2f} metros/segundo")
