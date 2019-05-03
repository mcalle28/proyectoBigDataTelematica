# Databricks notebook source
#import de todas las librerias necesarias de python y spark
import pyspark
import re
import pyspark.sql.functions as f
from pyspark.sql import SparkSession

from pyspark.sql.functions import col,udf,asc,lower
from pyspark.sql.types import IntegerType

from pyspark.ml.feature import Tokenizer,RegexTokenizer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.feature import HashingTF,IDF,Tokenizer

#Creación de la sesión para trabajar en spark
spark= SparkSession.builder.appName('proyecto3').getOrCreate()

# COMMAND ----------

#Creación de los tres dataframes a utilizar
df1= spark.read.csv('/FileStore/tables/articles1.csv',inferSchema=True,header=True)
df2= spark.read.csv('/FileStore/tables/articles2.csv',inferSchema=True,header=True)
df3= spark.read.csv('/FileStore/tables/articles3.csv',inferSchema=True,header=True)

#unión de los tres dataframes en uno solo
dfx=df1.union(df2)
dft=dfx.union(df3)

# COMMAND ----------

dft.show()

# COMMAND ----------

#separación de las tablas en el contenido interesante para la solución del problema
df=dft.select(dft['id'],dft['title'],dft['content'])

# COMMAND ----------

df.show()

# COMMAND ----------

#creación de los tokenizadores de palabras, en este caso se crean dos tipos, pero el tipo a utilizar es el que permite 
#las expresiones regulares regex_tokenizer, estas permiten limpiar caracteres especiales y palabras de longitud 1 
tokenizer= Tokenizer(inputCol='content', outputCol='words')
regex_tokenizer= RegexTokenizer(inputCol='content', outputCol='words',pattern='[^a-zA-Z0-9]+').setMinTokenLength(2)
count_tokens= udf(lambda words:len(words),IntegerType())

# COMMAND ----------

#limpieza de los datos nulos en contenido y titulo, además de la transformación del dataframe en tokens
df2=df.fillna("unknown", subset=["content","title"])
tokenized= regex_tokenizer.transform(df2)

# COMMAND ----------

tokenized.show()

# COMMAND ----------

#removedor de stopwords en ingles, creando un nuevo dataframe sin las mismas
remover= StopWordsRemover(inputCol='words', outputCol='filtered')
sinsw=remover.transform(tokenized)

# COMMAND ----------

sinsw.show()

# COMMAND ----------

#Testeo de hash y frecuencia de documento inverso
#esto no se utilizo al final pero es interesante verlo
#hashing_tf= HashingTF(inputCol='filtered',outputCol='rawFeatures')
#featurized_data=hashing_tf.transform(sinsw)
#featurized_data.show()

# COMMAND ----------

#idf=IDF(inputCol='rawFeatures', outputCol='resultado')
#idf_model=idf.fit(featurized_data)
#idf_model=idf.fit(featurized_data)
#rescaled_data=idf_model.transform(featurized_data)
#rescaled_data.select('id','title','filtered','resultado').show()

# COMMAND ----------

#creación y selección de la estructura del indice inverso, por medio de una agrupación y una agregación de las palabras tokenizadas
wordcount = sinsw.select("id", f.explode("filtered").alias("words")).groupBy("id","words").count().groupBy("words").agg(f.collect_list(f.struct(f.col("id"), f.col("count"))).alias("wordcount"))
IndiceInverso = wordcount.orderBy('words').sort(asc('words'))

# COMMAND ----------

IndiceInverso.show()

# COMMAND ----------

#creación del widget que ofrece databricks para introducir el texto
dbutils.widgets.text("word","Inserte palabra a buscar"," ")

# COMMAND ----------

#Muestra de los 5 textos con la mayor cantidad de las palabras
dfI= IndiceInverso.filter(IndiceInverso['words'] == dbutils.widgets.get("word").lower()).collect()
contador =dfI[0].wordcount
contador = sorted(contador, key=lambda x: x[1])
arregloTitulos = list(reversed(contador))[:5]

# COMMAND ----------

for x in range (0,5):
  print(str(arregloTitulos[x][1])+", "+sinsw.filter(sinsw['id'] == arregloTitulos[x][0]).collect()[0].id+", "+sinsw.filter(sinsw['id'] == arregloTitulos[x][0]).collect()[0].title)

# COMMAND ----------


