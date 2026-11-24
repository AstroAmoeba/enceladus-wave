# Dinámica de medios deformables, forzamiento por mareas y geofísica sísmica del interior de Encélado

**Informe técnico-científico basado en los modelos sísmicos 1D, 2D y 3D**  
**Referencias principales:** Dapré e Irving (2024, 2025)  
**Asignatura:** Dinámica de Medios Deformables  
**Fecha:** 23 de noviembre de 2026

## Resumen

El presente informe ofrece una caracterización rigurosa e integrada de la estructura interna, el comportamiento reológico y la respuesta sísmica de la luna helada de Saturno, Encélado. Se combinan los principios fundamentales de la mecánica de medios continuos y deformables (ecuaciones de balance de Cauchy, reología viscoelástica, elasticidad lineal de Hooke y propagación de ondas) con los hallazgos recientes del modelado sísmico 1D, 2D y 3D publicado por Dapré e Irving (2024, 2025). Se analizan los mecanismos de disipación de marea provocados por la excentricidad orbital, la refracción y reflexión de ondas en la corteza de hielo y en el océano subsuperficial, la transmisión a través del núcleo poroso o serpentinizado y las implicaciones cinemáticas para la selección de sitios de aterrizaje de futuras misiones planetarias (*Orbilander*). El documento incluye la formulación matemática detallada y una sección bibliográfica.

## 1. Introducción y marco geofísico de Encélado

Encélado (radio $R \approx 252\ \text{km}$) representa uno de los objetivos astrobiológicos y geofísicos prioritarios del sistema solar. Las observaciones de la sonda *Cassini* revelaron la presencia de una corteza helada exterior, un océano global de agua líquida y un núcleo rocoso de silicato hipotéticamente poroso o serpentinizado.

En el polo sur de Encélado se localizan cuatro *rifts* tectónicos principales, conocidos como *Tiger Stripe Fractures* (TSF). Estas fracturas penetran el grosor de la corteza de hielo y son la fuente de géiseres o *plumes* que expulsan vapor de agua, sales y compuestos orgánicos. La actividad tectónica y térmica de estas fallas está modulada periódicamente por el forzamiento de mareas gravitacionales que ejerce Saturno durante cada órbita (1,37 días).

Desde la perspectiva de la mecánica de medios deformables, comprender la dinámica interna de Encélado exige desacoplar y modelar:

1. La respuesta elástica y viscoelástica de la corteza helada ($T \sim 35$–$273\ \text{K}$).
2. La hidrodinámica invíscida o viscosa del océano subsuperficial.
3. La transferencia de esfuerzos y disipación de marea en el núcleo poroso de silicatos.
4. La propagación de frentes de onda sísmica tridimensionales (ondas P, S, ondas de superficie y ondas transmitidas por el núcleo).

## 2. Fundamentos de mecánica de medios deformables

### 2.1. Ecuaciones locales de balance y tensor de esfuerzos

Para cualquier medio continuo clásico (sólido o fluido) de densidad $\rho$, en un sistema de referencia inercial con campo de fuerzas de cuerpo por unidad de masa $\mathbf{b}$, la conservación del momento lineal viene dada por la ecuación de Cauchy:

$$
\rho\frac{D\mathbf{u}}{Dt}
= \nabla\cdot\boldsymbol{\sigma} + \rho\mathbf{b}
\quad\Longrightarrow\quad
\rho\left(\frac{\partial u_i}{\partial t}
+ u_j\frac{\partial u_i}{\partial x_j}\right)
= \frac{\partial\sigma_{ij}}{\partial x_j} + \rho b_i
$$

donde $\boldsymbol{\sigma}$ es el tensor de esfuerzos de Cauchy ($3\times3$). El balance de momento angular microscópico exige que, en ausencia de momentos de par externos, el tensor de esfuerzos sea simétrico:

$$
\sigma_{ij} = \sigma_{ji}
$$

Asimismo, la conservación de la masa se expresa mediante la ecuación de continuidad:

$$
\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{u}) = 0
$$

Para materiales incompresibles ($\rho = \text{constante}$), la condición geométrica se simplifica a la divergencia nula del campo de velocidades o desplazamientos:

$$
\nabla\cdot\mathbf{u}
= \epsilon_{kk}
= \frac{\partial u_k}{\partial x_k}
= 0
$$

### 2.2. Leyes constitutivas y atenuación viscoelástica

Para un sólido isotrópico linealmente elástico (sólido de Hooke), las ecuaciones constitutivas relacionan el tensor de esfuerzos $\boldsymbol{\sigma}$ con el tensor de deformaciones infinitesimales

$$
\boldsymbol{\epsilon}
= \frac{1}{2}\left(\nabla\mathbf{u} + (\nabla\mathbf{u})^T\right)
$$

mediante los parámetros de Lamé ($\lambda,\mu$):

$$
\sigma_{ij} = \lambda\epsilon_{kk}\delta_{ij} + 2\mu\epsilon_{ij}
$$

donde $\mu = G$ es el módulo de corte o cizalladura y $\lambda = K - \frac{2}{3}\mu$, siendo $K$ el módulo de compresibilidad volumétrica. En términos inversos, con el módulo de Young $E$ y el coeficiente de Poisson $\nu$:

$$
\epsilon_{ij}
= \frac{1+\nu}{E}\sigma_{ij}
- \frac{\nu}{E}\sigma_{kk}\delta_{ij}
$$

En la corteza helada de Encélado, la temperatura varía drásticamente desde los $35\ \text{K}$ en la superficie polar hasta la temperatura de fusión $T_0 \approx 273\ \text{K}$ en la base del océano. Dado que el hielo cerca del punto de fusión exhibe comportamiento plástico y viscoelástico, la respuesta a solicitaciones dinámicas presenta un desfase angular $0 < \phi < \pi/2$ entre esfuerzo y deformación, caracterizado por el factor de calidad sísmica $Q$:

$$
Q^{-1}(\omega,T) = \tan\phi(\omega,T)
$$

La atenuación $Q^{-1}$ se incrementa exponencialmente conforme la temperatura se aproxima al punto de fusión en la base del hielo.

## 3. Forzamiento por mareas y modelo reológico de Encélado

### 3.1. Gravitación diferencial y tectónica polar

Encélado orbita Saturno en una órbita ligeramente excéntrica ($e \approx 0.0047$), lo que genera variaciones periódicas en la distancia y en la dirección del vector de atracción gravitacional. Este gradiente espacial induce un campo de esfuerzo de marea oscilatorio ($\boldsymbol{\sigma}^{\text{tide}}$) sobre la corteza y el núcleo.

La fuerza de cuerpo por unidad de masa debida a la marea se deriva del potencial de marea $U_{\text{tide}}$:

$$
\mathbf{b}^{\text{tide}}
= -\nabla U_{\text{tide}}(r,\theta,\phi,t)
$$

En los *rifts* TSF del polo sur, el esfuerzo cortante de marea provoca fallamiento por cizalladura rumbada (*strike-slip*) o por tensión normal, promoviendo la reapertura constante de conductos y alimentando el criovolcanismo.

### 3.2. Estructura interna y modelos sísmicos

Dapré e Irving (2024, 2025) construyeron e inspeccionaron modelos estructurales con variaciones en las tres capas constituyentes:

| Modelo | Corteza de hielo | Océano líquido | Núcleo de silicato |
| --- | --- | --- | --- |
| **SingleCore** (promedio 1D) | 20 km | 50 km ($V_p = 1400\ \text{m/s}$) | Homogéneo comprimido ($R_c = 182\ \text{km}$) |
| **LayeredCore** (promedio 1D) | 20 km | 43 km ($V_p = 1400\ \text{m/s}$) | 30 km de antigorita sobre olivino seco |
| **ThickIce** (hielo grueso) | 40 km | 27 km ($V_p = 1400\ \text{m/s}$) | Capa serpentinizada delgada de 4 km |
| **SealedCore** (heterogéneo 2D/3D) | Variable | Variable | Capa serpentinizada expandida o rehidratada |

## 4. Sismología global y propagación de frentes de onda

### 4.1. Nomenclatura de fases sísmicas

Para describir la trayectoria de los rayos sísmicos que atraviesan los medios heterogéneos de Encélado, se emplea la convención introducida por Stähler et al. (2018) y ampliada por Dapré e Irving:

- **P, S:** ondas compresionales (P) y de corte (S) que se propagan en el hielo o en el núcleo.
- **e:** reflexión en la superficie base de la corteza de hielo (interfaz hielo-océano).
- **F:** onda compresional (P) que se propaga a través del océano fluido.
- **o:** reflexión en la interfaz océano-núcleo rocoso.
- **PFPFP:** onda compresional que nace en el hielo, atraviesa el océano como onda F, penetra y cruza el núcleo rocoso como P, cruza el océano nuevamente y retorna a la superficie helada.
- **P(FoF)$_N$FoFP:** reverberaciones múltiples dentro del océano subsuperficial.

### 4.2. Ecuaciones de onda y simulación computacional

La propagación de ondas elásticas e incompresibles en el medio continuo se resuelve mediante la ecuación vectorial de elastodinámica de Navier-Cauchy:

$$
\rho\frac{\partial^2\mathbf{u}}{\partial t^2}
= (\lambda+\mu)\nabla(\nabla\cdot\mathbf{u})
+ \mu\nabla^2\mathbf{u}
+ \rho\mathbf{b}
$$

En los trabajos de Dapré e Irving:

1. **Modelado 1D (2024):** se utilizó el código AxiSEM con mallas axisimétricas a frecuencias de hasta 8 Hz, aplicando un filtro de paso de banda de 1–6 Hz.
2. **Modelado 2D y 3D (2025):** se utilizó el código de elementos finitos espectrales AxiSEM3D a frecuencias de malla de 4 Hz, incorporando la topografía 3D de la corteza de hielo (modelos de Hemingway y Mittal, 2019, y Čadek et al., 2019) y perfiles térmicos bidimensionales $T(r,\theta,\phi)$.

## 5. Comparación de modelos 1D y 3D e implicaciones para misiones

### 5.1. Efecto de la heterogeneidad de la corteza y atenuación

Las simulaciones en 3D demuestran que el espesor variable de la corteza helada (desde menos de 5 km en el polo sur hasta más de 35 km en el ecuador y latitudes medias) altera los tiempos de llegada de las ondas de cuerpo en $\pm5$–$10\ \text{s}$. Esta magnitud de perturbación es similar al retraso inducido por variaciones estructurales dentro del núcleo rocoso (30–40 s).

Sin embargo, las fases que entran al núcleo con ángulos de salida empinados (tales como PFPFP y PFPPFP) escapan rápidamente de la zona caliente de alta atenuación en la base polar del hielo, manteniendo amplitudes detectables de aproximadamente $10^{-6}\ \text{m/s}^2$. Esto supera en dos órdenes de magnitud el piso de ruido instrumental del sismómetro de periodo corto (SP) de la misión *InSight* ($<10^{-8}\ \text{m/s}^2$).

### 5.2. Recomendación de sitio de aterrizaje

Para optimizar el retorno científico de un sismómetro único en superficie (*Orbilander*):

1. Se recomienda una ubicación de aterrizaje entre $20^\circ$ y $30^\circ$ de distancia epicentral desde el polo sur.
2. Esta franja evita la extrema atenuación basal del polo sur inmediato, garantiza visibilidad directa a la Tierra y luz solar, y registra simultáneamente ondas guiadas en el hielo, reverberaciones oceánicas P(FoF)$_N$FoFP y fases que muestrean el núcleo profundo (PFPFP).
3. Se aconseja el uso de sismómetros de 3 componentes para realizar análisis de polarización y determinar el azimut de origen de los sismos.

## 6. Conclusiones

1. La mecánica de medios deformables proporciona el marco riguroso para modelar desde la deformación por marea hasta la sismología planetaria en lunas heladas.
2. La elevada atenuación térmica en la base de la corteza de hielo no impide la detección de ondas de cuerpo profundas; sirve como un filtro natural que elimina ruido de fondo secundario.
3. El modelado 2D/3D con AxiSEM3D demuestra que las fases que atraviesan el núcleo (PFPFP) se pueden desacoplar del efecto del grosor local de la corteza mediante diferencias de tiempo entre fases guiadas por el océano.
4. La ventana geofísica óptima para futuras misiones espaciales se sitúa entre $20^\circ$ y $30^\circ$ de distancia respecto a la zona del polo sur.

## 7. Bibliografía y referencias

1. Dapré, K., & Irving, J. C. E. (2024). Global seismology in the interior of Enceladus. *Icarus, 408*, 115806. [https://doi.org/10.1016/j.icarus.2023.115806](https://doi.org/10.1016/j.icarus.2023.115806)
2. Dapré, K., & Irving, J. C. E. (2025). Seismic wavefield modeling of Enceladus: Challenges and opportunities presented by a 3D ice shell. *Journal of Geophysical Research: Planets, 130*(1), e2024JE008644. [https://doi.org/10.1029/2024JE008644](https://doi.org/10.1029/2024JE008644)
3. Čadek, O., Tobie, G., Van Hoolst, T., Massé, M., Choblet, G., Lefèvre, A., et al. (2016). Enceladus’s internal ocean and ice shell constrained from Cassini gravity, shape, and libration data. *Geophysical Research Letters, 43*(11), 5653–5660. [https://doi.org/10.1002/2016GL068634](https://doi.org/10.1002/2016GL068634)
4. Čadek, O., Souček, O., Běhounková, M., Choblet, G., Tobie, G., & Hron, J. (2019). Long-term stability of Enceladus’ uneven ice shell. *Icarus, 319*, 476–484. [https://doi.org/10.1016/j.icarus.2018.10.003](https://doi.org/10.1016/j.icarus.2018.10.003)
5. Hemingway, D. J., & Mittal, T. (2019). Enceladus’s ice shell thickness as constrained by gravity and topography. *Icarus, 332*, 111–115.
6. Stähler, S. C., Panning, M. P., Vance, S. D., Lorenz, R. D., van Driel, M., Nissen-Meyer, T., & Kedar, S. (2018). Seismic wave propagation in icy ocean worlds. *Journal of Geophysical Research: Planets, 123*(1), 206–232. [https://doi.org/10.1002/2017JE005338](https://doi.org/10.1002/2017JE005338)
7. Spurk, J. H., & Aksel, N. (2008). *Fluid Mechanics* (2.ª ed.). Springer-Verlag.
8. Viniegra, F. (2008). *Mecánica del cuerpo deformable* (borrador). Facultad de Ciencias, UNAM.
9. Chaves, E. W. V. (2013). *Notes on Continuum Mechanics*. Springer Science & Business Media.
10. Ortiz Prado, A. *Apuntes de Mecánica del Medio Continuo*. Facultad de Ingeniería, UNAM.
11. Lognonné, P., Banerdt, W. B., Giardini, D., Pike, W. T., Christensen, U., et al. (2019). SEIS: InSight’s seismic experiment for internal structure of Mars. *Space Science Reviews, 215*(1), 12.
12. MacKenzie, S. M., Neveu, M., Davila, A. F., Lunine, J. I., Craft, K. L., et al. (2021). The Enceladus Orbilander mission concept: Balancing return and resources in the search for life. *The Planetary Science Journal, 2*(2), 77.