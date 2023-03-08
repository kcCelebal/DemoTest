# Databricks notebook source
import json

# COMMAND ----------

# CSV options
infer_schema = 'true'
first_row_is_header = 'true'
delimiter = ","
file_type = 'csv'
file_location = '/FileStore/tables/trip_data.csv'

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
    .option("inferSchema", infer_schema) \
    .option("header", first_row_is_header) \
    .option("sep", delimiter) \
    .load(file_location)

# COMMAND ----------

dic = dict()

dic['columns'] = [{"element_name": 'medallion'},
                  {'element_name': 'hack_license'},
                  {'element_name': 'vendor_id'},
                  {'element_name': 'rate_code_id'},
                  {'element_name': 'store_and_fwd_flag'},
                  {'element_name': 'pickup_datetime'},
                  {'element_name': 'dropoff_datetime'},
                  {'element_name': 'passenger_count'},
                  {'element_name': 'trip_time_in_sec'},
                  {'element_name': 'trip_distance'},
                  {'element_name': 'pickup_long'},
                  {'element_name': 'pickup_lat'},
                  {'element_name': 'dropoff_long'},
                  {'element_name': 'dropoff_lat'},
                 ]


# COMMAND ----------

view_name = 'sample_file'
df.createOrReplaceGlobalTempView(view_name)

# COMMAND ----------

dbutils.notebook.exit(json.dumps(dic))
