# proyectoBigDataTelematica

Proyecto relacionado a la utilización de la tecnología big data para resolver un problema. Esto se hace con Apache Spark.

## División del trabajo
Preparación de datos: Maria Camila Calle
Buscador: Maria Camila Calle

## Proceso

Se utilizó databricks para este proyecto, la limpieza de palabras y la eliminación de palabras de longitud 1 se realizó facilmente con la ayuda de expresiónes regulares, esto ayuda además, a quitar stopwords por medio de StopWordsRemover, una libreria de pyspark (Cabe aclarar, que esto solo funciona en inglés).

La búsqueda fue realizada con un Índice invertido y la posibilidad de recibir palabras por teclado (la cual fue una dificultad principal a la hora de realizar este trabajo por medio de databricks) se realizó con la ayuda de dbutils.widgets, el cual viene instalado por defecto en databricks.

##  Notebook

El archivo de notebook y el archivo Html estan en la carpeta code de este mismo git