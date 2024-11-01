import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

x_input = ctrl.Antecedent(np.arange(0, 11, 1), 'input')
y_output = ctrl.Consequent(np.arange(0, 11, 1), 'output')

x_input['low'] = fuzz.trimf(x_input.universe, [0, 0, 5])
x_input['medium'] = fuzz.trimf(x_input.universe, [0, 5, 10])
x_input['high'] = fuzz.trimf(x_input.universe, [5, 10, 10])

y_output['low'] = fuzz.trimf(y_output.universe, [0, 0, 5])
y_output['medium'] = fuzz.trimf(y_output.universe, [0, 5, 10])
y_output['high'] = fuzz.trimf(y_output.universe, [5, 10, 10])

#regras fuzzy
rule1 = ctrl.Rule(x_input['low'], y_output['low'])
rule2 = ctrl.Rule(x_input['medium'], y_output['medium'])
rule3 = ctrl.Rule(x_input['high'], y_output['high'])

control_system = ctrl.ControlSystem([rule1, rule2, rule3])
control_simulation = ctrl.ControlSystemSimulation(control_system)

#dados para treinamento da rede neural
inputs = np.random.uniform(0, 10, 100)
outputs = []

for inp in inputs:
    control_simulation.input['input'] = inp
    control_simulation.compute()
    outputs.append(control_simulation.output['output'])

#treinando a MLP com dados fuzzy
mlp = MLPRegressor(hidden_layer_sizes=(5,), max_iter=1000)
mlp.fit(inputs.reshape(-1, 1), outputs)

#testando o sistema NF e comparando com as saídas do fuzzy
test_inputs = np.random.uniform(0, 10, 20)
predicted_outputs = mlp.predict(test_inputs.reshape(-1, 1))

fuzzy_outputs = []
for inp in test_inputs:
    control_simulation.input['input'] = inp
    control_simulation.compute()
    fuzzy_outputs.append(control_simulation.output['output'])

plt.scatter(test_inputs, predicted_outputs, color='red', label='MLP Outputs')
plt.scatter(test_inputs, fuzzy_outputs, color='blue', label='Fuzzy Outputs')
plt.title('Neuro-Fuzzy System Output Comparison')
plt.xlabel('Input')
plt.ylabel('Output')
plt.legend()
plt.show()
