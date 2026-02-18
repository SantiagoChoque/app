# App.py

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red) ![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen) ![PRs](https://img.shields.io/badge/PRs-Welcome-orange)

# 📊 Sistema de Actividad Financiera - Ingeniería Industrial

Este proyecto consiste en una aplicación interactiva desarrollada en **Python** utilizando **Streamlit**. La aplicación permite la gestión y el seguimiento de presupuestos para diversas actividades financieras, facilitando la visualización del estado de gasto frente al presupuesto asignado.

## 🚀 Características

* **Gestión de Actividades**: Permite añadir nombres de actividades, tipos de gasto y montos presupuestados.
* **Control de Gasto Real**: Calcula automáticamente si una actividad se encuentra "Dentro" o "Excedida" del presupuesto asignado.
* **Interfaz Interactiva**: Construida con Streamlit para una navegación fluida y visualización de datos en tiempo real.
* **Programación Orientada a Objetos**: El sistema utiliza clases en Python para estructurar la lógica de las actividades financieras.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 🐍
* **Framework Web:** Streamlit
* **Gestión de Datos:** Pandas
* **Entorno de Despliegue:** Streamlit Cloud / GitHub

## 📂 Estructura del Proyecto

```text
📦 app
 ┣ 📂 .streamlit         # Configuración de tema y despliegue
 ┃ ┗ 📜 config.toml
 ┣ 📂 img                # Recursos visuales (Logos de Python, Pandas, etc.)
 ┣ 📜 app.py             # Archivo principal de la aplicación
 ┣ 📜 requirements.txt   # Dependencias del proyecto
 ┗ 📜 README.md          # Documentación
```
### 📂 Desglose de Ejercicios

Este repositorio contiene el desarrollo práctico del curso, organizado de la siguiente manera:

#### 📝 Ejercicio 1: Fundamentos de Python
* **Lógica Básica:** Implementación de estructuras de control (if/else, bucles) para resolución de problemas matemáticos simples.
* **Manejo de Variables:** Uso de tipos de datos básicos y operaciones aritméticas aplicadas a casos de estudio.

#### 📈 Ejercicio 2: Cadenas de Markov (Proyecto Industrial)
* **Análisis de Mercado:** Modelado estocástico para determinar el *market share* de instituciones educativas.
* **Matrices de Transición:** Cálculo de probabilidades de estado estable para predecir comportamientos futuros del sistema.

#### 🛠️ Ejercicio 3: Estructuras de Datos y Listas
* **Gestión de Información:** Uso de listas y diccionarios para organizar datos de producción.
* **Filtros de Datos:** Implementación de funciones para buscar y filtrar información específica dentro de colecciones de datos.

#### 📙 Ejercicio 4: Sistema de Actividad Financiera
* **Programación Orientada a Objetos (POO):** Creación de la clase `Actividad` para encapsular datos y comportamiento financiero.
* **Control Presupuestal:** Interfaz interactiva en Streamlit que permite agregar actividades y validar si el gasto real está dentro del presupuesto.
* **Persistencia de Datos:** Implementación de `st.session_state` para mantener la lista de actividades actualizada sin perder datos al recargar la página.



## 🛠️ Instrucciones de Uso

# Clonar Repositorio:
```bash
git clone [https://github.com/SantiagoChoque/app.git](https://github.com/SantiagoChoque/app.git)
cd app
```

# Instalar dependencias
```bash
pip install -r requirements.txt

```
# Ejecutar aplicación
```bash
streamlit run app.py
```
Autor: Santiago Gabriel Choque Fernández

Año: 2026


