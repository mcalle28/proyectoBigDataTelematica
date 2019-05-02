# proyectoBigDataTelematica

Proyecto relacionado a la utilizaci�n de la tecnolog�a big data para resolver un problema. Esto se hace con Apache Spark.

## Divisi�n del trabajo
Preparaci�n de datos: Maria Camila Calle /n
Buscador: Maria Camila Calle


##1.Dise�o

###1.1 Metodolog�a de desarrollo

La metodolog�a de desarrollo del proyecto fue CRISP-DM, en la cual se identifican 6 fases principales para la miner�a de datos:

Figura 1: Entendimiento de las fases de CRISP-DM.

Cada una de las fases para el proyecto se realiz� de la siguiente manera y en el orden indicado por el framework:

**Entendimiento del negocio**

Referirse al punto 1.2 de este documento.

**Entendimiento de los datos**

Referirse al punto 1.3 de este documento.

**Preparaci�n de los datos**

Para que los datos provenientes de los CSV estuvieran disponibles a cualquier operaci�n realizada en el desarrollo se realizaron los siguientes pasos:

-Creaci�n de cada dataframe basado en uno de los tres archivos .csv
-Uni�n de los 3 dataframes en uno.
-Creaci�n de un nuevo dataframe que contuviera s�lo las columnas necesarias(ID, T�tulo y Contenido)
-Tokenizaci�n de todas las palabras disponibles.
-Limpieza de caracteres especiales por medio de una expresi�n regular.
-Limpieza de palabras de longitud 1.
-Limpieza de stopwords en el idioma ingl�s.
-Eliminaci�n o reemplazo de filas nulas.

Con esto los datos est�n listos para cualquier modelo necesario en la soluci�n del problema.

**Modelado**

Para  el modelado de la soluci�n, gracias a los datos obtenidos en la limpieza, se realiz� un �ndice invertido (una estructura de datos utilizada para la b�squeda y recuperaci�n de informaci�n). Los pasos para realizarlo fueron:

-Tokenizaci�n: Como se dicta en la limpieza de datos, cada palabra en cada documento fue tokenizada y separada por comas.
-Normalizaci�n: Se evit� la parte de normalizaci�n(organizaci�n de las palabras en su origen �can�nico� � m�dulos ling��sticos)  ya que fue considerada no necesaria para la soluci�n de este problema.
-Indexaci�n: Creaci�n de una columna para cada palabra, y una columna que describiera la ID del documento en la que se encuentra, adem�s de  la cantidad de veces que se encuentra en dicho documento. En esta parte tambi�n se decidi� probar con otro �ndice que mostrar� por cada documento, cu�les palabras exist�an y su cantidad.

Gracias a esto, se logr� llegar al �ndice esperado, y mejorar la b�squeda de dichas palabras en el dataframe.

**Evaluaci�n**

Con las pruebas realizadas en el modelo o estructura de datos definido en el punto anterior, se encontraron errores que llevaron a analizar de nuevo el problema y mejorarlo hasta que se tuviera una soluci�n correcta del mismo.
Referirse al punto 5 de este documento para m�s informaci�n sobre las pruebas.

**Despliegue**

El despliegue del producto final se realiz� en el cluster de Databricks, en un notebook que provee de varias librer�as de machine learning y manejo SQL, desde ah� se realizaron todas las fases de limpieza, modelado y evaluaci�n.


###1.2 Entendimiento del problema

Se tienen distintos archivos (verificar 1.3 Entendimiento de datos para m�s contexto) que contienen informaci�n de m�s de 100.000 noticias realizadas por distintos peri�dicos, con ellos y una palabra clave introducida por teclado, se necesita buscar las 5 noticias que sean m�s relevantes de acuerdo a la misma palabra. Para ello, se supondr� que las noticias que m�s contienen la misma son las m�s relevantes respecto a la tem�tica.

Con esta introducci�n se puede encontrar cuales son los pasos a seguir:

-Limpiar los datos, removiendo stopwords y caracteres especiales que puedan evitar que el contador funcione correctamente.
-Realizar con word count especial, que cuente no solo cada palabra, si no que por cada articulo cuente cu�ntas veces aparece cada una de las palabras.
-Organizar los datos en modo de �ndice invertido.
-Implementar la b�squeda, la cual recibe una palabra, y gracias a la estructura de �ndice invertido, encuentra las noticias que m�s la contengan.

Todos los pasos dictados anteriormente son necesarios para la correcta soluci�n del problema, y espec�ficamente, el �ndice invertido ayuda mucho al mismo, ya que provee de una estructura muy �til al momento de realizar la b�squeda.

###1.3 Entendimiento de los datos

Link a los datos:https://www.kaggle.com/snapcrack/all-the-news

Los datos recibidos provienen de kaggle, una comunidad en l�nea de an�lisis de datos y machine learning. Dicha informaci�n contiene la recopilaci�n de varias noticias de distintos peri�dicos estadounidenses a lo largo de varios a�os, tales como: New York Times, CNN, Buzzfeed, etc�tera.

Contienen 3 archivos .csv, cada uno contiene 50.000 noticias y pesa 200 MB aproximadamente,  todos estos se encuentran divididos en columnas que contienen la siguiente informaci�n:

-Id de la noticia
-T�tulo
-Entidad que la public�
-Nombre del autor
-Fecha de la publicaci�n
-Mes de la publicaci�n
-A�o de la publicaci�n
-Url del Art�culo
-Contenido de la noticia 

Para el problema, los datos mayoritariamente necesarios y relevantes son la Id, El t�tulo y el contenido del mismo, columnas en las cuales se encuentran la mayor cantidad de palabras con importancia en las noticias.


###1.4 APIs de Anal�tica

Las librer�as que se utilizaron en la soluci�n del problema fueron principalmente de pyspark, entre ellas, librer�as relacionadas con el manejo de base de datos sql (tales como col para revisar y modificar las columnas, adem�s de udf para crear funciones personales a llamar con los datos) y otras relacionadas con el aprendizaje de m�quinas, conteniendo algunos puntos de limpieza de datos, tales c�mo:

-Desde pyspark.ml.feature: RegexTokenizer, para dividir las distintas palabras en tokens por medio de una expresi�n regular, adem�s de eso, ayuda a remover palabras de longitud 1.
-Desde pyspark.ml.feature: StopWordsRemover, para remover las stopword en ingl�s.
-Desde pyspark.ml.feature: HashingTF, IDF,Tokenizer esto fue utilizado como prueba para resolver el peso de las palabras, pero ya que no se realiz� el punto 2, al final tuvo poca utilidad. Con esto se pueden crear estructuras de datos que tienen el peso de cada palabra en dicho documento, y evaluarlas adem�s de organizarlas.

###2.Desarrollo

El proceso de desarrollo se encuentra incluido en el notebook.

###3.Pruebas

Las pruebas fueron realizadas en el mismo notebook que provee este github, el cual tambi�n se encuentra en databricks, para el correcto funcionamiento de la soluci�n se realizaron:

-Pruebas unitarias con cada CSV, centr�ndose en el correcto control de los datos limpios
-Pruebas con los CSVs unidos, consultando distintas palabras en los mismos para analizar las respuestas

Con esto se pudo verificar el funcionamiento del algoritmo y la limpieza de los datos.

###4.Instalaci�n 

Gracias al ambiente que provee databricks, no se necesito instalar ninguna de las APIs utilizadas (descritas en el punto 1.4), lo �nico que se realiz� fue la subida de los CSVs para su utilizaci�n.

##5.Ejecuci�n

La ejecuci�n se realiza autom�ticamente en el notebook del cluster de databricks, cada que se necesite re-hacer un comando se debe oprimir ctrl shift en dicho comando y comenzar� a ejecutarse
