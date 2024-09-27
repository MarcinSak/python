import pandas as pd
import plotly.express as px
 
df = pd.read_csv('../data/015.gantt.txt', parse_dates=['start', 'end'])
 
df.head()