import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from urllib.request import urlopen
import streamlit as st
import seaborn as sns
import datetime 
import os
import json 

iris = pd.read_csv('iris.csv')

iris=pd.DataFrame(iris)
col = ['sepal_length','sepal_width','petal_length','petal_width','iris_type']
iris.columns=col
st.dataframe(iris)


fig = px.scatter_matrix(iris,dimensions=['sepal_length','sepal_width','petal_length','petal_width'],color='iris_type')
st.plotly_chart(fig,theme='streamlit')

#FILTER BY IRIS SPECIES
species = st.selectbox('SPECIES',list(iris['iris_type'].unique()))

#IRIS AFTER FILTERING
iris_filtered = iris[iris['iris_type']==species]

hist_data = [iris_filtered['sepal_length'],iris['sepal_width'],iris['petal_length'],iris['petal_width']]
group_labels = ['sepal_length','sepal_width','petal_length','petal_width']

st.markdown('## Distribution Plot per features')
fig_2 = ff.create_distplot(hist_data, group_labels, bin_size = [.25,.25,.25,0.25])


st.plotly_chart(fig_2,theme = None)

st.markdown('##  Distribution per species')

col_select = ['sepal_length','sepal_width','petal_length','petal_width']
feat_select = st.selectbox('FEATURES',col_select)

fig_3=px.box(iris,'iris_type',feat_select)
st.plotly_chart(fig_3)
