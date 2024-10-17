from pyspark.sql import functions as F



class JoinTransformer():
    

    def __init__(self, join_type, join_on):
        self.join_type = join_type
        self.join_on = join_on
    
    

    def transform(self, df1, df2):
       

        join_keys = []

        
        for table in self.join_on:
            join_keys.append(self.join_on.get(table))

        assert len(join_keys) == 2

        matching_col = join_keys

        df1 = df1.join(df2, df1[matching_col[0]] == df2[matching_col[1]], self.join_type).drop(df2[matching_col[1]])
        
        return df1


class CrossJoinTransformer():
    

    def __init__(self):
        pass

    
    def transform(self, df1, df2):
       
        return df1.alias('a').crossJoin(df2.alias('b'))