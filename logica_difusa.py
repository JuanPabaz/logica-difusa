import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# El objetivo es controlar la temperatura del aire acondicionado en función de la temperatura ambiente y la humedad.

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Sistema de Control Difuso para la Temperatura del Aire Acondicionado")

# Variables para los valores de entrada
room_temperature_var = tk.DoubleVar()
humidity_var = tk.DoubleVar()
result_var = tk.StringVar()

# Definir las variables lingüísticas
room_temperature = ctrl.Antecedent(np.arange(15, 41, 1), 'room_temperature')  # Temperatura ambiente de 15°C a 40°C
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')  # Humedad de 0% a 100%
ac_temperature = ctrl.Consequent(np.arange(16, 31, 1), 'ac_temperature')  # Temperatura del AC de 16°C a 30°C

# Funciones de membresía para la temperatura ambiente
room_temperature['cold'] = fuzz.trapmf(room_temperature.universe, [15, 15, 18, 22])
room_temperature['comfortable'] = fuzz.trapmf(room_temperature.universe, [20, 22, 26, 28])
room_temperature['hot'] = fuzz.trapmf(room_temperature.universe, [26, 30, 40, 40])

# Funciones de membresía para la humedad
humidity['low'] = fuzz.trapmf(humidity.universe, [0, 0, 20, 40])
humidity['medium'] = fuzz.trapmf(humidity.universe, [30, 40, 60, 70])
humidity['high'] = fuzz.trapmf(humidity.universe, [60, 80, 100, 100])

# Funciones de membresía para la temperatura del aire acondicionado
ac_temperature['cold'] = fuzz.trimf(ac_temperature.universe, [16, 16, 22])
ac_temperature['moderate'] = fuzz.trimf(ac_temperature.universe, [20, 24, 26])
ac_temperature['warm'] = fuzz.trimf(ac_temperature.universe, [24, 30, 30])

# Reglas difusas

# Definimos las reglas de razonamiento que controlan el sistema.
# Por ejemplo, si la temperatura ambiente es alta o la humedad es alta, la temperatura del AC debe ser fría.

rule1 = ctrl.Rule(room_temperature['cold'] & humidity['low'], ac_temperature['warm'])
rule2 = ctrl.Rule(room_temperature['comfortable'] & humidity['medium'], ac_temperature['moderate'])
rule3 = ctrl.Rule(room_temperature['hot'] | humidity['high'], ac_temperature['cold'])

# Reglas adicionales para mayor precisión
rule4 = ctrl.Rule(room_temperature['cold'] & humidity['medium'], ac_temperature['moderate'])
rule5 = ctrl.Rule(room_temperature['comfortable'] & humidity['low'], ac_temperature['moderate'])
rule6 = ctrl.Rule(room_temperature['comfortable'] & humidity['high'], ac_temperature['cold'])

# Crear el sistema de control difuso
ac_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
ac_sim = ctrl.ControlSystemSimulation(ac_ctrl)

# Función para ejecutar la simulación con los valores proporcionados por el usuario
def simulate():
    try:
        room_temperature_value = room_temperature_var.get()
        humidity_value = humidity_var.get()

        # Verificar que los valores estén dentro del rango permitido
        if 15 <= room_temperature_value <= 40 and 0 <= humidity_value <= 100:
            # Proporcionar los valores de entrada
            ac_sim.input['room_temperature'] = room_temperature_value
            ac_sim.input['humidity'] = humidity_value

            # Ejecutar la simulación
            ac_sim.compute()
            
            # Mostrar el resultado
            result_var.set(f"Temperatura recomendada del AC: {ac_sim.output['ac_temperature']:.2f}°C")

            # Visualizar la salida de temperatura después de la defuzificación
            ac_temperature.view(sim=ac_sim)
            plt.show()
        else:
            messagebox.showerror("Error", "La temperatura debe estar entre 15°C y 40°C, y la humedad entre 0% y 100%.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        
# Función para reiniciar los valores
def reset():
    room_temperature_var.set(20)
    humidity_var.set(50)
    result_var.set("")

# Crear los paneles
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

frame1.grid(row=0, column=0, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)

# Panel 1: Visualización de las funciones de membresía
tk.Label(frame1, text="Funciones de Membresía").grid(row=0, column=0, columnspan=2)

def plot_memberships():
    room_temperature.view()
    humidity.view()
    ac_temperature.view()
    plt.show()

tk.Button(frame1, text="Mostrar Rangos", command=plot_memberships).grid(row=1, column=0, columnspan=2)

# Panel 2: Entrada del usuario y resultado
tk.Label(frame2, text="Temperatura Ambiente (°C)").grid(row=0, column=0)
tk.Entry(frame2, textvariable=room_temperature_var).grid(row=0, column=1)

tk.Label(frame2, text="Humedad (%)").grid(row=1, column=0)
tk.Entry(frame2, textvariable=humidity_var).grid(row=1, column=1)

tk.Button(frame2, text="Simular", command=simulate).grid(row=2, column=0)
tk.Button(frame2, text="Resetear", command=reset).grid(row=2, column=1)

tk.Label(frame2, textvariable=result_var).grid(row=3, columnspan=2)

# Iniciar la aplicación
root.mainloop()