# 💰 Ciclo de Conversión de Efectivo (CCC)

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.17%2B-3F4F75?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Descripción General

Este proyecto es una herramienta educativa interactiva desarrollada en **Python** utilizando **Streamlit**. Su propósito principal es ilustrar de manera visual y pedagógica cómo funciona el **Ciclo de Conversión de Efectivo (CCC)**, una métrica financiera fundamental para entender la gestión de liquidez de una empresa.

La aplicación permite a los usuarios (estudiantes, profesionales o interesados) manipular variables clave y observar en tiempo real cómo estas afectan el ciclo financiero, visualizando los resultados tanto numéricamente como a través de gráficos dinámicos.

---

## ✨ Características Principales

*   **🎛️ Simulación Interactiva**: Controles deslizantes (*sliders*) para ajustar:
    *   **Días de Inventario (DI)**: Tiempo promedio de permanencia del inventario.
    *   **Días de Cuentas por Cobrar (DCC)**: Tiempo promedio de cobro a clientes.
    *   **Días de Cuentas por Pagar (DCP)**: Tiempo promedio de pago a proveedores.
*   **⚡ Cálculo en Tiempo Real**: Determinación automática del CCC basado en la fórmula `CCE = DI + DCC - DCP`.
*   **🧠 Feedback Visual e Interpretativo**:
    *   Métricas con colores condicionales (Rojo para avisos, Verde para escenarios favorables).
    *   Explicaciones contextuales sobre si el efectivo está "amarrado" o si existe financiamiento operativo.
*   **📊 Visualización Gráfica Avanzada**: Gráfico de barras horizontales (tipo Gantt) construido con **Plotly** que desglosa visualmente cómo se suman y restan los componentes del ciclo.
*   **🎨 Diseño Premium**: Interfaz moderna en modo oscuro, optimizada para la legibilidad y el enfoque en los datos.

---

## 🛠️ Requisitos Técnicos

Para ejecutar este proyecto localmente, necesitarás:

*   **Python**: Versión 3.8 o superior.
*   **Librerías**:
    *   `streamlit` (Framework de la aplicación)
    *   `plotly` (Visualización de datos)
    *   `pandas` y `numpy` (Procesamiento de datos)

El archivo `requirements.txt` contiene todas las dependencias necesarias.

---

## 🚀 Instalación Paso a Paso

Sigue estos pasos para configurar el entorno de desarrollo:

1.  **Clonar el Repositorio**:
    ```bash
    git clone https://github.com/randallnunezsancho-netizen/CCE.git
    cd CCE
    ```

2.  **Crear un Entorno Virtual (Opcional pero recomendado)**:
    *   Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   Mac/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instalar Dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la Aplicación**:
    ```bash
    streamlit run app.py
    ```

Una vez ejecutado, la aplicación se abrirá automáticamente en tu navegador predeterminado (usualmente en `http://localhost:8501`).

---

## 💡 Guía de Uso

1.  **Panel Lateral**: Utilízalo para repasar la fórmula teórica y las definiciones de las variables.
2.  **Panel Principal - Controles**:
    *   Desliza los controles de **DI** (Verde), **DCC** (Naranja) y **DCP** (Morado) para simular diferentes escenarios operativos.
3.  **Interpretación de Resultados**:
    *   Observa el número grande central. Este es tu **Ciclo de Conversión de Efectivo**.
    *   Lee la tarjeta de abajo para entender si tu empresa necesita financiamiento (CCE Positivo) o se está financiando con proveedores (CCE Negativo).
4.  **Análisis Gráfico**:
    *   Interactúa con el gráfico de barras al final de la página.
    *   Observa cómo la barra azul (CCE) llena el espacio que deja la gestión de cobros e inventarios frente a los pagos.

---

## 📂 Estructura del Proyecto

```text
CCE/
│
├── app.py                      # Archivo principal de la aplicación Streamlit
├── requirements.txt            # Lista de dependencias del proyecto
├── documentos/                 # Documentación y archivos de diseño
│   └── funcionalidades_CCE.md  # Definición de alcance y funcionalidades
├── venv/                       # Entorno virtual (no incluido en git)
└── README.md                   # Documentación del proyecto
```

---

## 🎓 Interpretación Pedagógica de Resultados

El proyecto busca enseñar dos estados fundamentales:

### 🔴 CCE Positivo (Efectivo "Amarrado")
Ocurre cuando `(Días Inventario + Días Cobro) > Días Pago`.
*   **Significado**: La empresa paga a sus proveedores antes de recibir el dinero de sus clientes.
*   **Consecuencia**: Necesita capital de trabajo adicional (préstamos o capital propio) para cubrir ese hueco de días.

### 🟢 CCE Negativo (Financiamiento Espontáneo)
Ocurre cuando `Días Pago > (Días Inventario + Días Cobro)`.
*   **Significado**: La empresa cobra a sus clientes y vende su inventario antes de tener que pagar a sus proveedores.
*   **Consecuencia**: Los proveedores están financiando la operación. Es una situación muy favorable para la liquidez.

---

## ⚖️ Licencia y Nota Educativa

Este proyecto es **Open Source** bajo la licencia **MIT**.

> **Nota Educativa**: Esta herramienta ha sido diseñada con fines **exclusivamente pedagógicos** para cursos de Finanzas Corporativas y Análisis Financiero. Aunque utiliza fórmulas financieras estándar, las decisiones empresariales reales deben considerar múltiples factores adicionales no contemplados en este modelo simplificado.

---
**Desarrollado con ❤️ para la enseñanza financiera.**  
*Udemy Antigravity Python Course*
