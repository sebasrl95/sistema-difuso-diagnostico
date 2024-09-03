import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear las variables difusas
sintomas = ctrl.Antecedent(np.arange(0, 11, 1), 'sintomas')
diagnostico = ctrl.Consequent(np.arange(0, 11, 1), 'diagnostico')

# Definir las funciones de membresía para síntomas
sintomas['bajo'] = fuzz.trimf(sintomas.universe, [0, 0, 5])
sintomas['medio'] = fuzz.trimf(sintomas.universe, [0, 5, 10])
sintomas['alto'] = fuzz.trimf(sintomas.universe, [5, 10, 10])

# Definir las funciones de membresía para diagnóstico
diagnostico['gripe'] = fuzz.trimf(diagnostico.universe, [0, 0, 5])
diagnostico['resfriado'] = fuzz.trimf(diagnostico.universe, [0, 5, 10])
diagnostico['migraña'] = fuzz.trimf(diagnostico.universe, [0, 5, 10])
diagnostico['saludable'] = fuzz.trimf(diagnostico.universe, [5, 10, 10])
# Añadir más diagnósticos según sea necesario

# Definir las reglas difusas
regla1 = ctrl.Rule(sintomas['alto'], diagnostico['gripe'])
regla2 = ctrl.Rule(sintomas['medio'], diagnostico['resfriado'])
regla3 = ctrl.Rule(sintomas['bajo'], diagnostico['saludable'])
# Añadir más reglas según sea necesario

# Crear el sistema de control difuso
diagnostico_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])
diagnostico_simulador = ctrl.ControlSystemSimulation(diagnostico_ctrl)

# Proporcionar datos de entrada
def diagnosticar(fiebre, dolor_cabeza, tos, estornudos, nausea, vomito, diarrea, mareo, falta_aire, dolor_oido, perdida_audicion, dolor_pecho, dolor_abdominal, ardor_estomago, picazon_ojo, nariz_congestionada, perdida_olfato, perdida_gusto, congestion_nasal, dolor_facial, palpitaciones, perdida_equilibrio):
    sintomas_input = {
        'fiebre': fiebre,
        'dolor_cabeza': dolor_cabeza,
        'tos': tos,
        'estornudos': estornudos,
        'nausea': nausea,
        'vomito': vomito,
        'diarrea': diarrea,
        'mareo': mareo,
        'falta_aire': falta_aire,
        'dolor_oido': dolor_oido,
        'perdida_audicion': perdida_audicion,
        'dolor_pecho': dolor_pecho,
        'dolor_abdominal': dolor_abdominal,
        'ardor_estomago': ardor_estomago,
        'picazon_ojo': picazon_ojo,
        'nariz_congestionada': nariz_congestionada,
        'perdida_olfato': perdida_olfato,
        'perdida_gusto': perdida_gusto,
        'congestion_nasal': congestion_nasal,
        'dolor_facial': dolor_facial,
        'palpitaciones': palpitaciones,
        'perdida_equilibrio': perdida_equilibrio
    }

    sintoma_total = np.mean(list(sintomas_input.values()))

    # Establecer las entradas
    diagnostico_simulador.input['sintomas'] = sintoma_total

    # Ejecutar la simulación
    diagnostico_simulador.compute()

    # Obtener los resultados
    return diagnostico_simulador.output['diagnostico']

# Ejemplo de uso
resultado = diagnosticar(8, 6, 7, 2, 1, 0, 0, 3, 5, 0, 1, 4, 2, 0, 0, 1, 0, 0, 0, 1, 2)

# Visualización
# Graficar las funciones de membresía
fig, ax = plt.subplots(figsize=(10, 8))

# Graficar síntomas
ax.plot(sintomas.universe, sintomas['bajo'], label='Bajo', color='blue')
ax.plot(sintomas.universe, sintomas['medio'], label='Medio', color='green')
ax.plot(sintomas.universe, sintomas['alto'], label='Alto', color='red')

# Graficar diagnóstico
ax.plot(diagnostico.universe, diagnostico['gripe'], label='Gripe', color='cyan', linestyle='--')
ax.plot(diagnostico.universe, diagnostico['resfriado'], label='Resfriado', color='magenta', linestyle='--')
ax.plot(diagnostico.universe, diagnostico['migraña'], label='Migraña', color='yellow', linestyle='--')
ax.plot(diagnostico.universe, diagnostico['saludable'], label='Saludable', color='black', linestyle='--')

# Configurar gráficos
ax.set_title('Sistema Difuso de Diagnóstico Médico')
ax.set_xlabel('Grado de Síntoma')
ax.set_ylabel('Grado de Membresía')
ax.legend(loc='upper right')

# Mostrar gráfico
plt.show()
