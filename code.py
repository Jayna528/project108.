import pandas as pd
import plotly.figure_factory as ff 
import plotly.express as px


df = pd.read_csv('Student Marks vs Days Present.csv')
markslist = df['Marks In Percentage'].tolist()

print(markslist)

fig = ff.create_distplot([markslist], ['Grades of Students'], show_hist = False)
fig.show()