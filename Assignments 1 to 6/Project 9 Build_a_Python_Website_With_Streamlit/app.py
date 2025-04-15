import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.write(df.head())

    st.write("📈 Data Summary")
    st.write(df.describe())

    st.subheader("🔎 Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter", columns)
    unique_values = df[selected_column].dropna().unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("📊 Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    chart_type = st.selectbox("Select chart type", ["Line Chart", "Bar Chart", "Scatter Plot"])

    if st.button("Generate Plot"):
        if x_column in filtered_df.columns and y_column in filtered_df.columns:
            if not filtered_df.empty:
                try:
                    if chart_type == "Line Chart":
                        st.line_chart(filtered_df.set_index(x_column)[y_column])

                    elif chart_type == "Bar Chart":
                        st.bar_chart(filtered_df.set_index(x_column)[y_column])

                    elif chart_type == "Scatter Plot":
                        fig, ax = plt.subplots()
                        ax.scatter(filtered_df[x_column], filtered_df[y_column], color="skyblue")
                        ax.set_xlabel(x_column)
                        ax.set_ylabel(y_column)
                        ax.set_title(f"{y_column} vs {x_column}")
                        st.pyplot(fig)

                except Exception as e:
                    st.error(f"Plotting error: {e}")
            else:
                st.warning("⚠️ No data available after filtering.")
        else:
            st.warning("⚠️ Selected columns are not available in the filtered dataset.")
