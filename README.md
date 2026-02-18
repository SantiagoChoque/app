# App.py

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red) ![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen) ![PRs](https://img.shields.io/badge/PRs-Welcome-orange)

# 📊 Sistema de Actividad Financiera 

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
### 📂 Desglose de los Módulos del Proyecto

#### 🏠 Home (Panel Principal)
* **Vista General:** Presenta los objetivos del proyecto y datos generales.

#### 📕 Ejercicio 1: Variables y Condicionales
* **Lógica de Comparación:** Implementación de un verificador simple de presupuesto.
* **Control de Flujo:** Uso de estructuras `if-else` para comparar montos y determinar si existe un excedente o déficit de dinero en tiempo real.

#### 📗 Ejercicio 2: Listas y Diccionarios
* **Estructuras de Datos:** Registro de múltiples actividades financieras mediante diccionarios almacenados en listas.
* **Integración con Pandas:** Conversión de datos en un `DataFrame` para una visualización tabular profesional.
* **Persistencia:** Uso de `st.session_state` para mantener la tabla de datos actualizada durante la navegación.

#### 📘 Ejercicio 3: Funciones y Programación Funcional
* **Cálculo de Retorno:** Implementación de funciones para proyectar el retorno esperado basado en interés simple.
* **Optimización de Código:** Uso de **expresiones Lambda** y la función **Map** para procesar listas de datos de manera eficiente.

#### 📙 Ejercicio 4: Programación Orientada a Objetos (POO)
* **Paradigma de Clases:** Modelado del sistema financiero mediante la clase `Actividad`.
* **Encapsulamiento:** Cada actividad es un objeto con sus propios atributos y métodos (como `esta_en_presupuesto` y `mostrar_info`).
* **Modularidad:** Demuestra cómo organizar código complejo de forma escalable y mantenible.

# 🛠️ Instrucciones de Uso

## Clonar Repositorio:
```bash
git clone [https://github.com/SantiagoChoque/app.git](https://github.com/SantiagoChoque/app.git)
cd app
```

## Instalar dependencias
```bash
pip install -r requirements.txt

```
## Ejecutar aplicación
```bash
streamlit run app.py
```
## ✏️Autor: Santiago Gabriel Choque Fernández
* Repositorio GitHub: [https://github.com/SantiagoChoque/app/](https://github.com/SantiagoChoque/app/)
* Aplicación en Streamlit Cloud: [https://app-santiagochoque.streamlit-app](https://app-santiagochoque.streamlit.app)
* Correo: sgchoquefer@gmail.com
* Año: 2026


