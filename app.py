import streamlit as st
import joblib
import pandas as pd

loaded_model = joblib.load('Energy_Consumption.pkl')
st.title('Energy Predictor')
col1, col2 = st.columns([2,1])

with col1:
    start_date = st.date_input('Start date')
with col2:
    end_date = st.date_input('End date')
    if start_date and end_date:
        delt = end_date - start_date
        no_of_days = delt.days
    st.write(f'number of days {no_of_days}')
    
hour = st.selectbox('Select hour',no_of_days * 24)

temperature = st.number_input('Temperature',key='temp')
occ = list(range(0,10))
occupancy = st.selectbox('Occupancy',occ)
hum = list(range(30,61))
humidity = st.select_slider('Humidity',hum)

hvac = st.radio('HVAC Usage (1 for On, 0 for Off)',(1, 0))
ac = list(range(0,11))
num_ac = st.select_slider('Number of AC', ac)
hvac_watt = st.number_input('HVAC Watt Count',min_value=0,key='hvac')

light = st.radio('Light Usage (1 for On, 0 for Off)',(1, 0))
lig = list(range(0,11))
num_lights = st.select_slider('Number of Lights', lig)
light_watt  = st.number_input('Light Watt Count',min_value=0,key='light')

fans = st.radio('Fan Usage (1 for On, 0 for Off)',(1, 0))
fan = list(range(0,11))
num_fans = st.select_slider('Number of Fans', fan)   
fans_watt  = st.number_input('Fan Watt Count',min_value=0,key='fan')

dayofweek = st.text_input('Which Day 1-7')
holliday = st.radio('Holiday (1 for Yes, 0 for No)',(1, 0))

if st.button('Predict'):
    total_hvac_consumption = hvac_watt * hvac * num_ac * hour
    total_light_consumption = light_watt * light * num_lights * hour
    total_fan_consumption = fans_watt * fans * num_fans * hour
    total_consumption = total_hvac_consumption + total_light_consumption + total_fan_consumption

    if total_consumption > 1000:
        total_consumption_kwh = total_consumption/1000
        st.write(f'Total Energy consumption of all devices :{total_consumption_kwh:.2f} kwh')
    else:
        st.write(f'Total Energy consumption of all devices :{total_consumption} Wh')

    data = pd.DataFrame([[temperature,humidity,occupancy,hvac,light,dayofweek,holliday,hour]],
                        columns=['Temperature', 'Humidity','Occupancy', 'HVACUsage', 'LightingUsage','DayOfWeek','Holiday','Year','Month','Day','Hour'])
    prediction = loaded_model.predict(data)

    if prediction[0] > 1000:
        st.write(f'Predicted Energy consumption of all devices :{prediction[0]/1000 :.2f} kwh')
    else:
        st.write(f'Predicted Energy consumption of all devices :{prediction[0]: .2f} Wh')
