# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bokeh.sampledata.gapminder import life_expectancy
import pandas as pd

print(life_expectancy)

df = pd.DataFrame(life_expectancy)

print(df.loc['Afghanistan'])
