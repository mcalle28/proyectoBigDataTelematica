# proyectoBigDataTelematica

Proyecto relacionado a la utilización de la tecnología big data para resolver un problema. Esto se hace con Apache Spark.

## División del trabajo

Preparación de datos: Maria Camila Calle

Buscador: Maria Camila Calle


## 1.Diseño

### 1.1 Metodología de desarrollo

La metodología de desarrollo del proyecto fue CRISP-DM, en la cual se identifican 6 fases principales para la minería de datos:
![imagenframework](https://emba.epfl.ch/wp-content/uploads/2018/04/CRISP-DM-01.png)


_Figura 1: Entendimiento de las fases de CRISP-DM._

Cada una de las fases para el proyecto se realizó de la siguiente manera y en el orden indicado por el framework:

**Entendimiento del negocio**

Referirse al punto 1.2 de este documento.

**Entendimiento de los datos**

Referirse al punto 1.3 de este documento.

**Preparación de los datos**

Para que los datos provenientes de los CSV estuvieran disponibles a cualquier operación realizada en el desarrollo se realizaron los siguientes pasos:

- Creación de cada dataframe basado en uno de los tres archivos .csv
- Unión de los 3 dataframes en uno.
- Creación de un nuevo dataframe que contuviera sólo las columnas necesarias(ID, Título y Contenido)
- Tokenización de todas las palabras disponibles.
- Limpieza de caracteres especiales por medio de una expresión regular.
- Limpieza de palabras de longitud 1.
- Limpieza de stopwords en el idioma inglés.
- Eliminación o reemplazo de filas nulas.

Con esto los datos están listos para cualquier modelo necesario en la solución del problema.

**Modelado**

Para  el modelado de la solución, gracias a los datos obtenidos en la limpieza, se realizó un índice invertido (una estructura de datos utilizada para la búsqueda y recuperación de información). Los pasos para realizarlo fueron:

- Tokenización: Como se dicta en la limpieza de datos, cada palabra en cada documento fue tokenizada y separada por comas.
- Normalización: Se evitó la parte de normalización(organización de las palabras en su origen “canónico” ó módulos lingüísticos)  ya que fue considerada no necesaria para la solución de este problema.
- Indexación: Creación de una columna para cada palabra, y una columna que describiera la ID del documento en la que se encuentra, además de  la cantidad de veces que se encuentra en dicho documento. En esta parte también se decidió probar con otro índice que mostrará por cada documento, cuáles palabras existían y su cantidad.

Gracias a esto, se logró llegar al índice esperado, y mejorar la búsqueda de dichas palabras en el dataframe.

**Evaluación**

Con las pruebas realizadas en el modelo o estructura de datos definido en el punto anterior, se encontraron errores que llevaron a analizar de nuevo el problema y mejorarlo hasta que se tuviera una solución correcta del mismo.
Referirse al punto 5 de este documento para más información sobre las pruebas.

**Despliegue**

El despliegue del producto final se realizó en el cluster de Databricks, en un notebook que provee de varias librerías de machine learning y manejo SQL, desde ahí se realizaron todas las fases de limpieza, modelado y evaluación.


### 1.2 Entendimiento del problema

Se tienen distintos archivos (verificar 1.3 Entendimiento de datos para más contexto) que contienen información de más de 100.000 noticias realizadas por distintos periódicos, con ellos y una palabra clave introducida por teclado, se necesita buscar las 5 noticias que sean más relevantes de acuerdo a la misma palabra. Para ello, se supondrá que las noticias que más contienen la misma son las más relevantes respecto a la temática.

Con esta introducción se puede encontrar cuales son los pasos a seguir:

- Limpiar los datos, removiendo stopwords y caracteres especiales que puedan evitar que el contador funcione correctamente.
- Realizar con word count especial, que cuente no solo cada palabra, si no que por cada articulo cuente cuántas veces aparece cada una de las palabras.
- Organizar los datos en modo de índice invertido.
- Implementar la búsqueda, la cual recibe una palabra, y gracias a la estructura de índice invertido, encuentra las noticias que más la contengan.

Todos los pasos dictados anteriormente son necesarios para la correcta solución del problema, y específicamente, el índice invertido ayuda mucho al mismo, ya que provee de una estructura muy útil al momento de realizar la búsqueda.

### 1.3 Entendimiento de los datos

Link a los datos:https://www.kaggle.com/snapcrack/all-the-news

Los datos recibidos provienen de kaggle, una comunidad en línea de análisis de datos y machine learning. Dicha información contiene la recopilación de varias noticias de distintos periódicos estadounidenses a lo largo de varios años, tales como: New York Times, CNN, Buzzfeed, etcétera.

Contienen 3 archivos .csv, cada uno contiene 50.000 noticias y pesa 200 MB aproximadamente,  todos estos se encuentran divididos en columnas que contienen la siguiente información:

- Id de la noticia
- Título
- Entidad que la publicó
- Nombre del autor
- Fecha de la publicación
- Mes de la publicación
- Año de la publicación
- Url del Artículo
- Contenido de la noticia 

Para el problema, los datos mayoritariamente necesarios y relevantes son la Id, El título y el contenido del mismo, columnas en las cuales se encuentran la mayor cantidad de palabras con importancia en las noticias.


### 1.4 APIs de Analítica

Las librerías que se utilizaron en la solución del problema fueron principalmente de pyspark, entre ellas, librerías relacionadas con el manejo de base de datos sql (tales como col para revisar y modificar las columnas, además de udf para crear funciones personales a llamar con los datos) y otras relacionadas con el aprendizaje de máquinas, conteniendo algunos puntos de limpieza de datos, tales cómo:

- Desde pyspark.ml.feature: RegexTokenizer, para dividir las distintas palabras en tokens por medio de una expresión regular, además de eso, ayuda a remover palabras de longitud 1.
- Desde pyspark.ml.feature: StopWordsRemover, para remover las stopword en inglés.
- Desde pyspark.ml.feature: HashingTF, IDF,Tokenizer esto fue utilizado como prueba para resolver el peso de las palabras, pero ya que no se realizó el punto 2, al final tuvo poca utilidad. Con esto se pueden crear estructuras de datos que tienen el peso de cada palabra en dicho documento, y evaluarlas además de organizarlas.

### 2.Desarrollo

El proceso de desarrollo se encuentra incluido en el notebook.

### 3.Pruebas

Las pruebas fueron realizadas en el mismo notebook que provee este github, el cual también se encuentra en databricks, para el correcto funcionamiento de la solución se realizaron:

- Pruebas unitarias con cada CSV, centrándose en el correcto control de los datos limpios
- Pruebas con los CSVs unidos, consultando distintas palabras en los mismos para analizar las respuestas

Con esto se pudo verificar el funcionamiento del algoritmo y la limpieza de los datos.

### 4.Instalación 

Gracias al ambiente que provee databricks, no se necesito instalar ninguna de las APIs utilizadas (descritas en el punto 1.4), lo único que se realizó fue la subida de los CSVs para su utilización.

### 5.Ejecución

La ejecución se realiza automáticamente en el notebook del cluster de databricks, cada que se necesite re-hacer un comando se debe oprimir ctrl shift en dicho comando y comenzará a ejecutarse
