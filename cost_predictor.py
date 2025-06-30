import streamlit as st
import pandas as pd
#import joblib

df = pd.read_csv("diamonds.csv")
st.title("Diamond💎 cost predictor")
st.write("Curious about your diamond's value? I'm here to help!🤓")
carat = st.slider("Carat or weight of the diamond", 0.2, 6.0, step=0.1)
cut = st.selectbox("Quality of the cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Diamond colour from best (D) to worst (J)", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox("Clarity of the diamond from worst (I1) to best (IF)", ["I1", "SI2", "VS2", "VS1", "VVS2", "VVS2", "IF"])
length_x = st.slider("Length in mm", 0.0, 12.0, step=0.1)
width_y = st.slider("Width in mm", 0.0, 60.0, step =0.1)
depth_z = st.slider("Depth in mm", 0.0, 32.0, step=0.1)
total_depth = None
if (length_x + width_y) > 0:
   total_depth = (2*depth_z)/(length_x + width_y)
   st.write(f"Total depth percentage is {total_depth:.4f}")
width_of_top_of_diamond = st.slider("Width of top of diamond relative to widest point", 40.0, 100.0, step=0.1)



#model, model_columns = joblib.load()
#inputs_frame = pd.DataFrame([{"carat":carat, "cut":cut, "color":color, "clarity":clarity, "x":length_x, "y":width_y, "z":depth_z, "depth":total_depth, "table":width_of_top_of_diamond  }])
#new_dataset = pd.concat([inputs_frame,df], axis=0)
#for col in model_columns:
#   if col not in inputs_frame:
#      inputs_frame[col] = 0
#inputs_frame = inputs_frame[model_columns]
currency_rates = {"USD":1, "EUR":0.85, "RUB":78.52 , "KES":129.32,"BWP":13.35 ,"CAD":1.37 , "AOA":914.48 , "CDF":2876, "ZAR":18, "CNY":7.17, "INR":85.5, "JPY": 144.65, "AED":3.67,"GBP":0.73}
currency = st.selectbox("Choose your preferred currency", list(currency_rates.keys()))

if st.button("Generate predicted diamond price"):
#  predicted_price_in_USD = model.predict(inputs_frame)[0]
#  converted_price = predicted_price_in_USD * currency_rates[currency]
  st.write(f"The diamond price is estimated to:")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://www.transparenttextures.com/patterns/diamond-upholstery.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
