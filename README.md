# Sistema Experto de Recomendación de Libros

Este es un sistema de control difuso que ajusta la temperatura recomendada del aire acondicionado en función de la **temperatura ambiente** y la **humedad relativa**.  
El sistema utiliza lógica difusa para imitar el razonamiento humano y ofrece una interfaz gráfica para la interacción con el usuario.

## Requisitos Previos

- Python 3.10 o superior
- Homebrew (solo para macOS, en caso de instalar Tkinter)

## Instalación

1. **Instalar tkinter (solo en macOS):**
   ```bash
   brew install python-tk
   ```

2. **Crear entorno virtual:**
   ```bash
   python3 -m venv venv
   ```

3. **Activar entorno virtual:**
   ```bash
   source venv/bin/activate
   ```

4. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Activar el entorno virtual (si no está activado):**
   ```bash
   source venv/bin/activate
   ```

2. **Ejecutar el programa:**
   ```bash
   python se_quiz.py
   ```

3. **Usar la interfaz gráfica:**
- Ingresa la temperatura ambiente (15°C – 40°C).
- Ingresa la humedad relativa (0% – 100%).
- Haz clic en Simular para obtener la temperatura recomendada del aire acondicionado.
- Haz clic en Mostrar Rangos para visualizar las funciones de membresía.
- Haz clic en Resetear para reiniciar los valores.

## Características

- Sistema de lógica difusa con reglas personalizadas.
- Interfaz gráfica amigable con Tkinter.
- Visualización de funciones de membresía y resultados con Matplotlib.
- Entradas configurables:
 - Temperatura ambiente
 - Humedad relativa
- Salida: Temperatura recomendada del aire acondicionado.

## Tecnologías Utilizadas

- **Python 3.10+**
- **Numpy: Cálculos numéricos.**
- **scikit-fuzzy: Motor de lógica difusa.**
- **Matplotlib: Visualización de funciones y resultados.**
- **Tkinter: Interfaz gráfica de usuario.**
