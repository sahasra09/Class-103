import pandas as pd
import plotly.express as px
#line graph
#df=pd.read_csv('line_chart.csv')
#fig=px.line(df,x='Year',y='Per capita income',color='Country',title='Per capita income')
#fig.show()

#bar graph
#df=pd.read_csv('data.csv')
#fig=px.bar(df,x='Country',y='InternetUsers')
#fig.show()

#scatter plot
df=pd.read_csv('data.csv')
fig=px.scatter(df,x='Population',y='Per capita',size='Percentage',color='Country',size_max=60)
fig.show()