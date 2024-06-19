# Practica de refactor

## Integrantes
- Mariajulia Romani Tafur
- Sofia Herrera Salazar

## Evaluación del código resultante


### Nombres Claros y Representativos

**Clase Voto:**
- Los atributos (`region`, `provincia`, `distrito`, `dni`, `candidato`, `esvalido`) tienen nombres claros que representan los datos asociados a cada voto.

**Clase CalculaGanador:**
- Los métodos (`leerDatos`, `contarVotosValidos`, `calcularPorcentajes`, `calcularGanador`) tienen nombres que describen claramente su función.

**Variables locales:**
- Las variables locales como `votosxcandidato`, `porcentajes`, `candidatos_ordenados` son representativas de los datos que almacenan.

### Funciones Cortas y Sin Efectos Colaterales

**Métodos de CalculaGanador:**
- `leerDatos`: Lee un archivo CSV y devuelve una lista de objetos Voto.
- `contarVotosValidos`: Cuenta los votos válidos para cada candidato.
- `calcularPorcentajes`: Calcula los porcentajes de votos válidos para cada candidato.
- `calcularGanador`: Determina el ganador o los candidatos que pasan a segunda vuelta según los criterios especificados.

Cada método realiza una tarea específica y no causa efectos colaterales indeseados en el estado de la aplicación más allá de su función declarada.

### Comentarios Innecesarios

- **Código legible:** En general, el código es legible sin necesidad de comentarios adicionales. Los nombres de métodos y variables son descriptivos y explican por sí mismos qué hace cada parte del código.
  
