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
clarity = st.selectbox("Clarity of the diamond from worst (I1) to best (IF)", ["I1", "SI2", "VS2", "VS1", "VVS2", "IF"])
depth_z = st.slider ('Depth of the diamond', 0.2, 45.0, step=0.1)
width_of_top_of_diamond = st.slider("Width of top of diamond relative to widest point", 40.0, 100.0, step=0.1)
inputs_frame = pd.DataFrame([{"carat":carat, "clarity":clarity, 'z': depth_z, "table":width_of_top_of_diamond  }])
new_dataset = pd.concat([inputs_frame,df], axis=0)
encoded_input = pd.get_dummies(inputs_frame, columns=["clarity"], drop_first=True)
encoded_input = encoded_input.reindex(columns=model_columns, fill_value=0)
currency_rates = {"USD":1, "EUR":0.85, "RUB":78.52 , "KES":129.32,"BWP":13.35 ,"CAD":1.37 , "AOA":914.48 , "CDF":2876, "ZAR":18, "CNY":7.17, "INR":85.5, "JPY": 144.65, "AED":3.67,"GBP":0.73}
currency = st.selectbox("Choose your preferred currency", list(currency_rates.keys()))

if st.button("Generate predicted diamond price"):
  predicted_price_in_USD = model.predict(encoded_input)[0]
  converted_price = predicted_price_in_USD * currency_rates[currency]
  st.write(f"The diamond price is estimated to: {converted_price:.2f}{currency}")


