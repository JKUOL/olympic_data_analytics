# Databricks notebook source
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, DoubleType, BooleanType, DateType

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "d995325e-d603-4690-abab-efc78860266d",
"fs.azure.account.oauth2.client.secret": 'ais8Q~e-ZP8K1Ufd2Z7.FxMv9h76irbcydbWxaOz',
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/eb9f0dd6-c9f9-49a5-a299-727717251806/oauth2/token"}


dbutils.fs.mount(
source = "abfss://tokyo-olympics-data@tokyoolimpicsdata.dfs.core.windows.net", # container@storageacc
mount_point = "/mnt/tokyoolympics",
extra_configs = configs)


# COMMAND ----------

# MAGIC %fs
# MAGIC ls "mnt/tokyoolympics"

# COMMAND ----------

athletes = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympics/raw-data/athletes.csv")
coaches = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympics/raw-data/coaches.csv")
medals = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympics/raw-data/medals.csv")
teams = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympics/raw-data/teams.csv")
entriesgender = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympics/raw-data/entriesgender.csv")

# COMMAND ----------

athletes.show()

# COMMAND ----------

athletes.printSchema()

# COMMAND ----------

coaches.show()

# COMMAND ----------

coaches.printSchema()

# COMMAND ----------

medals.show()

# COMMAND ----------

medals.printSchema()

# COMMAND ----------

teams.show()

# COMMAND ----------

teams.printSchema()

# COMMAND ----------

entriesgender.show()

# COMMAND ----------

entriesgender.printSchema()

# COMMAND ----------

# Find the top countries with the highest number of gold medals
top_gold_medal_countries = medals.orderBy("Gold", ascending=False).select("Team_Country","Gold").show()

# COMMAND ----------

# Calculate the average number of entries by gender for each discipline
average_entries_by_gender = entriesgender.withColumn(
    'Avg_Female', entriesgender['Female'] / entriesgender['Total']
).withColumn(
    'Avg_Male', entriesgender['Male'] / entriesgender['Total']
)
average_entries_by_gender.show()

# COMMAND ----------

athletes.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/tokyoolympics/transformed-data/athletes")
coaches.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympics/transformed-data/coaches")
medals.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympics/transformed-data/medals")
teams.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympics/transformed-data/teams")
entriesgender.repartition(1).write.mode("overwrite").option("header","true").csv("/mnt/tokyoolympics/transformed-data/entriesgender")

# COMMAND ----------


