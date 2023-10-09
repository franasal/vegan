import streamlit as st
import time
# from playsound import playsound
import base64



st.set_page_config(page_title="Lebenshof Kuhtopia!", page_icon="Iconveg.png")

st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)



# Example usage:
sanctuary_name = "Kuhtopia"


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


def form_fck(total_time):
    with st.form("thisform"):


        if total_time>0:

            total_time_mins=total_time/60

            alarm1 = st.slider(label='Minutes', min_value=0.0, max_value=total_time_mins, step=0.5, format='%.1f' ,key=4)*60



    # # Every form must have a submit button.
    #
        submitted = st.form_submit_button("Submit")

        if submitted:
            # on_click= start_alarm(total_time, alarm1, alarm2)
            st.text("started")
            my_bar = st.progress(0)

            st.text(total_time)
            sleep_time = total_time/100
            alarm1_perc =  int((alarm1*100)/total_time)

            test_time_fast = 1
            with st.spinner("meditating..."):

                for percent_complete in range(100):

                    time.sleep(sleep_time/test_time_fast)
                    if percent_complete == alarm1_perc:
                        autoplay_audio('shovel-gong.mp3')
                        st.success("alarm 1")
                    elif percent_complete == 99:
                        autoplay_audio('gong1-94016.mp3')
                        st.success("alarm 2")
                    my_bar.progress(percent_complete + 1)



colH, colM, colS = st.columns(3)
with colH:

    hour = st.number_input(label='Hours', min_value=0, max_value=100, step=1, format='%d' ,key=1)*60*60

with colM:

    minutes = st.number_input(label='Minutes', min_value=0, max_value=60, step=1, format='%d' ,key=2)*60

with colS:

    secs = st.number_input(label='Seconds', min_value=0, max_value=60, step=1, format='%d' ,key=3)

total_time = hour + minutes + secs

setalarm = st.button("", on_click=form_fck(total_time))
