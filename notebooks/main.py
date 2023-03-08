# Databricks notebook source
# creating Spark dataframe


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
