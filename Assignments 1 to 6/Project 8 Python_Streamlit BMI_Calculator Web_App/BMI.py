import streamlit as st

def calculate_bmi(weight, height_m):
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def main():
    # Set page config
    st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

    # Custom CSS styling for background color and sections
    st.markdown("""
        <style>
        /* Full Page Background */
        body {
            background-color: #f0f8ff; /* Light Blue Background */
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
        
        .stApp {
            background-color: #f0f8ff; /* Make sure the app background is the same */
            padding: 20px;
        }

        .title {
            text-align: center;
            font-size: 4em;
            color: #4CAF50;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #666;
        }
        .bmi-result {
            text-align: center;
            font-size: 1.5em;
            margin-top: 20px;
            background-color: #ffffff; /* White background for result box */
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .input-section {
            background-color: #ffffff; /* White background for input section */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # App title and subtitle
    st.markdown('<div class="title">💪 BMI Calculator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Calculate your Body Mass Index easily!</div>', unsafe_allow_html=True)
    st.write("")

    name = st.text_input("👤 Enter your name:")
    col1, col2 = st.columns(2)

    with col1:
        inches = st.number_input("📏 Height (inches):", min_value=0, step=1)
    with col2:
        weight = st.number_input("⚖️ Weight (kg):", min_value=0.0, format="%.2f")

    # BMI Calculation
    if st.button("🚀 Calculate BMI"):
        if inches > 0 and weight > 0:
            # Convert height to meters
            height_m = inches * 0.0254

            bmi = calculate_bmi(weight, height_m)
            st.markdown(f'<div class="bmi-result">👉 **{name}, your BMI is {bmi}**</div>', unsafe_allow_html=True)

            # Feedback based on BMI range
            if bmi < 18.5:
                st.warning("🍃 You are underweight.")
                st.balloons() # Celebrate when the user is underweight 
            elif 18.5 <= bmi < 24.9:
                st.success("✅ You have a normal weight.")
                st.balloons()  # Celebrate when the user has a normal weight 
            elif 25 <= bmi < 29.9:
                st.warning("⚠️ You are overweight.")
            else:
                st.error("🚨 You are obese.")
        else:
            st.error("❌ Please enter valid height and weight.")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
