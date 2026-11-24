# Dinámica de medios deformables, forzamiento por mareas y geofísica sísmica del interior de Encélado

## 1. Marco fundacional de la mecánica de medios continuos aplicado a cuerpos planetarios

El estudio de la respuesta estructural, la elastodinámica y el comportamiento térmico de los cuerpos helados del sistema solar exterior requiere un tratamiento analítico basado en la mecánica del medio continuo. Este marco físico-matemático constituye el pilar fundamental para modelar cuantitativamente la deformación finita e infinitesimal, la respuesta reológica compleja bajo cargas cíclicas y la propagación de ondas sísmicas a través de la litosfera helada, el océano subsuperficial y el núcleo rocoso de Encélado. Al abstraer la microestructura de los agregados policristalinos de hielo I$_h$ y los silicatos del núcleo en campos tensoriales diferenciables de esfuerzo, deformación y flujo, se pueden formular ecuaciones de gobierno que predicen la respuesta del sistema planetario global ante perturbaciones dinámicas exógenas y endógenas.

### Análisis cinemático y dinámico

La descripción del estado mecánico en un punto del continuo planetario se fundamenta en la representación tensorial del esfuerzo y la deformación. El estado tensional interno se define mediante el tensor de esfuerzos de Cauchy, denotado en notación directa como $\mathbf{\sigma}$ y en notación de índices como $\sigma_{ij}$. Es un tensor simétrico de segundo orden ($\sigma_{ij} = \sigma_{ji}$) cuyas componentes especifican las tracciones normales y cortantes sobre planos ortogonales. Cinemáticamente, para pequeñas deformaciones en la litosfera helada, el tensor de deformación infinitesimal $\mathbf{E}$ (con componentes $E_{ij}$) se obtiene a partir del gradiente del campo de desplazamientos $\mathbf{u}$:

$$
\mathbf{E} = \frac{1}{2}\left(\nabla\mathbf{u} + (\nabla\mathbf{u})^T\right)
\quad\Longleftrightarrow\quad
E_{ij} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right)
= u_{(i,j)}
$$

La evolución espacio-temporal del continuo planetario está restringida por las ecuaciones fundamentales de balance:

- **Ecuación de continuidad de masa con discontinuidades (formulación euleriana):** describe la conservación local de la masa y permite la presencia de interfaces internas discontinuas, como la frontera hielo-océano:

  $$
  \frac{D\rho}{Dt} + \rho\,\operatorname{div}(\mathbf{v}) = 0
  \quad\Longleftrightarrow\quad
  \frac{\partial \rho}{\partial t} + \frac{\partial(\rho v_i)}{\partial x_i} = 0
  $$

  donde $\rho(\mathbf{x},t)$ es la densidad de masa y $\mathbf{v}(\mathbf{x},t)$ es el campo de velocidades materiales.

- **Ecuación de movimiento de Cauchy (conservación de la cantidad de movimiento):** rige el equilibrio dinámico bajo el campo de fuerzas de cuerpo $\mathbf{b}$ (donde $\mathbf{b} = \mathbf{g}$ representa la aceleración gravitatoria planetaria y de marea) y la divergencia del tensor de esfuerzos:

  $$
  \operatorname{div}(\mathbf{\sigma}) + \rho\mathbf{b} = \rho\mathbf{a}
  \quad\Longleftrightarrow\quad
  \sigma_{ij,j} + \rho b_i = \rho\dot{v}_i
  $$

  donde $\mathbf{a} = \dot{\mathbf{v}} = D\mathbf{v}/Dt$ es la aceleración del elemento continuo.

### Comportamiento constitutivo

La caracterización reológica del volumen helado de Encélado exige leyes constitutivas específicas para cada capa térmica y mecánica:

1. **Elasticidad lineal generalizada (ley de Hooke en notación de Voigt):** en la litosfera fría y somera, el comportamiento se modela acoplando el vector de esfuerzos $\{\sigma\} = [\sigma_{11}, \sigma_{22}, \sigma_{33}, \sigma_{23}, \sigma_{13}, \sigma_{12}]^T$ con el vector de deformaciones de ingeniería $\{\varepsilon\} = [E_{11}, E_{22}, E_{33}, 2E_{23}, 2E_{13}, 2E_{12}]^T$ mediante la matriz de rigidez elástica $[\mathcal{C}]$ de dimensión $6\times6$, tal que $\{\sigma\} = [\mathcal{C}]\{\varepsilon\}$. La simetría cristalina y microestructural condiciona el número de constantes elásticas independientes:
   - *Isótropa:* 2 constantes independientes (parámetros de Lamé $\lambda$ y $\mu$, o módulo de Young $E$ y coeficiente de Poisson $\nu$).
   - *Monoclínica:* presenta un plano de simetría estructural (debido a sistemas de fallas paralelas), lo que reduce la matriz a 13 constantes elásticas independientes.
   - *Ortótropa:* caracterizada por 9 constantes independientes, aplicable a capas de hielo con orientación preferencial de microfracturas ortogonales.

2. **Viscoelasticidad lineal:** en el hielo basal cálido y dúctil adyacente al océano subsuperficial, la respuesta atenuativa y disipativa bajo cargas cíclicas se formula integrando el módulo de relajación $E(t)$ y el tiempo de memoria $k_0$. Para un flujo de cortante simple, la relación constitutiva diferencial adopta la forma:

   $$
   \sigma_{21} + k_0\dot{\sigma}_{21} = 2\eta E_{12}
   \quad\Longleftrightarrow\quad
   s_{ij} + k_0\dot{s}_{ij} = 2\eta\dot{e}_{ij}
   $$

   donde $\eta$ es la viscosidad dinámica, $e_{ij}$ es el tensor de tasa de deformación desviadora y $k_0$ representa el tiempo de memoria o tiempo de relajación de Maxwell ($\tau_M = \eta/\mu$). En el hielo basal de Encélado, $k_0$ compite directamente con el periodo de forzamiento orbital de Saturno ($P \approx 1.37\ \text{días} \approx 1.18\times10^5\ \text{s}$), gobernando la disipación termomecánica.

3. **Termoelasticidad y energía libre de Helmholtz:** el acoplamiento entre la deformación mecánica y la temperatura $T$ se formaliza linealizando el potencial de energía libre de Helmholtz por unidad de masa, $\psi(\mathbf{E}, T)$. Siguiendo el desarrollo constitutivo termoelástico, el potencial se expande cuadráticamente:

   $$
   \begin{aligned}
   \psi(\mathbf{E}, T) ={}&
   \frac{1}{2\rho_0}(\mathbf{E} - \mathbf{E}_0) : \mathbb{C} : (\mathbf{E} - \mathbf{E}_0) \\
   &- \frac{1}{\rho_0}(T - T_0)\mathbf{A} : (\mathbf{E} - \mathbf{E}_0) \\
   &+ c_v\left[(T - T_0) - T\ln\left(\frac{T}{T_0}\right)\right]
   \end{aligned}
   $$

   donde $\mathbb{C}$ es el tensor de elasticidad de cuarto orden, $\mathbf{A} = \mathbb{C}:\boldsymbol{\alpha}$ es el tensor de tensiones térmicas ($\boldsymbol{\alpha}$ es el tensor de expansión térmica), $c_v$ es el calor específico a volumen constante y $\rho_0$ es la densidad de referencia a la temperatura $T_0$. Derivando $\mathbf{\sigma} = \rho_0\,\partial\psi/\partial\mathbf{E}$, se obtiene la ecuación constitutiva termoelástica acoplada:

   $$
   \mathbf{\sigma} = \mathbb{C}:(\mathbf{E} - \mathbf{E}_0) - \mathbf{A}(T - T_0)
   $$

### Síntesis comparativa de modelos constitutivos

| Modelo constitutivo | Ecuación o relación tensorial clave | Mecanismo de respuesta física | Relevancia para la capa de hielo de Encélado |
| --- | --- | --- | --- |
| **Elástico lineal (isótropo u ortótropo)** | $\{\sigma\} = [\mathcal{C}]\{\varepsilon\}$ | Respuesta instantánea y completamente reversible; no disipativa. Depende de las constantes elásticas (2 en isótropo, 9 en ortótropo y 13 en monoclínico). | Gobierna la corteza frágil superior (capa somera fría, $T\sim75\ \text{K}$). Dicta la velocidad de propagación de ondas sísmicas P y S de alta frecuencia. |
| **Viscoelástico lineal (modelo de Maxwell)** | $s_{ij} + k_0\dot{s}_{ij} = 2\eta\dot{e}_{ij}$ | Respuesta dependiente del tiempo, con histéresis y atenuación. El tiempo de memoria $k_0 = \eta/\mu$ regula la conversión de energía elástica en disipación viscosa. | Gobierna el hielo basal cálido ($T\sim273\ \text{K}$) cercano al océano. Modula la deformación de marea cíclica en la escala orbital ($P\approx1.37$ días) y la atenuación anelástica ($Q^{-1}$). |
| **Termoelástico acoplado** | $\mathbf{\sigma} = \mathbb{C}:(\mathbf{E} - \mathbf{E}_0) - \mathbf{A}(T - T_0)$ | Acoplamiento bidireccional entre distorsión mecánica, gradientes de temperatura y flujo de calor, derivado del potencial de Helmholtz $\psi(\mathbf{E},T)$. | Origina esfuerzos tectónicos térmicos intensos debido al elevado gradiente geotérmico ($\sim200\ \text{K}$) entre la superficie helada y el océano subsuperficial. |

Los tensores de esfuerzo y los modelos constitutivos viscoelásticos aquí formulados gobiernan formalmente la deformación por mareas dinámicas que sufre la corteza de Encélado, sometida al campo gravitatorio variable de Saturno.

## 2. Acoplamiento gravitacional, forzamiento por mareas y precursores de la tectónica en Encélado

El acoplamiento gravitacional resonante entre Saturno y Encélado genera un forzamiento periódico de marea que actúa como el motor térmico y mecánico primario de este mundo oceánico. Comprender la distribución espacio-temporal de los esfuerzos de marea es esencial para diagnosticar el estado tensional de la litosfera helada, la disipación interna de energía y la génesis de patrones tectónicos en la región polar sur (*South Polar Terrain*, SPT).

### Equilibrio hidrostático y esfuerzos de marea

En ausencia de excentricidad orbital, el interior planetario se encuentra en un estado de esfuerzo esférico e hidrostático, donde el gradiente de presión equilibra las fuerzas de cuerpo:

$$
\nabla p = \rho\mathbf{b}
$$

Debido a la órbita excéntrica ($e\approx0.0047$), Encélado experimenta variaciones periódicas en la magnitud y orientación del potencial de marea de Saturno, que introducen fuerzas de cuerpo dependientes del tiempo:

$$
\mathbf{b}(\mathbf{x},t) = \mathbf{g}_0(\mathbf{x}) + \mathbf{g}_{\text{marea}}(\mathbf{x},t)
$$

La superposición cíclica de tracciones y compresiones descompone el tensor de esfuerzos de Cauchy $\mathbf{\sigma}$ en su componente esférica (presión hidrostática $p = -\frac{1}{3}\operatorname{Tr}(\mathbf{\sigma})$) y el tensor desviador de esfuerzos $\mathbf{s}$:

$$
\mathbf{s} = \mathbf{\sigma} - \frac{1}{3}\operatorname{Tr}(\mathbf{\sigma})\mathbf{1}
\quad\Longleftrightarrow\quad
s_{ij} = \sigma_{ij} - \frac{1}{3}\sigma_{kk}\delta_{ij}
$$

El tensor desviador $\mathbf{s}$ almacena la energía elástica de distorsión. El forzamiento gravitatorio periódico de Saturno induce variaciones cíclicas en los esfuerzos flexurales y cortantes dentro de la corteza helada, con amplitudes del orden de $10$ a $100\ \text{kPa}$. Estas fluctuaciones de esfuerzo desviador son el motor primario que conduce a la nucleación de fallas y a la apertura activa de las fracturas dorsales conocidas como «Franjas de Tigre» (*Tiger Stripes*).

### Criterios de plastificación y fractura

Cuando la magnitud del tensor desviador de esfuerzos $\mathbf{s}$ bajo deformación por mareas supera la resistencia mecánica del hielo policristalino, el material transiciona del régimen elástico hacia la cedencia plástica y el fracturamiento litosférico. El inicio de la plasticidad se evalúa mediante dos criterios fundamentales:

1. **Criterio de fluencia de von Mises:** establece que la plastificación ocurre cuando el segundo invariante del tensor desviador, $J_2 = \frac{1}{2}\mathbf{s}:\mathbf{s} = \frac{1}{2}s_{ij}s_{ij}$, alcanza el límite de cedencia en tracción $\sigma_Y$:

   $$
   \mathcal{F}(J_2,\sigma_Y) = \sqrt{3J_2} - \sigma_Y = 0
   $$

2. **Criterio de esfuerzo cortante máximo de Tresca:** prescribe que la fluencia inelástica se inicia cuando el esfuerzo cortante máximo en el espacio de esfuerzos principales ($\sigma_1 \geq \sigma_2 \geq \sigma_3$) alcanza el límite de cortante puro $k$:

   $$
   \mathcal{F}(\mathbf{\sigma},k) = |\sigma_1 - \sigma_3| - 2k = 0
   \quad\Longleftrightarrow\quad
   \tau_{\max} = \frac{|\sigma_1 - \sigma_3|}{2} = k
   $$

En el espacio de esfuerzos principales, la función $\mathcal{F}(\mathbf{\sigma}) = 0$ define la superficie de fluencia. El gradiente tensorial de esta superficie determina la dirección del tensor de tasa de deformación plástica mediante el vector normal de flujo plástico:

$$
\mathbf{n} = \nabla_{\mathbf{\sigma}}\mathcal{F}
= \frac{\partial\mathcal{F}}{\partial\mathbf{\sigma}}
$$

Para el criterio de von Mises, al diferenciar $J_2 = \frac{1}{2}s_{kl}s_{kl}$ con respecto al tensor de esfuerzos de Cauchy $\mathbf{\sigma}$ (donde $\partial s_{kl}/\partial\sigma_{ij} = \delta_{ik}\delta_{jl} - \frac{1}{3}\delta_{ij}\delta_{kl}$), se obtiene exactamente $\partial J_2/\partial\mathbf{\sigma} = \mathbf{s}$. Aplicando la regla de la cadena:

$$
\begin{aligned}
\mathbf{n}
&= \frac{\partial\mathcal{F}}{\partial\mathbf{\sigma}}
= \frac{\partial(\sqrt{3J_2} - \sigma_Y)}{\partial\mathbf{\sigma}} \\
&= \frac{1}{2}(3J_2)^{-1/2}\cdot 3\frac{\partial J_2}{\partial\mathbf{\sigma}}
= \frac{3}{2\sqrt{3J_2}}\mathbf{s}
= \sqrt{\frac{3}{2}}\frac{\mathbf{s}}{\|\mathbf{s}\|}
\end{aligned}
$$

donde $\|\mathbf{s}\| = \sqrt{\mathbf{s}:\mathbf{s}} = \sqrt{2J_2}$. La normal de flujo $\mathbf{n}$ dicta la cinemática de la deformación inelástica irreversible y actúa como precursor mecánico de la falla tectónica en la litosfera helada.

### Desglose de mecanismos tectónicos

La conversión de las fuerzas de marea gravitacionales en la estructura tectónica observada en Encélado sigue cuatro fases mecánicas encadenadas:

1. **Acumulación de esfuerzo desviador:** las fuerzas de cuerpo periódicas $\mathbf{g}_{\text{marea}}(t)$ distorsionan la corteza, incrementando cíclicamente la magnitud del tensor desviador $\mathbf{s}$ y acumulando energía de deformación elástica.
2. **Relajación viscoelástica cíclica:** en el hielo basal subsuperficial cálido, los esfuerzos desviadores se atenúan térmicamente a escalas de tiempo gobernadas por el tiempo de memoria $k_0 = \eta/\mu$. Este proceso convierte energía mecánica en calor mediante disipación viscoelástica y concentra los esfuerzos residuales en la litosfera fría somera.
3. **Superación del límite de cedencia plástica:** cuando los esfuerzos acumulados en la litosfera superior violan el criterio de von Mises ($\sqrt{3J_2} \geq \sigma_Y$) o el de Tresca ($|\sigma_1 - \sigma_3| \geq 2k$), el estado tensional alcanza la superficie de fluencia $\mathcal{F} = 0$.
4. **Generación de fracturas sísmicamente activas:** el flujo inelástico orientado por la normal $\mathbf{n}$ induce la nucleación y propagación de fallas por cizalla y grietas de tracción, como las *Tiger Stripes*. Esto genera sismicidad tectónica activa y abre conductos para el criovolcanismo.

La estructura fracturada, heterogénea y anisotrópica resultante de esta actividad tectónica de mareas altera de forma determinante la velocidad, el patrón de atenuación y la dirección de propagación de las ondas sísmicas en la corteza helada.

## 3. Modelado del campo de ondas sísmicas: heterogeneidad 3D y efecto de guía de onda en la corteza

La interpretación de la estructura interna de Encélado mediante sismología planetaria exige simular cuantitativamente la propagación del campo de ondas sísmicas en modelos tridimensionales de velocidad complejos. Los análisis numéricos de elastodinámica planetaria (tales como los desarrollados por Dapré e Irving) demuestran que las variaciones laterales 3D en el espesor de la capa de hielo y las propiedades reológicas del interior distorsionan severamente el frente de onda sísmico y condicionan la firma espectral observable en la superficie.

### Fenomenología de ondas en medios heterogéneos

Al propagarse por el interior de Encélado, el campo de ondas elásticas interactúa con tres dominios mecánicos principales: la litosfera de hielo I$_h$, el océano subsuperficial salino y el núcleo poroso de silicatos. En las interfaces cinemáticas mayores ocurren los siguientes fenómenos:

- **Reflexión y refracción en interfaces de impedancia:** la energía de las ondas compresionales (P) y de cortante (S) se particiona según el contraste de impedancia acústica ($Z = \rho V$). En la interfaz corteza-océano (definida mecánicamente en $z = d_{\text{corteza}}$), el módulo de rigidez del fluido se anula ($\mu_{\text{océano}} = 0$, $V_{s,\text{océano}} = 0$). En consecuencia, el coeficiente de reflexión para ondas S incidentes desde la corteza es $|R_{SS}| = 1$, lo que impide totalmente la transmisión de ondas de cortante al océano.
- **Conversión de fases y dispersión 3D:** las variaciones tridimensionales del espesor cortical ($\sim5\ \text{km}$ en el polo sur frente a $\sim35\ \text{km}$ en el ecuador) provocan una dispersión espacial del frente de onda, inducen reflexiones múltiples e interfieren destructivamente con las fases profundas de menor amplitud.

### La corteza de hielo como guía de onda sísmica (*ice shell waveguide*)

El comportamiento elastodinámico dominante en la litosfera de Encélado es la formación de una **guía de onda sísmica hiper-eficiente** (*ice shell waveguide*).

La física de esta guía de onda está gobernada por las condiciones de frontera de la capa helada: la superficie libre superior ($z = 0$, con tracciones nulas, $\mathbf{\sigma}\cdot\mathbf{n} = \mathbf{0}$) y la interfaz basal hielo-océano ($z = d_{\text{corteza}}$). Dado que el océano líquido es incapaz de sostener esfuerzos cortantes ($V_s = 0$), la frontera basal actúa mecánicamente como un límite blando ideal para las ondas transversales y refleja totalmente las ondas $S_{\text{ice}}$ mediante reflexión interna total.

Como resultado, la energía liberada por fuentes sísmicas someras (tales como fallamiento tectónico por marea o actividad criovolcánica en las *Tiger Stripes*) queda atrapada eficientemente dentro del volumen de la corteza. Esta canalización genera una cascada de reflexiones múltiples ($P_{\text{ice}}P_{\text{ice}}$, $S_{\text{ice}}S_{\text{ice}}$) y estimula modos de ondas de superficie de alta amplitud (Rayleigh y Love), lo que restringe severamente la proporción de energía cinética que logra refractarse hacia abajo a través del océano y alcanzar el núcleo rocoso.

### Matriz comparativa de propagación sísmica

| Propagación canalizada en la corteza (*ice shell waveguide*) | Fases transmitidas a las capas profundas (océano y núcleo) |
| --- | --- |
| **Fases dominantes:** ondas de superficie (Rg, Love) y múltiples corticales atrapadas ($P_{\text{ice}}P_{\text{ice}}$, $S_{\text{ice}}S_{\text{ice}}$, $P_{\text{ice}}S_{\text{ice}}$). | **Fases dominantes:** ondas compresionales transmitidas por el núcleo ($P_{\text{core}}$, PKP) y reflexiones en el fondo oceánico/núcleo ($P_{\text{ocean}}P$, ScP). |
| Retiene mecánicamente la mayor parte de la energía elástica de fuentes someras debido a la reflexión interna total en la interfaz hielo-océano ($\mu_{\text{océano}} = 0$). | Atraviesan la frontera hielo-océano como ondas $P_{\text{ocean}}$, penetran en la matriz porosa del núcleo rocoso y allí se reconvierten parcialmente a $S_{\text{core}}$. |
| Amplitudes elevadas y trenes de onda de larga duración que dominan el sismograma en estaciones de superficie. | Amplitudes fuertemente reducidas (varios órdenes de magnitud menores que las de la guía de onda) debido a pérdidas por refracción y divergencia esférica. |
| Alta sensibilidad a la estructura litosférica somera, los gradientes térmicos, la densidad de microfracturas y las variaciones 3D del espesor de la corteza. | Transportan la firma diagnóstica directa del espesor absoluto de la capa de agua, la rigidez del núcleo y la porosidad de la matriz de silicatos. |

El atrapamiento en la guía de onda cortical implica que la detección de fases sísmicas profundas desde la superficie depende críticamente de métodos avanzados de procesamiento espectral e instrumentalización optimizada.

## 4. Sismología global del interior: fases transmitidas por el núcleo y diagnóstico para misiones en la superficie

La exploración sismológica *in situ* de Encélado estará condicionada por el despliegue de una estación sísmica única en la superficie planetaria. Para superar la limitación que supone la escasez de estaciones y el enmascaramiento por la guía de onda cortical, la sismología global debe explotar las firmas espectrales y cinemáticas de las fases sísmicas que muestrean el interior profundo, lo que permitirá desentrañar la porosidad del núcleo rocoso, el espesor del océano y la estructura interna global.

### Análisis de fases profundas (reflejadas y transmitidas por el núcleo)

Las ondas sísmicas que logran escapar del atrapamiento en la corteza y viajan a través del océano subsuperficial proporcionan un diagnóstico directo sobre la reología de la frontera núcleo-océano (COB/CMB):

- **Fases transmitidas por el núcleo (equivalentes a $P_{\text{core}}$ y PKP):** están compuestas por energía compresional que se refracta hacia el océano, ingresa al núcleo poroso de silicatos, se propaga como onda de matriz o de poro y retorna a la corteza. Una elevada porosidad en el núcleo reduce drásticamente el módulo de incompresibilidad efectivo ($K_{\text{core}}$) y las velocidades sísmicas ($V_p$, $V_s$), lo que induce retrasos cinemáticos medibles y atenuación espectral por flujo de fluido intergranular.
- **Fases reflejadas en la COB (equivalentes a $P_{\text{ocean}}P$ y ScP):** son fases que rebotan en la interfaz entre el océano líquido y la superficie del núcleo rocoso. La relación de amplitud entre la llegada reflejada en la COB ($P_{\text{ocean}}P$) y la llegada transmitida ($P_{\text{core}}$) permite discriminar entre variaciones en el espesor del océano y cambios en la porosidad del núcleo.

### Restricciones para misiones de sismología en la superficie

El modelado elastodinámico 3D expone restricciones operativas críticas para la recolección de datos sísmicos desde un único sismómetro en Encélado:

1. **Sombra de guía de onda y distancia epicentral:** la amplitud de las fases transmitidas por el núcleo varía de manera no lineal con la distancia angular ($\Delta$) desde los epicentros activos en el polo sur. A distancias intermedias, las ondas globales quedan eclipsadas por la llegada de alta amplitud de las ondas atrapadas en la corteza helada.
2. **Efecto topográfico de la interfaz basal:** las variaciones laterales del espesor de la corteza actúan como lentes elásticas y distorsionan los tiempos de viaje de las fases globales. Se requieren métodos de cocientes espectrales horizontal a vertical (H/V) y de funciones de receptor para aislar las respuestas del interior sin sesgos topográficos.

### Recomendaciones de diagnóstico sísmico

Para maximizar el retorno científico de futuras misiones sismológicas en la superficie de Encélado, se establecen las siguientes directrices geotécnicas y analíticas:

- **Identificación de fases clave:** priorizar a bordo algoritmos de filtrado polarizado y trazado de rayos para aislar las llegadas de baja amplitud $P_{\text{ocean}}P$ y $P_{\text{core}}$, separándolas de la reverberación estocástica dominada por la guía de onda de la corteza helada.
- **Distribución epicentral:** emplazar el módulo sísmico en ubicaciones que optimicen la distancia angular respecto a la región polar sur ($\Delta\sim30^\circ$ a $90^\circ$), donde la geometría de emisión permite que las fases transmitidas por el núcleo emerjan fuera de la ventana temporal codal de mayor amplitud de las ondas de superficie atrapadas.
- **Discriminación de la porosidad del núcleo:** utilizar cocientes espectrales de alta frecuencia y análisis de dispersión de fase entre $P_{\text{ocean}}P$ y $P_{\text{core}}$ para cuantificar la porosidad del núcleo. Un núcleo altamente poroso permeado por agua genera un corrimiento espectral distintivo hacia frecuencias más bajas debido a la atenuación anelástica ($Q^{-1}$) por fricción de fluido en la matriz rocosa.

La integración analítica de la mecánica de medios continuos, el forzamiento de marea viscoelástico y la sismología global 3D constituye la herramienta decisiva para interpretar las señales registradas en superficie y descifrar la estructura interna inexplorada de los mundos oceánicos helados.