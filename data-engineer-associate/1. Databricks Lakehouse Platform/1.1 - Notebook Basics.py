# Databricks notebook source
print("Hello World!")

# COMMAND ----------

%sql
SELECT "Hello world from SQL!"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC 
# MAGIC text with a **bold** and *italicized* in it.
# MAGIC 
# MAGIC Ordered list
# MAGIC 1. first
# MAGIC 1. second
# MAGIC 1. third
# MAGIC 
# MAGIC Unordered list
# MAGIC * coffee
# MAGIC * tea
# MAGIC * tea
# MAGIC 
# MAGIC 
# MAGIC Images:
# MAGIC ![Associate-badge](https://www.databricks.com/wp-content/uploads/2022/04/associate-badge-eng.svg)
# MAGIC 
# MAGIC And of course, tables:
# MAGIC 
# MAGIC | user_id | user_name |
# MAGIC |---------|-----------|
# MAGIC |    1    |    Adam   |
# MAGIC |    2    |    Sarah  |
# MAGIC |    3    |    John   |
# MAGIC 
# MAGIC Links (or Embedded HTML): <a href="https://docs.databricks.com/notebooks/notebooks-manage.html" target="_blank"> Managing Notebooks documentation</a>

# COMMAND ----------
%run ../Includes/Setup

# COMMAND ----------
print(full_name)

# COMMAND ----------
%fs ls '/databricks-datasets'

# COMMAND ---------- databricks utils
dbutils.help()

# COMMAND ----------
dbutils.fs.help()

# COMMAND ----------
files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------
display(files)

# COMMAND ----------
# With Tab Command Autocompletion
