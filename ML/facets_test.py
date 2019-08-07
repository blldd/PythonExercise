# -*- coding: utf-8 -*-
"""
@Time    : 2019/8/6 8:28 PM
@Author  : ddlee
@File    : facets_test.py
"""
from facets_overview.generic_feature_statistics_generator import GenericFeatureStatisticsGenerator
import pandas as pd

df =  pd.DataFrame({'num' : [1, 2, 3, 4], 'str' : ['a', 'a', 'b', None]})
proto = GenericFeatureStatisticsGenerator().ProtoFromDataFrames([{'name': 'test', 'table': df}])



import pandas as pd
import pandas_profiling

data=pd.read_csv("model.csv")
pandas_profiling.ProfileReport(data)

profile = pandas_profiling.ProfileReport(data)
profile.to_file(outputfile = "output_file.html")


#

import pandas as pd
import pandas_profiling
import numpy as np

# importing the data
df = pd.read_csv('/Users/lukas/Downloads/titanic/train.csv')

# descriptive statistics
df.describe()

pandas_profiling.ProfileReport(df)

