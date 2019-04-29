# proyectoBigDataTelematica

Proyecto relacionado a la utilizaci�n de la tecnolog�a big data para resolver un problema. Esto se hace con Apache Spark.

## Divisi�n del trabajo
Preparaci�n de datos: Maria Camila Calle
Buscador: Maria Camila Calle

## Proceso

Se utiliz� databricks para este proyecto, la limpieza de palabras y la eliminaci�n de palabras de longitud 1 se realiz� facilmente con la ayuda de expresi�nes regulares, esto ayuda adem�s, a quitar stopwords por medio de StopWordsRemover, una libreria de pyspark (Cabe aclarar, que esto solo funciona en ingl�s).

La b�squeda fue realizada con un �ndice invertido y la posibilidad de recibir palabras por teclado (la cual fue una dificultad principal a la hora de realizar este trabajo por medio de databricks) se realiz� con la ayuda de dbutils.widgets, el cual viene instalado por defecto en databricks.

##  Notebook

El archivo de notebook y el archivo Html estan en la carpeta code de este mismo git