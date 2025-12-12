# Documento de Funcionalidades del Proyecto

Este documento describe las funcionalidades que desarrollaremos en el proyecto **Ciclo de Conversión de Efectivo**, utilizando **Antigravity** como entorno de desarrollo.  

El enfoque que seguimos es **pedagógico**: queremos ilustrar cómo un proyecto puede dividirse en distintas etapas (*sprints*), cada una con un entregable funcional. En un entorno real, muchas de estas funcionalidades podrían desarrollarse de forma iterativa o integrada, pero aquí las mantendremos separadas para fines de enseñanza.

---

## Funcionalidad 1: Variables financieras básicas para el cálculo

**Objetivo**: Capturar las variables contables claves y calcular los componentes del modelo de acuerdo  

**Alcance**:
- Entrada mediante *sliders* de 3 variables de la fórmula: CCE = di + dcc - dcp:  
  - di = días inventario  
  - dcc = días cuentas por cobrar  
  - dcp = días cuentas por pagar
  
- Cálculo de los tres componentes:  
  estas 3 variables alcanzan un valor de 0 a 100.  
- Visualización del resultado en métricas numéricas más la palabra "días", aplicando los valores de los sliders.

- El panel izquierdo lleva una pequeña explicación de la fórmula, las variables y qué mide el ciclo de conversión de efectivo.


-incluir un mensaje dinámico que cambie de color debajo del resultado
	1. si el ciclo es positivo (rojo), con una leyenda de: "CCE: positivo (xx días). La empresa necesita XX días adicionales para convertir sus inversiones en efectivo. El efectivo queda amarrado en el ciclo operativo".  
	2. si el ciclo es negativo(verde) con una leyenda de: "CCE: negativo (xx días). La empresa cobra xx días antes de pagar a sus proveedores. Esto representa un financiamiento operativo favorable".

- Construir la aplicación sobre un fondo oscuro para el descanso de la vista del usuario.
- Puedes utilizar emojis para una visualización más amigable 
- Los colores están sincronizados entre las leyendas de los slicers y las barras del gráfico de la función 2. Un color por cada variable.


---

## Funcionalidad 2: Visualización en un gráfico de barras horizontales 

**Objetivo**: Representar gráficamente la descomposición del Ciclo de Conversión de Efectivo (CCE).  

**Alcance**:
- Construcción de un gráfico que muestre la interacción de:  
 	1. DI = días inventario  
   	2. DCC = días cuentas por cobrar  
   	3. DCP = días cuentas por pagar
   	4. CCE = el resultado

- El gráfico deberá actualizarse dinámicamente cuando cambien las variables de entrada en los slicers.  
- Etiquetas y ejes explicativos que refuercen la interpretación del modelo.

Esta es la **“joya pedagógica”** del proyecto: permite comprender de forma intuitiva cómo se combinan los factores para determinar el ciclo de conversión de efectivo.

En el gráfico:

- la barra días de inventario comienza siempre en cero.
- la barra días de cuentas por cobrar no comienzan en cero, inician a partir del final de días del inventario. Porque en la fórmula se suman y se quiere tener esa representación.
- la barra días de cuentas por pagar inician desde cero.
- y la barra del resultado inicia según el escenario:(PERO SIEMPRE DEBE SER MOSTRADA, AÚN CUANDO SEA VALOR CERO)

	Componente,			Posición de Inicio,	Posición de Fin,		Comentario
	Días Inventario (DI),		0,			DI,				Siempre inicia en cero.
	Días Cuentas por Cobrar (DCC),	DI,			DI + DCC,			Inicia al final de DI (se suma al ciclo).
	Días Cuentas por Pagar (DCP),	0,			DCP,				"Inicia en cero (indica el ""ahorro"" en tiempo)."
	CCE (Resultado),		"min(DI+DCC,DCP)",	"max(DI+DCC,DCP)",		Depende del escenario (Positivo/Negativo).

	
---

## Nota final

Estas funcionalidades se desarrollarán **en dos sprints**, cada uno enfocado en una parte específica del proyecto.  
Al mantenerlas separadas, los estudiantes podrán comprender mejor cómo se construye progresivamente un sistema, desde los cálculos básicos hasta las visualizaciones avanzadas y el contexto financiero.  

Este enfoque permite practicar no solo la programación con **Python, Streamlit y Plotly**, sino también la organización profesional de un proyecto de desarrollo con **Antigravity AI**.

