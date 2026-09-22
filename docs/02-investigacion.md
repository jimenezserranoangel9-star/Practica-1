# Investigación: Qué es la Teoría de la Computación
**Unidad Temática I - Fundamentos Lógico-Matemáticos**  
*Documento de Investigación Estudiantil*

---

## 1. Introducción
En este documento se abarcan los fundamentos de la Teoría de la Computación. Se analizan de forma profunda las definiciones principales de la disciplina, sus orígenes históricos vinculados al programa de Hilbert, las paradojas lógicas y el *Entscheidungsproblem*. Asimismo, se desglosan sus tres ramas fundamentales (computabilidad, complejidad y autómatas), la importancia de la Tesis de Church-Turing, y los conceptos formales de lenguajes, alfabetos y operaciones sobre cadenas. Finalmente, se explica la jerarquía de Chomsky y se formaliza la definición de autómatas finitos, destacando su equivalencia y aplicaciones en el mundo real.

---

## 2. ¿Qué es la Teoría de la Computación y qué preguntas se plantea?
La Teoría de la Computación es el pilar teórico de las ciencias de la computación y la ingeniería en sistemas. Trata de descubrir qué problemas pueden ser resueltos mediante algoritmos y, de ser así, con qué nivel de eficiencia en cuanto a tiempo y memoria.

Existen múltiples formas de definirla:
* **Hopcroft et al.:** Se define como "el estudio de los fundamentos lógicos y matemáticos de la computación, centrada en los límites de lo que las máquinas abstractas pueden y no pueden hacer".
* **Kelley:** La define como "la rama de la informática que trata de qué puede ser computado y qué recursos son necesarios para hacerlo, estableciendo modelos matemáticos de las computadoras".
* **Programa Sintético del IPN:** Se concibe como una asignatura crítica para fundamentar el diseño de compiladores y el análisis de algoritmos.

La disciplina busca responder a preguntas trascendentales:
* ¿Cuáles son los límites fundamentales del procesamiento de información?
* ¿Existe algún algoritmo para resolver determinado problema matemático?
* ¿Qué hace que algunos problemas sean intratables computacionalmente, incluso con el hardware más avanzado?

---

## 3. Sus orígenes: el programa de Hilbert y las paradojas
La Teoría de la Computación tiene sus raíces en las matemáticas de principios del siglo XX con el **programa de Hilbert**. David Hilbert propuso fundamentar todas las matemáticas en un conjunto finito y estricto de axiomas, demostrando que este sistema era **consistente** (sin contradicciones) y **completo** (toda afirmación verdadera se podía demostrar).

Dentro de este proyecto surgió el ***Entscheidungsproblem*** (problema de decisión), el cual preguntaba si existía un procedimiento mecánico (algoritmo) que pudiera decidir automáticamente si cualquier afirmación matemática dada era verdadera o falsa.

Sin embargo, el proyecto enfrentó grandes límites:
1. **Paradoja de Russell:** Demostró fallas en la teoría de conjuntos ingenua mediante la paradoja del conjunto de todos los conjuntos que no se contienen a sí mismos.
2. **Teoremas de Incompletitud de Kurt Gödel (1931):** Demostraron que ningún sistema axiomático complejo puede ser a la vez consistente y completo.
3. **Alan Turing y Alonzo Church:** Demostraron que el *Entscheidungsproblem* no tiene solución. Turing creó la *Máquina de Turing* y demostró que no existe un algoritmo universal para decidir la verdad de cualquier enunciado.

---

## 4. Las Tres Ramas de la Teoría

### 4.1 Teoría de Autómatas y Lenguajes Formales
Responde a: *¿Cómo modelamos matemáticamente el cálculo y el procesamiento de cadenas de texto?*  
Define máquinas abstractas (autómatas) y reglas de sintaxis (gramáticas), desde autómatas finitos simples (implementables en hardware como un GAL22V10 mediante VHDL) hasta máquinas complejas.

### 4.2 Teoría de la Computabilidad
Responde a: *¿Qué problemas pueden ser resueltos por una computadora y cuáles son inherentemente irresolubles?*  
Clasifica problemas en decidibles e indecidibles. Un ejemplo es el **Problema de la Parada (Halting Problem)** demostrado por Turing: es imposible escribir un programa que analice a otro y determine si terminará o se quedará en un bucle infinito.

### 4.3 Teoría de la Complejidad Computacional
Responde a: *¿Qué hace que algunos problemas sean computacionalmente fáciles y otros prácticamente imposibles?*  
Estudia los recursos (tiempo y memoria RAM) necesarios para un algoritmo, clasificando problemas en clases como **P** (resoluble en tiempo polinomial) y **NP** (fáciles de verificar, pero presuntamente lentos de encontrar).

---

## 5. La Tesis de Church-Turing
Afirma que cualquier función que sea efectivamente calculable por un ser humano siguiendo un algoritmo puede ser calculada por una **Máquina de Turing**.

Se demostró matemáticamente que tres sistemas desarrollados de forma independiente son totalmente equivalentes:
* El Cálculo Lambda ($\lambda$-cálculo) de Alonzo Church.
* La Máquina de Turing de Alan Turing.
* Las Funciones Recursivas Parciales de Gödel-Herbrand.

### ¿Por qué se denomina "tesis" y no "teorema"?
Un teorema relaciona dos conceptos formales mediante una demostración matemática. La Tesis de Church-Turing relaciona un concepto rígidamente formalizado (la Máquina de Turing) con una noción intuitiva e informal (el "cálculo efectivo" o algoritmo humano). Al no poder formalizar la "intuición", no puede ser demostrada con un teorema estricto, pero se acepta por carecer de contraejemplos.

---

## 6. Conceptos Formales: Alfabeto, Cadena y Lenguaje

* **Alfabeto ($\Sigma$):** Conjunto finito y no vacío de símbolos indivisibles. Ejemplo: $\Sigma = \{0, 1\}$.
* **Cadena ($w$):** Secuencia finita de símbolos de un alfabeto. Su longitud se denota como $\vert{}w\vert{}$. Existe la cadena vacía, denotada como $\lambda$ o $\epsilon$ ($\vert{}\lambda\vert{} = 0$).
* **Lenguaje ($L$):** Conjunto de cadenas formadas a partir de un alfabeto ($L \subseteq \Sigma^*$).

### 6.1 Las operaciones formales
* **Concatenación de cadenas:** Unir dos cadenas ($x=01, y=11 \implies xy=0111$).
* **Concatenación de lenguajes:** $L_1 L_2 = \{xy \mid x \in L_1, y \in L_2\}$.
* **Potencia ($L^n$):** Concatenar un lenguaje consigo mismo $n$ veces ($L^2 = LL$).
* **Reflexión ($L^R$):** Cadenas leídas al revés.
* **Unión ($L_1 \cup L_2$):** Cadenas que pertenecen a $L_1$, $L_2$ o ambos.
* **Intersección ($L_1 \cap L_2$):** Cadenas presentes en ambos lenguajes.
* **Diferencia ($L_1 - L_2$):** Cadenas en $L_1$ que no están en $L_2$.
* **Cerradura de Kleene ($\Sigma^*$):** Conjunto infinito de todas las cadenas posibles, **incluyendo** la cadena vacía ($\lambda$).
* **Cerradura Positiva ($\Sigma^+$):** Conjunto de cadenas de longitud 1 o mayor (**excluyendo** $\lambda$).
* **¿Por qué $\Sigma^0 = \{\lambda\}$?:** La potencia cero genera cadenas de longitud cero. La única secuencia de longitud cero es la cadena vacía ($\lambda$). Por tanto, el conjunto contiene un único elemento neutro.
* **Diferencia entre $\Sigma^*$ y $\Sigma^+$:** Se expresa como $\Sigma^* = \Sigma^+ \cup \{\lambda\}$.

---

## 7. La Jerarquía de Chomsky

Propuesta por Noam Chomsky, clasifica los lenguajes formales según la estructura de sus reglas de producción:

| Tipo | Gramática | Máquina que lo reconoce |
| :---: | :--- | :--- |
| **0** | Irrestricta (Recursivamente enumerable) | Máquina de Turing (MT) |
| **1** | Sensible al contexto | Autómata Linealmente Acotado (LBA) |
| **2** | Libre de contexto | Autómata de Pila (Push-down Automaton) |
| **3** | Regular | Autómata Finito (AFD / AFN) |

---

## 8. Autómatas Finitos y Expresiones Regulares

### Autómata Finito Determinista (AFD)
Se define como una quintupla $M = (Q, \Sigma, \delta, q_0, F)$:
* $Q$: Conjunto finito de estados.
* $\Sigma$: Alfabeto de entrada.
* $\delta: Q \times \Sigma \rightarrow Q$: Función de transición unívoca.
* $q_0 \in Q$: Estado inicial.
* $F \subseteq Q$: Conjunto de estados finales o de aceptación.

### Autómata Finito No Determinista (AFN)
Su función de transición mapea hacia el conjunto potencia de los estados: $\delta: Q \times \Sigma \rightarrow \mathcal{P}(Q)$. Puede estar en múltiples estados simultáneamente. A pesar de esto, **el AFD y el AFN son equivalentes en potencia de cómputo**. El algoritmo de *Construcción de subconjuntos* permite transformar cualquier AFN en un AFD.

### 8.1 Aplicaciones Reales de las Expreiones Regulares
1. **Análisis Léxico en Compiladores e Intérpretes:** Agrupación de caracteres en *tokens* (palabras clave, operadores, identificadores).
2. **Validación de Integridad en Formularios y BD:** Verificación de formatos de correo, teléfonos y prevención de Inyección SQL en sistemas como PostgreSQL o MySQL.
3. **Búsqueda y Reemplazo de Patrones Complejos:** Uso de herramientas como `grep` o IDEs para manipular archivos masivos de código.

---

## 9. Conclusión
La Teoría de la Computación conecta conceptos abstractos (paradojas lógicas, autómatas, lenguajes formales) con aplicaciones prácticas en la ingeniería de software moderna, como compilar lenguajes, proteger bases de datos y manipular flujos de información estructurada.

---

## Referencias
* [1] F. Díaz Barriga y G. Hernández Rojas, *Estrategias docentes para un aprendizaje significativo*. México: McGraw Hill, 2016.
* [2] H. Díaz, *Lenguajes y autómatas*. Universidad Autónoma Metropolitana, 2020.
* [3] A. Hodges, "Alan Turing home page," [Online]. Available: https://www.turing.org.uk/index.html.
* [4] J. E. Hopcroft, *TEORÍA DE AUTÓMATAS, LENGUAJES Y COMPUTACIÓN*, 3rd ed. Addison-Wesley, 2007.
* [5] Instituto Politécnico Nacional, *Programa sintético: Teoría de la Computación*. Escuela Superior de Cómputo (ESCOM), 2020.
* [6] D. Kelley, *Teoría de autómatas y lenguajes formales*. Prentice Hall, 2001.