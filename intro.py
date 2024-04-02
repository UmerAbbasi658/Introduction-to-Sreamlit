import streamlit as st

st.title("Our First Streamlit")
from PIL import Image

st.subheader('Images of Moon')

image=Image.open("g.jpg")
st.image(image,use_column_width=True)

st.write(" Writing any text")

st.markdown("This is a markdown cell")

st.success('Congratulations You have run the app')
st.info('This is an information section just for you')
st.warning('There is a warning')
st.error('you are having an error')
st.help(range)
st.text('-----'*100)

import numpy as np 
import pandas as pd 

dataframe=np.random.rand(10,20)

st.dataframe(dataframe)

st.text('-----'*100)

import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.rand(20, 30), columns=['column_name_%d' % i for i in range(30)])


st.dataframe(data.style.highlight_max(axis=1))
st.text('***'*100)

#Display chart
chart_data=pd.DataFrame(np.random.randn(50,3), columns=['a','b','c'])
st.line_chart(chart_data)
st.text('--'*100)

st.area_chart(chart_data)

st.bar_chart(chart_data)

import matplotlib.pyplot as plt
arr=np.random.normal(1,1,size=100)
plt.hist(arr,bins=20)
st.pyplot()
st.text('****'*100)


import plotly
import plotly.figure_factory as ff 


# another distplot

x1=np.random.randn(200)-2
x2=np.random.randn(200)
x3=np.random.randn(200)-2

hist_data=[x1,x2,x3]
group_labels=['group1','group2','group3']

fig=ff.create_distplot(hist_data,group_labels,bin_size=[.2,.25,.5])
st.plotly_chart(fig,use_container_width=True)
st.text('****'*100)

# Define the latitude and longitude range for Islamabad
min_lat, max_lat = 33.5496, 33.7151
min_lon, max_lon = 72.7612, 73.2013

# Generate random latitude and longitude values within the range for Islamabad
data_df = pd.DataFrame(np.random.rand(100, 2), columns=['lat', 'lon'])
data_df['lat'] = data_df['lat'] * (max_lat - min_lat) + min_lat
data_df['lon'] = data_df['lon'] * (max_lon - min_lon) + min_lon

# Display the map with the generated data
st.map(data_df)
st.text('--'*100)
# creating buttons

if st.button('Say Hello'):
    st.write("Hello, we are here and there is a map of Islamabad above")
else:
    # Define the latitude and longitude range for Islamabad
    min_lat, max_lat = 33.5496, 33.7151
    min_lon, max_lon = 72.7612, 73.2013

    # Generate random latitude and longitude values within the range for Islamabad
    data_df = pd.DataFrame(np.random.rand(100, 2), columns=['lat', 'lon'])
    data_df['lat'] = data_df['lat'] * (max_lat - min_lat) + min_lat
    data_df['lon'] = data_df['lon'] * (max_lon - min_lon) + min_lon

    # Display the map with the generated data
    st.map(data_df)
    st.text('--'*100)

st.text('--'*100)

genre=st.radio('What is your favourite genre?',('Comedy','Drama','Documentary'))

if genre=='Comedy':
	st.write('You love Comedy')
elif genre=='Drama':
	st.write('drama is cool')
else:
    st.write('I see interesting')
    # Define the latitude and longitude range for Islamabad
    min_lat, max_lat = 33.5496, 33.7151
    min_lon, max_lon = 72.7612, 73.2013

    # Generate random latitude and longitude values within the range for Islamabad
    data_df = pd.DataFrame(np.random.rand(100, 2), columns=['lat', 'lon'])
    data_df['lat'] = data_df['lat'] * (max_lat - min_lat) + min_lat
    data_df['lon'] = data_df['lon'] * (max_lon - min_lon) + min_lon

    # Display the map with the generated data
    st.map(data_df)


st.text('--'*100)

# select button

option=st.selectbox('How was your night?',('Fantastic','Good','Awesome','Fine'))
st.write('You said your night was ',option)

st.text('--'*100)

option=st.multiselect('How was your night?',('Fantastic','Good','Awesome','Fine'))
st.write('You said your night was ',option)


st.text('--'*100)


age = st.slider('How old are you?', 0, 150, 10, key='age_slider')
st.write('Your Age is and your answer of spending night is:', age, option)
# slider in a different way
values=st.slider('Select a range of values',0,60,(15,30))
st.write('You have selected range between',values)

st.text('--'*100)

number=st.number_input('Enter some numbers')
st.write('The number you entered is:',number)

st.text('--'*100)
# How a user can upload

upload_file=st.file_uploader('Choose a csv file',type='csv')
if upload_file is not None:
	df=pd.read_csv(upload_file)
	st.write('This is your data',df)
	st.success('Successfully Uploaded')
else:
	st.markdown('Upload a csv file')

st.text('--'*100)

# we can add a color picker
color=st.sidebar.color_picker('Pick your color','#00FFAA')
st.write('This Your color',color)

# how we can set a side bar
sidebar=st.sidebar.selectbox('What is your favorite car?',('Mercedes','Haval','BMW','Range Rover','Others','Not sure','Nothing'))
# progress bar
# import time
# progress_bar=st.progress(0)
# for percent_complete in range(100):
# 	time.sleep(0.3)
# 	progress_bar.progress(percent_complete+1)

	
# 	with st.spinner('wait for it...'):
# 		time.sleep(5)

st.write("🎈🎉🥳")
st.balloons()
	