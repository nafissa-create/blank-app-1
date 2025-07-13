import streamlit as st
import pandas as pd
import joblib

st.markdown(
       f"""
       <style>
       .stApp {{
           background-image: url("https://www.transparenttextures.com/patterns/diamond-upholstery.png");
           background-size: cover;
           background-repeat: no-repeat;
           background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

model = joblib.load("linear_model.pkl")
model_columns = joblib.load("model_columns.pkl")


df = pd.read_csv("diamonds.csv")
st.title("Diamond💎 cost predictor")
st.write("Curious about your diamond's value? I'm here to help!🤓")
carat = st.slider("Carat or weight of the diamond", 0.2, 6.0, step=0.1)
length_x = st.slider ('Length of the diamond', 0.0, 12.0, step=0.1)
width_y = st.slider ('width of the diamond', 0.0, 60.0, step=0.1)
depth_z = st.slider ('Depth of the diamond', 0.0, 32.0, step=0.1)
width_of_top_of_diamond = st.slider("Width of top of diamond relative to widest point", 40.0, 100.0, step=0.1)
inputs_frame = pd.DataFrame([{"carat":carat, "x":length_x, 'y':width_y, 'z': depth_z, "table":width_of_top_of_diamond }])
new_dataset = pd.concat([inputs_frame,df], axis=0)
inputs_frame.reindex(columns= model_columns, fill_value=0)
currency_rates = {"USD":1, "EUR":0.85, "RUB":78.52 , "KES":129.32,"BWP":13.35 ,"CAD":1.37 , "AOA":914.48 , "CDF":2876, "ZAR":18, "CNY":7.17, "INR":85.5, "JPY": 144.65, "AED":3.67,"GBP":0.73}
currency = st.selectbox("Choose your preferred currency", list(currency_rates.keys()))

if st.button("Generate predicted diamond price"):
  predicted_price_in_USD = model.predict(inputs_frame)[0]
  converted_price = predicted_price_in_USD * currency_rates[currency]
  st.write(f"The diamond price is estimated to: {converted_price:.2f}{currency}")


