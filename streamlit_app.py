import streamlit as st
import time
from datetime import datetime, date


seconds_in_a_day = 24 * 60 * 60


def update_dashboard4(vegan_days, num_people):

    count = 0

    while True:
        time.sleep(1)
        print(vegan_days)
        count += 1

        vegan_time = vegan_days.days + (count/seconds_in_a_day)

        water_consumption = vegan_time * 4.164 * num_people
        grain_consumption = vegan_time * 18 * num_people
        forest_land = vegan_time * 3 * num_people
        co2_emission = vegan_time * 9 * num_people
        animal_lives_saved = vegan_time * 0.22 * num_people




        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric(label="💧 Liters of Water", value=("%.2f" % water_consumption), delta=("%.8f" % water_consumption))
        with col2:
            st.metric(label="🌽 Kg of Grain", value=("%.2f" %grain_consumption), delta=("%.8f" %grain_consumption))
        with col3:
            st.metric(label="🌲 Sq.m of Forested land", value=("%.2f" %forest_land), delta=("%.8f" %forest_land))
        with col4:
            st.metric(label="☁️ Kg of CO2", value=("%.2f" %co2_emission), delta=("%.8f" %co2_emission))
        with col5:
            st.metric(label="animal_lives_saved ", value=("%.0f" %animal_lives_saved), delta=("%.8f" %animal_lives_saved))


# dashboard title
st.title("Vegan live impact tracker")

dt = st.date_input("When's your Vegan birthday", date.today())

today = date.today()
today = date(
    year=today.year,
    month=today.month,
    day=today.day,
)

vgnbdays = today - dt

num_people = 1


with st.empty():
    update_dashboard4(vgnbdays, num_people)