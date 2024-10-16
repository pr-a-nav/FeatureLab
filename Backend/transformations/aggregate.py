from pyspark.sql import functions as F
import typing
import pyspark.data


class AggregateTransformer():
   

    def __init__(self, group_by_columns, aggregation_type):
        self.group_by_columns = group_by_columns
        self.aggregation_type = aggregation_type

    def transform(self, df):
        
        df = df.groupBy(*self.group_by_columns)

        if self.aggregation_type == 'sum':
            df = df.sum()
        if self.type == 'avg':
            df = df.mean()
        if self.type == 'count':
            df = df.count()

        return df