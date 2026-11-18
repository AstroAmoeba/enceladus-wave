# Seguimiento del proyecto final — Lista de tareas y entregables

**Título:** Propagación de ondas elásticas en la capa de hielo de Encelado: análisis teórico de reflexión-transmisión y validación numérica simplificada con TauP y Deepwave

**Duración:** 4 semanas
**Herramientas:** Python (NumPy, Matplotlib), ObsPy TauP, Deepwave, LaTeX/Markdown

---

## Semana 1 — Fundamentos teóricos y modelos de hielo

### Tareas

- [ ] Lectura focalizada de Dapré & Irving (2024): secciones 1, 2.1–2.3, 3.1
- [ ] Lectura de Dapré & Irving (2025): introducción y discusión sobre heterogeneidad 3D
- [ ] Estudio de elasticidad lineal y ecuación de Navier–Lamé (Shearer, cap. 2; Royer & Valier-Brasier, cap. 1–2)
- [ ] Derivar la ecuación de onda elástica para medio isótropo con $\lambda(z)$, $\mu(z)$, $\rho(z)$
- [ ] Estudiar el perfil térmico de Hussmann et al. (2015) — Ec. (1) del artículo
- [ ] Estudiar la relación velocidad–temperatura en hielo (Kohnen, 1974; Aster & Winberry, 2017)
- [ ] Construir script en Python para generar perfiles $T(z)$, $V_P(z)$, $V_S(z)$ para:
  - [ ] Modelo de hielo delgado (20 km)
  - [ ] Modelo de hielo grueso (40 km)
  - [ ] Modelo con gradiente térmico conductivo
- [ ] Generar Figura 1: perfiles de velocidad y temperatura
- [ ] Revisión con el profesor (si aplica) y ajuste del alcance

### Entregables

- [ ] **E1.1** — Borrador de la sección de marco teórico (elasticidad + termoelasticidad)
- [ ] **E1.2** — Derivación escrita de la ecuación de onda con propiedades variables
- [ ] **E1.3** — Figura 1: perfiles $T(z)$, $V_P(z)$, $V_S(z)$ para los tres modelos
- [ ] **E1.4** — Script `perfiles_hielo.py` funcionando y documentado

---

## Semana 2 — Reflexión, transmisión y aproximación WKBJ

### Tareas

- [ ] Estudiar condiciones de frontera en interfaces (Shearer, cap. 3; Royer & Valier-Brasier, cap. 3)
- [ ] Derivar coeficientes de reflexión y transmisión para incidencia normal y oblicua
- [ ] Calcular numéricamente $R$ y $T$ para la interfaz hielo–océano en los tres modelos
- [ ] Analizar sensibilidad de $R$ y $T$ al espesor del hielo y al perfil térmico
- [ ] Estudiar la aproximación WKBJ (Shearer, cap. 4)
- [ ] Derivar la expresión de tiempo de viaje $t = \int dz / V(z)$ y amplitud $\propto 1/\sqrt{\rho V}$
- [ ] Implementar integración numérica WKBJ en Python
- [ ] Calcular tiempos de viaje WKBJ para fases PeP, SeS y sus múltiplos
- [ ] Generar Figura 2: tiempos de viaje WKBJ vs. distancia epicentral (comparación con Fig. 6 de Dapré & Irving, 2024)
- [ ] Instalar ObsPy y familiarizarse con TauP
- [ ] Construir modelo de velocidad 1D simplificado de Encelado en ObsPy (hielo, océano, núcleo)
- [ ] Calcular tiempos de viaje con TauP para PeP y SeS con dos espesores de hielo
- [ ] Generar Figura 3: tiempos TauP vs. distancia epicentral (hielo delgado vs. grueso)
- [ ] Comparar cuantitativamente WKBJ vs. TauP y discutir discrepancias

### Entregables

- [ ] **E2.1** — Formulario de coeficientes $R$, $T$ (derivación)
- [ ] **E2.2** — Tabla 1: coeficientes $R$, $T$ para cada modelo e interfaz
- [ ] **E2.3** — Figura 2: tiempos de viaje WKBJ
- [ ] **E2.4** — Figura 3: tiempos de viaje TauP (validación)
- [ ] **E2.5** — Script `wkbj_tiempos.py` y `taup_encelado.py`
- [ ] **E2.6** — Borrador de la sección de metodología (Parte A y B)

---

## Semana 3 — Simulación conceptual, acoplamiento tidal y discusión

### Tareas

- [ ] Instalar Deepwave (`pip install deepwave`)
- [ ] Estudiar los ejemplos de simulación elástica 1D/2D de la documentación de Deepwave
- [ ] Configurar modelo 1D de dos capas (hielo sobre océano) con velocidades realistas
- [ ] Definir fuente tipo Ricker somera y receptor en superficie
- [ ] Ejecutar simulación para un caso simple (hielo homogéneo)
- [ ] Identificar llegada directa y reflexión en la interfaz hielo–océano
- [ ] Generar Figura 4: sismograma sintético 1D conceptual (Deepwave)
- [ ] Discutir limitaciones del modelo Deepwave frente a los modelos analíticos y a AxiSEM
- [ ] Estudiar potencial tidal de Saturno sobre Encelado y esfuerzos tidales (Hurford et al., 2020; Dapré & Irving, 2024, sección 1)
- [ ] Redactar sección corta (1–2 páginas) sobre acoplamiento tidal y reactivación de TSF
- [ ] Analizar termoelasticidad: cómo el gradiente térmico modifica $V_P$, $V_S$ y $Q^{-1}$
- [ ] Generar Figura 5: $Q^{-1}(T)$ comparando Cammarano et al. (2006) vs. Kuroiwa (1964) (basado en Fig. 2 del artículo)
- [ ] Redactar sección de resultados y discusión (borrador)
- [ ] Redactar sección de limitaciones del modelo 1D

### Entregables

- [ ] **E3.1** — Figura 4: sismograma sintético 1D (Deepwave)
- [ ] **E3.2** — Script `deepwave_1d.py` funcionando y documentado
- [ ] **E3.3** — Sección de acoplamiento tidal (1–2 páginas)
- [ ] **E3.4** — Figura 5: curvas $Q^{-1}(T)$ y discusión del efecto en amplitudes
- [ ] **E3.5** — Borrador de la sección de resultados y discusión
- [ ] **E3.6** — Sección de limitaciones (1D vs. 3D, isotropía vs. anisotropía, fuente monopolo)

---

## Semana 4 — Redacción final y cierre

### Tareas

- [ ] Redactar introducción (contexto astrobiológico, sismicidad en Encelado, problema de investigación, objetivos)
- [ ] Redactar conclusiones (síntesis de resultados, cumplimiento de objetivos, aportes)
- [ ] Redactar sección de trabajo futuro (solver de diferencias finitas 1D/2D, modelo 3D de Hemingway & Mittal, inversión de datos)
- [ ] Revisar y unificar figuras y tablas (numeración, títulos, referencias en el texto)
- [ ] Revisar referencias bibliográficas (formato consistente)
- [ ] Revisar formato general del documento (márgenes, fuente, espaciado)
- [ ] Preparar presentación (si aplica): diapositivas con figuras clave
- [ ] Ensayar presentación
- [ ] Entrega final del documento
- [ ] Entrega de scripts y datos suplementarios (si se requieren)

### Entregables

- [ ] **E4.1** — Borrador completo del documento (todos los capítulos)
- [ ] **E4.2** — Documento final revisado y formateado
- [ ] **E4.3** — Presentación (diapositivas)
- [ ] **E4.4** — Paquete de scripts (`perfiles_hielo.py`, `wkbj_tiempos.py`, `taup_encelado.py`, `deepwave_1d.py`) con README
- [ ] **E4.5** — Entrega final

---

## Resumen de entregables por semana

| Semana | Entregables principales | Estado |
|---|---|---|
| 1 | E1.1–E1.4: Marco teórico, derivación, Figura 1, script de perfiles | ☐ |
| 2 | E2.1–E2.6: Coeficientes $R$/$T$, Tabla 1, Figuras 2–3, scripts WKBJ y TauP | ☐ |
| 3 | E3.1–E3.6: Figura 4 (Deepwave), sección tidal, Figura 5 ($Q^{-1}$), borrador de resultados | ☐ |
| 4 | E4.1–E4.5: Documento final, presentación, scripts, entrega | ☐ |

---

## Lista de verificación rápida (checklist global)

### Documento
- [ ] Introducción
- [ ] Marco teórico (elasticidad, termoelasticidad, reología, reflexión/transmisión, WKBJ, mareas)
- [ ] Metodología (modelos, TauP, Deepwave)
- [ ] Resultados (Figuras 1–5, Tabla 1)
- [ ] Discusión (comparación con Dapré & Irving, limitaciones)
- [ ] Conclusiones
- [ ] Trabajo futuro
- [ ] Referencias
- [ ] Apéndices (opcional: derivaciones detalladas, código)

### Figuras
- [ ] Figura 1: perfiles $T(z)$, $V_P(z)$, $V_S(z)$
- [ ] Figura 2: tiempos de viaje WKBJ
- [ ] Figura 3: tiempos de viaje TauP (validación)
- [ ] Figura 4: sismograma sintético 1D (Deepwave)
- [ ] Figura 5: curvas $Q^{-1}(T)$

### Tablas
- [ ] Tabla 1: coeficientes $R$, $T$ por modelo e interfaz
- [ ] Tabla 2 (opcional): comparación WKBJ vs. TauP

### Código
- [ ] `perfiles_hielo.py`
- [ ] `wkbj_tiempos.py`
- [ ] `taup_encelado.py`
- [ ] `deepwave_1d.py`
- [ ] `README.md` con instrucciones de ejecución

### Presentación
- [ ] Diapositivas con motivación, objetivos, metodología, resultados clave, conclusiones
- [ ] Ensayo cronometrado

---

## Notas de seguimiento

- **Prioridad alta:** Figuras 1, 2 y 3 (son el núcleo cuantitativo del proyecto).
- **Prioridad media:** Figura 4 (Deepwave) — no debe consumir más de 1–2 días.
- **Prioridad baja:** Apéndices y material suplementario.
- **Riesgo:** Si Deepwave presenta problemas de instalación o configuración, se puede sustituir por un ejemplo de la documentación oficial o por una simulación acústica 1D simple con NumPy. **No debe comprometer el cronograma.**
- **Fecha de revisión con el profesor:** idealmente al final de la semana 1 o 2 para validar el alcance.
