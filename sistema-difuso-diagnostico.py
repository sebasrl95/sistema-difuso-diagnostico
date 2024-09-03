import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definición de las variables de entrada (sintomas)
fiebre = ctrl.Antecedent(np.arange(0, 41, 1), 'fiebre')
dolor_cabeza = ctrl.Antecedent(np.arange(0, 11, 1), 'dolor_cabeza')
tos = ctrl.Antecedent(np.arange(0, 11, 1), 'tos')
nausea = ctrl.Antecedent(np.arange(0, 11, 1), 'nausea')
dolor_abdominal = ctrl.Antecedent(np.arange(0, 11, 1), 'dolor_abdominal')

# Definición de la variable de salida (diagnostico)
diagnostico = ctrl.Consequent(np.arange(0, 101, 1), 'diagnostico')

# Definición de las funciones de pertenencia para los síntomas
fiebre['leve'] = fuzz.trimf(fiebre.universe, [0, 0, 37])
fiebre['moderado'] = fuzz.trimf(fiebre.universe, [36, 37, 39])
fiebre['severo'] = fuzz.trimf(fiebre.universe, [38, 40, 40])

dolor_cabeza['leve'] = fuzz.trimf(dolor_cabeza.universe, [0, 0, 3])
dolor_cabeza['moderado'] = fuzz.trimf(dolor_cabeza.universe, [2, 5, 8])
dolor_cabeza['severo'] = fuzz.trimf(dolor_cabeza.universe, [7, 10, 10])

tos['leve'] = fuzz.trimf(tos.universe, [0, 0, 3])
tos['moderado'] = fuzz.trimf(tos.universe, [2, 5, 8])
tos['severo'] = fuzz.trimf(tos.universe, [7, 10, 10])

nausea['leve'] = fuzz.trimf(nausea.universe, [0, 0, 3])
nausea['moderado'] = fuzz.trimf(nausea.universe, [2, 5, 8])
nausea['severo'] = fuzz.trimf(nausea.universe, [7, 10, 10])

dolor_abdominal['leve'] = fuzz.trimf(dolor_abdominal.universe, [0, 0, 3])
dolor_abdominal['moderado'] = fuzz.trimf(dolor_abdominal.universe, [2, 5, 8])
dolor_abdominal['severo'] = fuzz.trimf(dolor_abdominal.universe, [7, 10, 10])

# Definición de las funciones de pertenencia para el diagnóstico
diagnostico['Saludable'] = fuzz.trimf(diagnostico.universe, [0, 0, 25])
diagnostico['Leve'] = fuzz.trimf(diagnostico.universe, [20, 40, 60])
diagnostico['Moderado'] = fuzz.trimf(diagnostico.universe, [50, 70, 90])
diagnostico['Severo'] = fuzz.trimf(diagnostico.universe, [80, 100, 100])
