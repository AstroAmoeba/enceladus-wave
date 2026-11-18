
**Título propuesto:**
**“Propagación de ondas elásticas en la capa de hielo de Encelado: análisis teórico de reflexión-transmisión y validación numérica simplificada con TauP y Deepwave”**

**Planteamiento del problema y motivación**

Encelado presenta una capa de hielo cuyo espesor varía con la latitud y cuya temperatura controla tanto las velocidades elásticas como la atenuación. Dapré & Irving (2024, 2025) han mostrado, mediante simulaciones de campo de onda completo, que esta heterogeneidad introduce diferencias en tiempos de arribo comparables a las producidas por la incertidumbre en la estructura del núcleo, lo que plantea un desafío para la interpretación de futuros datos sísmicos . Sin embargo, antes de abordar simulaciones complejas, es necesario establecer los fundamentos analíticos que permitan entender *por qué* y *cuánto* afecta la heterogeneidad del hielo a la propagación de ondas P y S.

**Objetivo general**

Caracterizar el efecto de la heterogeneidad de espesor y temperatura de la capa de hielo de Encelado sobre la propagación de ondas elásticas P y S, mediante análisis teórico de reflexión/transmisión y tiempos de viaje, complementado con simulaciones numéricas simplificadas que permitan validar las tendencias predichas.

**Objetivos específicos**

1. Derivar las ecuaciones de Lamé para un medio isótropo con propiedades ($\lambda$, $\mu$, $\rho$) variables con la profundidad, y obtener los coeficientes de reflexión y transmisión en la interfaz hielo–océano en función del espesor y del perfil térmico.
2. Calcular tiempos de viaje mediante la aproximación de rayos (WKBJ) para fases representativas (PeP, SeS y sus múltiplos) en escenarios de hielo delgado (20 km) y grueso (40 km).
3. **Validar los cálculos analíticos mediante ObsPy TauP**, generando curvas de tiempo-distancia para las mismas fases y modelos, y comparando cuantitativamente con las tendencias reportadas en Dapré & Irving (2024).
4. **Implementar una simulación 1D conceptual con Deepwave** para una capa de hielo homogénea con contraste de impedancia hielo–océano, con el fin de visualizar la generación de fases reflejadas y transmitidas, y discutir sus limitaciones frente a los modelos analíticos.
5. Discutir cualitativamente el acoplamiento tidal como mecanismo generador de la sismicidad en las Tiger Stripe Fractures y su relación con la ubicación de la fuente.

**Metodología (resumen)**

**Parte A – Análisis teórico (semanas 1–2):**
- Derivación de la ecuación de onda elástica con propiedades variables con $z$.
- Cálculo de coeficientes de reflexión/transmisión $R$, $T$ usando impedancias $Z = \rho V$.
- Integración WKBJ para tiempos de viaje: $t = \int dz / V(z)$.
- Perfiles $T(z)$, $V_P(z)$, $V_S(z)$ basados en Hussmann et al. (2015) y la relación hielo–temperatura de Kohnen (1974).

**Parte B – Validación con ObsPy TauP (semana 2–3):**
- Construcción de un modelo de velocidad 1D simplificado de Encelado (hielo, océano, núcleo) usando los valores de la Fig. 4 de Dapré & Irving (2024).
- Cálculo de tiempos de viaje para PeP y SeS con dos espesores de hielo distintos.
- Comparación de las diferencias de tiempo de arribo (en segundos) con las tendencias de la Fig. 6 del artículo. **Producto: una figura de tiempo vs. distancia epicentral con dos curvas (hielo delgado vs. grueso).**

**Parte C – Simulación conceptual con Deepwave (semana 3):**
- Configuración de un modelo 1D de dos capas (hielo sobre océano) con velocidades $V_P$ realistas.
- Propagación de una ondícula de Ricker desde una fuente somera, registro en superficie.
- Identificación visual de la llegada directa y la reflexión en la interfaz hielo–océano.
- **Producto: un sismograma sintético 1D simple que ilustra el concepto de reflexión.** Se discutirá explícitamente que este modelo no captura efectos 3D ni heterogeneidad lateral, y que su función es exclusivamente pedagógica/conceptual.

**Parte D – Discusión y acoplamiento tidal (semana 3–4):**
- Sección breve sobre esfuerzos tidales y reactivación de TSF (basada en Hurford et al., 2020 y Dapré & Irving, 2024).
- Limitaciones del enfoque 1D frente a los modelos 3D de Dapré & Irving (2025).

**Entregables concretos**

| Semana | Entregable |
|---|---|
| 1 | Derivación de ecuación de onda con propiedades variables; perfiles $V_P(z)$, $V_S(z)$, $T(z)$ |
| 2 | Tabla de coeficientes $R$, $T$ para interfaz hielo–océano; figura de tiempos WKBJ |
| 3 | Figura de tiempos TauP (validación); sismograma Deepwave conceptual; sección de acoplamiento tidal |
| 4 | Documento final + presentación |

**Trabajo futuro (explícitamente fuera de alcance)**

- Implementación de un solver de diferencias finitas 1D/2D para campo de onda completo en medios con heterogeneidad de espesor.
- Modelo 2D/3D de espesor variable (Hemingway & Mittal, 2019, truncado).
- Inversión de tiempos de arribo para recuperar estructura del hielo y del núcleo.

**Bibliografía fundamental**

- Dapré, K. & Irving, J.C.E. (2024). Global seismology in the interior of Enceladus. *Icarus*, 408, 115806. 
- Dapré, K. & Irving, J.C.E. (2025). Seismic Wavefield Modeling of Enceladus: Challenges and Opportunities Presented by a 3D Ice Shell. *JGR Planets*. 
- Shearer, P.M. (2009). *Introduction to Seismology*.
- Royer, D. & Valier-Brasier, T. (2022). *Elastic Waves in Solids*.
- Igel, H. (2017). *Computational Seismology* (para trabajo futuro).

**Herramientas computacionales**

- **ObsPy** (TauP): cálculo de tiempos de viaje. Documentación: obspy.org.
- **Deepwave** (PyTorch): simulación de onda elástica 1D. Instalación: `pip install deepwave` .
- Python (NumPy/Matplotlib): integración WKBJ y gráficos.


### Por qué esta combinación funciona para tu caso

**ObsPy TauP** es la herramienta que **el propio artículo de Dapré & Irving usa** para sus cálculos de tiempos de viaje . Al usarla, estás replicando su metodología con un modelo simplificado, lo cual es una validación legítima y directa. La curva de aprendizaje es mínima: en una tarde puedes tener tu primera figura.

**Deepwave** añade el componente “visual” de un sismograma, que es atractivo para la presentación y demuestra que entiendes la diferencia entre un tiempo de viaje (rayo) y una traza sísmica (campo de onda). Pero **limítalo a un solo caso** (hielo homogéneo sobre océano) y preséntalo como “demostración conceptual”, no como resultado principal. Su documentación incluye ejemplos de onda elástica 1D/2D que puedes adaptar .

**El equilibrio:** la Parte A (teoría) es el núcleo del proyecto, la Parte B (TauP) aporta resultados cuantitativos comparables con el artículo, y la Parte C (Deepwave) aporta una ilustración visual sin consumir tiempo excesivo. Así cumples con el balance “teoría + simulación sencilla” que buscas, sin salirte del alcance de 4 semanas que tu profesor aprobó.
