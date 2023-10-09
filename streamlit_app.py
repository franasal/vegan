import streamlit as st
import time
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from streamlit_extras.buy_me_a_coffee import button


st.set_page_config(page_title="Your Ⓥegan Impact", page_icon="Iconveg.png")


st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

# hide some stuff
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


seconds_in_a_day = 24 * 60 * 60


def update_dashboard(vegan_days, num_people):

    count = 0

    while True:
        time.sleep(1)
        count += 1

        vegan_time = vegan_days.days + (count/seconds_in_a_day)

        water_consumption = vegan_time * 4.164 * num_people
        grain_consumption = vegan_time * 18 * num_people
        forest_land = vegan_time * 3 * num_people
        co2_emission = vegan_time * 9 * num_people
        animal_lives_saved = vegan_time * 0.22 * num_people

        col_, col1, col2,  = st.columns(3)

        with col_:
            st.success("Since your 🌱 vegan birthday you have saved:")
            st.metric(label="🐄 Animal Lives! ", value=("%.0f" %animal_lives_saved), delta=("%.8f" %animal_lives_saved))



        with col1:
            st.metric(label="🌽 Kg of Grain", value=("%.2f" %grain_consumption), delta=("%.8f" %grain_consumption))
            st.metric(label="🌲 Sq.m of Forested land", value=("%.2f" %forest_land), delta=("%.8f" %forest_land))
        with col2:

            st.metric(label="☁️ Kg of CO2", value=("%.2f" %co2_emission), delta=("%.8f" %co2_emission))
            st.metric(label="💧 Liters of Water", value=("%.2f" % water_consumption), delta=("%.8f" % water_consumption))


col1, col2, col3 = st.columns(3)

with col2:
    st.image("./A4.png")

st.markdown("<h1 style='text-align: center;'>Your Ⓥegan Impact</h1>", unsafe_allow_html=True)





today = date.today()
today = date(
    year=today.year,
    month=today.month,
    day=today.day,
)

min_year = datetime.now() - relativedelta(years=120)


dt = st.date_input("When's your Vegan birthday?", date.today(), min_value=min_year, max_value=date.today())
pl = st.empty()
sec = st.empty()

vgnbdays = today - dt

num_people = 1


with pl:
    update_dashboard(vgnbdays, num_people)
# sec = st.empty()
with sec:

    button(username="AnimalSanctuaryAlly", floating=False, width=221)
