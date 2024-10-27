import numpy as np
import skfuzzy as fuzz 
from skfuzzy import control as ctrl

angulo = ctrl.Antecedent(np.arange(-90, 91, 1), 'angulo')
velocidade_angular = ctrl.Antecedent(np.arange(-10, 11, 1), 'velocidade_angular')
posicao_carro = ctrl.Antecedent(np.arange(-10, 11, 1), 'posicao_carro')
velocidade_carro = ctrl.Antecedent(np.arange(-10, 11, 1), 'velocidade_carro')

#força a ser aplicada no carro (em Newtons)
forca_carro = ctrl.Consequent(np.arange(-100, 101, 1), 'forca_carro')

#pertinência para o ângulo (em graus)
angulo['esquerda'] = fuzz.trimf(angulo.universe, [-90, -45, 0])
angulo['vertical'] = fuzz.trimf(angulo.universe, [-10, 0, 10])
angulo['direita'] = fuzz.trimf(angulo.universe, [0, 45, 90])

#pertinência para a velocidade angular (em graus/segundo)
velocidade_angular['esquerda'] = fuzz.trimf(velocidade_angular.universe, [-10, -5, 0])
velocidade_angular['parado'] = fuzz.trimf(velocidade_angular.universe, [-2, 0, 2])
velocidade_angular['direita'] = fuzz.trimf(velocidade_angular.universe, [0, 5, 10])

#pertinência para a posição do carro (em metros)
posicao_carro['esquerda'] = fuzz.trimf(posicao_carro.universe, [-10, -5, 0])
posicao_carro['centro'] = fuzz.trimf(posicao_carro.universe, [-1, 0, 1])
posicao_carro['direita'] = fuzz.trimf(posicao_carro.universe, [0, 5, 10])

#pertinência para a velocidade do carro (em metros/segundo)
velocidade_carro['esquerda'] = fuzz.trimf(velocidade_carro.universe, [-10, -5, 0])
velocidade_carro['parado'] = fuzz.trimf(velocidade_carro.universe, [-1, 0, 1])
velocidade_carro['direita'] = fuzz.trimf(velocidade_carro.universe, [0, 5, 10])

#pertinência para a força aplicada no carro (em Newtons)
forca_carro['forte_esquerda'] = fuzz.trimf(forca_carro.universe, [-100, -50, 0])
forca_carro['fraco_esquerda'] = fuzz.trimf(forca_carro.universe, [-50, -25, 0])
forca_carro['neutro'] = fuzz.trimf(forca_carro.universe, [-10, 0, 10])
forca_carro['fraco_direita'] = fuzz.trimf(forca_carro.universe, [0, 25, 50])
forca_carro['forte_direita'] = fuzz.trimf(forca_carro.universe, [0, 50, 100])

rule1 = ctrl.Rule(angulo['esquerda'] & velocidade_angular['esquerda'], forca_carro['forte_direita'])
rule2 = ctrl.Rule(angulo['direita'] & velocidade_angular['direita'], forca_carro['forte_esquerda'])
rule3 = ctrl.Rule(angulo['vertical'] & velocidade_angular['parado'], forca_carro['neutro'])
rule4 = ctrl.Rule(posicao_carro['esquerda'] & velocidade_carro['direita'], forca_carro['fraco_direita'])
rule5 = ctrl.Rule(posicao_carro['direita'] & velocidade_carro['esquerda'], forca_carro['fraco_esquerda'])

controlador = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
simulacao = ctrl.ControlSystemSimulation(controlador)

def simular_pendulo(angulo_atual, velocidade_angular_atual, posicao_carro_atual, velocidade_carro_atual):
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

if __name__ == "__main__":
    while True:
        angulo_atual, velocidade_angular_atual, posicao_carro_atual, velocidade_carro_atual = obter_valores_usuario()
        
        forca_aplicada = simular_pendulo(angulo_atual, velocidade_angular_atual, posicao_carro_atual, velocidade_carro_atual)
        
        print(f"Força aplicada no carro: {forca_aplicada:.2f} N")

        continuar = input("Deseja realizar outra simulação? (s/n): ")
        if continuar.lower() != 's':
            break