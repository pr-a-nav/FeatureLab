from feature import Feature
import pandas as pd


df = pd.DataFrame({
    "custom":[1,2],
    "age":[4,6],   
})
list = ["go"]

fr = Feature("go","int")
fr.detect_new_feature(df,list)