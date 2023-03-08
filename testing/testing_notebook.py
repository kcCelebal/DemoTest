# Databricks notebook source
from runtime.nutterfixture import NutterFixture, tag
from pyspark.sql.functions import *
from pyspark.sql.types import *
import json

# COMMAND ----------

def matchColumnNames(df, dic):
    unmatched_col_list = []
    col_set = set(df.columns)
    for x in dic['columns']:
        if x['element_name'] not in col_set:
            unmatched_col_list.append(x['element_name'])
            return unmatched_col_list
    return unmatched_col_list


class MyTestFixture(NutterFixture):
    
    def __init__(self, mandatory_fields, view_name):
        json_dic = dbutils.notebook.run('../notebooks/main', 600,  {'view_name': view_name}) 
        self.dic = json.loads(json_dic)
        self.df = spark.table('global_temp.' + view_name)
        self.mandatory_fields = mandatory_fields.copy()
        super().__init__()
    
    
    def assertion_TestMatchColumnNames(self):
        unmatched_col_list = matchColumnNames(self.df, self.dic)
        print('List of unmatched columns ', unmatched_col_list)
        assert len(unmatched_col_list) == 0, "Column names mismatch"

# COMMAND ----------

mandatory_fields = ['medallion', 'vendor_id']
DFtesting = MyTestFixture(mandatory_fields, 'sample_file')
result = DFtesting.execute_tests()
# print(result.to_string())

# COMMAND ----------


