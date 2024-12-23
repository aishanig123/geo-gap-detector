!pip install folium

import folium
import pandas as pd
from folium.plugins import HeatMap

data = {
    'ZIP Code': [
        '38601', '38672', '38680', '38666', '38683', '38654', '38609', '38657', '38648', '38625',
        '87501', '88001', '88012', '87506', '87507', '88021', '87532', '87540', '88042', '88046',
        '02118', '02114', '02116', '02115', '02113', '02139', '02140', '02139', '02108', '02111',
        '55101', '55401', '55403', '55405', '55406', '55407', '55408', '55409', '55410', '55411'
    ],
    'State': [
        'Mississippi', 'Mississippi', 'Mississippi', 'Mississippi', 'Mississippi', 'Mississippi',
        'Mississippi', 'Mississippi', 'Mississippi', 'Mississippi',
        'New Mexico', 'New Mexico', 'New Mexico', 'New Mexico', 'New Mexico', 'New Mexico',
        'New Mexico', 'New Mexico', 'New Mexico', 'New Mexico',
        'Massachusetts', 'Massachusetts', 'Massachusetts', 'Massachusetts', 'Massachusetts',
        'Massachusetts', 'Massachusetts', 'Massachusetts', 'Massachusetts', 'Massachusetts',
        'Minnesota', 'Minnesota', 'Minnesota', 'Minnesota', 'Minnesota', 'Minnesota',
        'Minnesota', 'Minnesota', 'Minnesota', 'Minnesota'
    ],
    'Avg Distance to Nearest Hospital (miles)': [
        25, 30, 28, 32, 27, 29, 26, 24, 31, 22,
        22, 24, 26, 20, 18, 25, 19, 23, 21, 22,
        5, 3, 4, 2, 3, 1, 3, 2, 4, 3,
        12, 10, 11, 8, 9, 7, 12, 11, 10, 13
    ],
    'Latitude': [
        34.001, 34.731, 34.654, 34.872, 34.999, 34.534, 34.389, 34.872, 34.300, 34.533,
        35.682, 32.327, 32.123, 35.658, 35.124, 32.475, 32.675, 32.345, 32.874, 32.978,
        42.347, 42.354, 42.367, 42.360, 42.344, 42.362, 42.375, 42.388, 42.400, 42.430,
        44.975, 44.986, 44.965, 44.947, 44.940, 44.930, 44.951, 44.962, 44.983, 44.970
    ],
    'Longitude': [
        -90.259, -90.014, -90.123, -90.234, -90.456, -90.345, -90.123, -90.678, -90.654, -90.567,
        -105.937, -104.973, -104.878, -105.456, -105.123, -104.800, -104.567, -104.456, -104.345, -104.230,
        -71.061, -71.064, -71.055, -71.040, -71.034, -71.070, -71.080, -71.090, -71.095, -71.085,
        -93.265, -93.271, -93.258, -93.245, -93.232, -93.229, -93.222, -93.235, -93.238, -93.250
    ]
}

df = pd.DataFrame(data)

states_of_interest = ['Mississippi', 'New Mexico', 'Massachusetts', 'Minnesota']
df_filtered = df[df['State'].isin(states_of_interest)]

m = folium.Map(location=[37.8, -96], zoom_start=5)

heat_data = [[row['Latitude'], row['Longitude'], row['Avg Distance to Nearest Hospital (miles)']] for index, row in df_filtered.iterrows()]

HeatMap(heat_data, radius=25, blur=15).add_to(m)

def get_color(distance):
    if distance < 5:
        return 'green'
    elif distance < 10:
        return 'orange'
    elif distance < 15:
        return 'red'
    else:
        return 'purple'

for idx, row in df_filtered.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=folium.Popup(f"ZIP Code: {row['ZIP Code']}<br>State: {row['State']}<br>Avg Distance: {row['Avg Distance to Nearest Hospital (miles)']} miles", parse_html=True),
        icon=folium.Icon(color=get_color(row['Avg Distance to Nearest Hospital (miles)']))
    ).add_to(m)

m
