
import streamlit as st
from openai import OpenAI

NVIDIA_API_Key = st.secrets["NVIDIA_API_Key"]
client = OpenAI(
    api_key= NVIDIA_API_Key,
    base_url="https://integrate.api.nvidia.com/v1"
)

st.title("🏋️ BMI Calculator")

name = st.text_input("Enter your name")

wt = st.number_input(
    "Enter your weight (kg)",
    min_value=1.0,
    max_value=300.0,
    value=60.0
)

ht = st.number_input(
    "Enter your height (cm)",
    min_value=50.0,
    max_value=250.0,
    value=170.0
)

if st.button("Calculate BMI"):

    if name.strip() == "":
        st.warning("Please enter your name.")

    else:
        bmi = round(wt / (ht / 100) ** 2, 2)

        st.success(
            f"{name}, with your weight {wt} kg and height {ht} cm, "
            f"your BMI is {bmi}"
        
        )
        prompt = f"Analyze the {bmi} in less than 100 words"
        response = client.chat.completions.create(
        model="z-ai/glm-5.3-flash",
        messages=[
        {"role": "user", "content": prompt}
        ]
        )

        # print(response.text)
        st.write(response.choices[0].message.content)