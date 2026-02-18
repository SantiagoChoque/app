import streamlit as st 
import pandas as pd 

ejercicios = ["🏠 Home", "📕 Ejercicio 1:", "📗 Ejercicio 2:", "📘 Ejercicio 3:", "📙 Ejercicio 4:"]
st.sidebar.image("img/DMC.png")
st.sidebar.title("Navegación: ",text_alignment="left")
pagina = st.sidebar.selectbox("Elija el ejercicio: ", ejercicios)
#------------------------------------------------------------------------------------------------------------------------------
if pagina == "🏠 Home":
    st.title("Proyecto Final, Python Fundamentals:", text_alignment="center")
    st.divider()
    st.subheader("📚 Ejercicios realizados: ")
    col1,col2=st.columns(2)
    with col1:
        with st.container(border=True):
            st.info("📕 **Ejercicio 1:** Variables y Condicionales")
        with st.container(border=True):
            st.info ("📘 **Ejercicio 3:** Funciones y Programación Funcional")

    with col2:
        with st.container(border=True):
            st.info("📗 **Ejercicio 2:** Listas y Diccionarios\n ")
        with st.container(border=True):
            st.info ("📙 **Ejercicio 4:** Progamación Orientada a Objetos (POO)")
    
    st.divider()
    
    st.subheader("🌐 Descripción de la Aplicación:")
    
    st.write("""La presente aplicación ha sido desarrollada como parte del Módulo 1 del curso ofrecido 
        por DMC Python Fundamentals de la Especialización en Python for Analytics.
        """)
    
    st.write("""🎯 El objetivo principal de esta aplicación es construir una herramienta utilizando como tecnologías
            principales Python y Streamlit para demostrar el dominio de los pilares de la programación en 4 módulos.
        """)
    
    st.subheader("📕 Ejercicio 1:")
    
    st.write("""Este módulo presenta un verificador simple para la gestión de presupuestos
        utilizando **variables y condicionales** donde el usuario puede ingresar un presupuesto
        y un gasto y el sistema los compara, para mostrar el exceso o la falta de dinero""")
    
    st.subheader("📗 Ejercicio 2:")
    
    st.write("""En el segundo módulo se programó una estructura que nos permite registrar actividades
        financieras utilizando **diccionarios y listas**. Para la visualización del **data frame**
        generado por el registro se utilizó la librería **Pandas**""")
    
    st.subheader("📘 Ejercicio 3:")
    
    st.write("""El siguiente módulo consta de una optimización de cálculos para un retorno esperado utilizando
        la fórmula del interés simple, expresado a través de **funciones, expresiones lambda y programación funcional con map**
        """)
    
    st.subheader("📙 Ejercicio 4:")
    
    st.write("""Por último el módulo 4 evidencia el Modelado de sistemas bajo el paradigma de la **Programación Orientada a Objetos (POO)
        permitiendo una organización de código modular y escalable.
        """)
    
    
    st.divider()
    
    st.subheader("📝 Datos del trabajo:  ")
    st.write("**Nombre del estudiante:** Santiago Gabriel Choque Fernández")
    st.write("**Nombre del módulo:** Python Fundamentals")
    st.write("**Año:** 2026")
    st.write("**Tecnologías utilizadas:** Python, Streamlit, Pandas") 
    
    st.divider()
    
    st.subheader("🦾 Tecnologías utilizadas")
    
    col1,col2,col3=st.columns(3)
    with col1:
        st.image("img/PYTHON.png", caption="Python")
    with col2:
        st.image("img/STREAMLIT.png",caption="Streamlit")
    with col3:
        st.image("img/PANDAS.png", caption="Pandas")
    st.divider()

#------------------------------------------------------------------------------------------------------------------------------
if pagina == "📕 Ejercicio 1:":
    st.title("📕 **Ejercicio 1:**")
    st.divider()
    st.write("""
        Este módulo sirve para realizar una comparación rápida y única entre un monto de dinero disponible y un gasto planeado.
        
        Qué hacer:
        
        Ingresa el monto total de tu presupuesto.
        
        Ingresa el valor del gasto que deseas realizar.
        
        Haz clic en "Ejecutar".
        
        Resultado: El sistema te mostrará con un mensaje de color si estás dentro del límite o si te has excedido, indicando exactamente cuánto dinero sobra o falta.    

        """)
    st.divider()
    st.subheader("🧮 Comparación presupuesto vs gasto: ")
    col1,col2=st.columns(2)
    with col1:
        presupuesto = st.number_input("💚 Ingrese el presupuesto destinado: ", min_value=0.0)
    with col2:
        gasto = st.number_input("❌ Ingrese el gasto a realizar: ", min_value=0.0)
    
    if st.button("Ejecutar"):
        if presupuesto >= gasto:
            st.success("Esta usted dentro del presupuesto")
            st.write("Le quedan", presupuesto-gasto)
        else:
            st.warning("El presupuesto fue excedido")
            st.write("Faltan", round(gasto-presupuesto,2))
    st.divider()
#------------------------------------------------------------------------------------------------------------------------------
if pagina == "📗 Ejercicio 2:":

    
    st.title("📗 **Ejercicio 2:**")
    st.divider()
    
    st.write("""
        Aquí puedes gestionar múltiples gastos e ingresos de forma organizada.
        
        Qué hacer:
        
        Escribe el nombre y selecciona el tipo de actividad (Ingreso o Gasto).
        
        Define el presupuesto asignado y el gasto real efectuado.
        
        Presiona "Agregar actividades" para guardarla en la tabla.
        
        Resultado: Verás una tabla con todas tus actividades registradas y un análisis de cumplimiento para cada una.
        """)
    
    
    st.divider()
    st.subheader("Ingresa los datos: ")
    col1,col2=st.columns(2)
    with col1:
        nombre = st.text_input("Ingrese el nombre de la actividad: ")
        tipo = st.selectbox("Ingrese el tipo de actividad: ", ["📈Ingreso","📉Gasto"])
    with col2:
        presupuesto1 = st.number_input("Ingrese el presupuesto asignado de la actividad: ", min_value=0.0)
        gasto1 = st.number_input("Ingrese el gasto de la actividad: ", min_value=0.0)

    if "actividades" not in st.session_state:
        st.session_state.actividades = []
        st.info("👇 Comieza por añadir actividades: ")

        
    if st.button("Agregar actividades: "):
        if presupuesto1 >= gasto1:
            diccionario = {"Nombre": nombre, "Tipo": tipo, "Presupuesto": presupuesto1, "Gasto Real": gasto1}
            st.session_state.actividades.append(diccionario)
            st.success("Actividad agregada, esta dentro del presupuesto.")
            st.divider()
            st.subheader("Datos de la actividad: ")
            col1,col2,col3=st.columns(3)
            with col1:
                st.write("**Nombre de la actividad:** ", diccionario["Nombre"])
                st.write("**Tipo:** ", diccionario["Tipo"]) 
                st.write("**Prespuesto:** ", diccionario["Presupuesto"])
                st.write("**Gasto:** ", diccionario["Gasto Real"])
            with col2:
                st.subheader("**Estado**: ✅ Cumple")
            with col3:
                st.write("Sobran: ")
                st.write(diccionario["Presupuesto"]-diccionario["Gasto Real"])
        else:
            diccionario = {"Nombre": nombre, "Tipo": tipo, "Presupuesto": presupuesto1, "Gasto Real": gasto1}
            st.warning("Está usted fuera del presupuesto, actividad agregada")
            st.session_state.actividades.append(diccionario)
            st.subheader("Datos de la actividad: ")
            col1,col2,col3=st.columns(3)
            with col1:
                st.write("**Nombre de la actividad:** ", diccionario["Nombre"])
                st.write("**Tipo:** ", diccionario["Tipo"]) 
                st.write("**Prespuesto:** ", diccionario["Presupuesto"])
                st.write("**Gasto:** ", diccionario["Gasto Real"])
            with col2:
                st.subheader("**Estado**: ❌ No Cumple")
            with col3:
                st.write("Faltan: ")
                st.write(diccionario["Gasto Real"]-diccionario["Presupuesto"])            


    if st.session_state.actividades:
        st.subheader("Visualización de datos: ")
        df = pd.DataFrame(st.session_state.actividades)
        st.dataframe(df,hide_index=True, column_config={
        "Presupuesto": st.column_config.NumberColumn(format="S/. %.2f"),
        "Gasto Real": st.column_config.NumberColumn(format="S/. %.2f")})
        
        if st.button("🚮 Eliminar actividades:"):
            st.session_state.actividades=[]
            st.rerun()
    st.divider()
        
#------------------------------------------------------------------------------------------------------------------------------
if pagina == "📘 Ejercicio 3:":
    st.title("📘 **Ejercicio 3:**")
    st.divider()
    
    st.write("""
        Este módulo utiliza programación funcional (map y lambda) para proyectar cuánto dinero podrías obtener de tus actividades en un tiempo determinado.
        
        Qué hacer:
        
        Ingresa el nombre de la actividad y su presupuesto base.
        
        Define una tasa de retorno (porcentaje) y la cantidad de meses.
        
        Haz clic en el botón de cálculo.
        
        Resultado: El sistema aplicará la fórmula Presupuesto * Tasa * Meses a todas las actividades de tu lista y mostrará el retorno esperado
        """)
    
    
    st.divider()
    st.header("📊 Cálculo de retorno esperado:")
    st.subheader("Ingresar nueva actividad:  ")
    
    nombre = st.text_input("Nombre de la actividad: ")
    col1,col2,col3=st.columns(3)
    with col1:
        presupuesto = st.number_input("Presupuesto (S/.)", min_value=0.00, value=1000.00)
    with col2:
        tasa=st.number_input("Tasa (%)", min_value=0.00, value=5.00)
    with col3:
        meses=st.number_input("Meses", min_value=0,value=12)
    st.divider()
    
    def retorno(presupuesto, tasa, meses):
        resultado= presupuesto * tasa/100 * meses
        return resultado
    
    if "lista" not in st.session_state:
        st.session_state.lista = []
        st.info("👇 Comieza por añadir actividades")
        
    if st.button("Agregar actividad: "):
        diccionario={"Nombre": nombre, "Presupuesto": presupuesto, "Tasa (%)":tasa, "Meses": meses}
        st.session_state.lista.append(diccionario)
        st.success("Cálculo realizado")
        st.write("Actividad Agregada: ", nombre)
    
    if st.session_state.lista:        
        lista_con_retorno = list(map(lambda x: {
            **x, 
            "Retorno Esperado": retorno(x["Presupuesto"], x["Tasa (%)"], x["Meses"])
            }, st.session_state.lista))
        
        
        df = pd.DataFrame(lista_con_retorno)
        st.dataframe(df,hide_index=True, column_config={
        "Presupuesto": st.column_config.NumberColumn(format="S/. %.2f"),
        "Tasa (%)": st.column_config.NumberColumn(format="%.2f%%"),
        "Retorno Esperado": st.column_config.NumberColumn(format="S/. %.2f")})

    if st.session_state.lista:
        if st.button("🚮 Eliminar actividades:"):
            st.session_state.lista=[]
            st.rerun()
    st.divider()  
        
#------------------------------------------------------------------------------------------------------------------------------
if pagina == "📙 Ejercicio 4:":
    st.title("📙 **Ejercicio 4:**")
    st.divider()
    
    st.write(""" 
        Este es el nivel más avanzado, donde cada actividad se convierte en un objeto con sus propias reglas y métodos.
        
        Qué hacer:
        
        Completa los datos de la actividad (nombre, tipo, presupuesto y gasto real).
        
        Presiona "Agregar Actividad".
        
        Resultado: El programa instanciará una clase llamada Actividad y usará el método mostrar_info() para imprimir un resumen estilizado de cada objeto creado.  
        """)
    
    
    st.divider()
    st.subheader("Sistema de Actividad Financiera: ")
    nombre = st.text_input("Nombre: ")
    tipo = st.selectbox("Ingrese el tipo de actividad: ", ["📈Ingreso","📉Gasto"])

    col1, col2 = st.columns(2)
    with col1:
        presupuesto = st.number_input("Presupuesto (S/.)", min_value=0.0)
    with col2:
        gasto = st.number_input("Gasto Real (S/.)", min_value=0.0)

    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto = gasto_real
        
        def esta_en_presupuesto(self):
            return self.gasto <= self.presupuesto
    
        def mostrar_info(self):
            if self.esta_en_presupuesto():
                estado = "✅ Dentro" 
            else:
                estado = "❌ Excedido"
            return f"**{self.nombre}** ({self.tipo}) | Presupuesto: S/.{self.presupuesto} | Gasto: S/.{self.gasto} | Estado: {estado}"
    
    if "objetos" not in st.session_state:
        st.session_state.objetos = []
        st.info("👇 Comienza por añadir actividades")

    if st.button("Agregar Actividad"):
        objeto = Actividad(nombre, tipo, presupuesto, gasto)
        st.session_state.objetos.append(objeto)
        st.success("¡Actividad guardada!")
        
    st.divider()
    if st.session_state.objetos:
        st.write("### Lista de Actividades:")
        for i in st.session_state.objetos:
            st.info(i.mostrar_info())
        if st.button("🚮 Eliminar actividades:"):
            st.session_state.objetos=[]
            st.rerun()



