# 📝 Bitácora de Cambios y Aprendizajes - Proyecto CCE

Este documento registra la evolución del proyecto **Ciclo de Conversión de Efectivo (CCE)**, detallando las funcionalidades implementadas, las modificaciones realizadas y los aprendizajes técnicos y de flujo de trabajo adquiridos.

---

## 📅 Historial de Cambios

### [2025-12-12] - Funcionalidad 2: Visualización Gráfica y Documentación
**Descripción del Cambio:**
*   Implementación de gráfico de barras horizontales con `plotly.graph_objects`.
*   Lógica tipo Gantt para visualizar la composición del ciclo (DI, DCC, DCP, CCE).
*   Ajuste de colores en el gráfico para coincidir con los sliders (Verde, Naranja, Morado, Azul).
*   Generación del archivo `README.md` con instrucciones de instalación, uso y contexto pedagógico.

**💡 Aprendizajes:**
*   **Plotly en Streamlit**: La integración de gráficos interactivos de Plotly enriquecen significativamente la experiencia de usuario comparado con gráficos estáticos.
*   **Lógica Visual**: Traducir una fórmula matemática (`DI + DCC - DCP`) a una representación visual de barras requiere una lógica de "inicio" y "fin" (bases) para cada barra, similar a un cronograma.

---

### [2025-12-12] - Funcionalidad 1: Variables y Cálculos Básicos
**Descripción del Cambio:**
*   Creación de la estructura base de la aplicación en `app.py`.
*   Implementación de sliders para variables de entrada (DI, DCC, DCP).
*   Desarrollo lógico del cálculo del CCE.
*   **Ajuste de UI**: Se modificó el color y tamaño de fuente de las etiquetas de días en los sliders para mejorar la legibilidad y consistencia con los emoticonos, usando HTML/CSS inyectado vía `st.markdown`.
*   Mensajes condicionales (Rojo/Verde) para interpretar el resultado.

**💡 Aprendizajes:**
*   **Personalización de Streamlit**: Aunque Streamlit es limitado en diseño nativo, el uso de `st.markdown` con HTML y CSS (`unsafe_allow_html=True`) es crucial para lograr una estética "premium" y personalizada (colores específicos, tamaños de fuente).
*   **Interacción con el Agente**: Se identificó que para ajustes finos de diseño (como tamaño de letra específico o colores exactos), es más efectivo dar instrucciones precisas y directas ("aumentar letra", "color gris a color X") que descripciones generales.

---

### [2025-12-11] - Inicio del Proyecto
**Descripción del Cambio:**
*   Configuración inicial del repositorio.
*   Creación del entorno virtual y definición de `requirements.txt`.
*   Definición del alcance en `documentos/funcionalidades_CCE.md`.

**💡 Aprendizajes:**
*   **Planificación**: Separar el proyecto en funcionalidades cláramente definidas (Sprints) facilita el desarrollo modular y evita la sobrecarga cognitiva al programar.
