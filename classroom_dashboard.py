# import pandas as pd
# import streamlit as st
# import plotly.express as px

# # Page title
# st.title("📊 Daily Household Energy Consumption Dashboard")

# # Load CSV
# @st.cache_data
# def load_data():
#     df = pd.read_csv("energy_data_india.csv")
#     df['Date'] = pd.to_datetime(df['Date'])
#     return df

# df = load_data()

# # Sidebar Filters
# st.sidebar.header("Filters")
# appliance = st.sidebar.multiselect("Select Appliances", options=df['Appliance'].unique(), default=df['Appliance'].unique())

# filtered_df = df[df['Appliance'].isin(appliance)]

# # Show Data
# st.subheader("Filtered Energy Consumption Data")
# st.dataframe(filtered_df)

# # Line Chart
# st.subheader("📈 Line Graph - Daily Consumption by Appliance")
# line_chart = px.line(filtered_df, x="Date", y="Consumption_kWh", color="Appliance", markers=True)
# st.plotly_chart(line_chart)

# # Scatter Plot
# st.subheader("🔵 Scatter Plot - Energy Consumption Trends")
# scatter = px.scatter(filtered_df, x="Date", y="Consumption_kWh", color="Appliance", size="Consumption_kWh", hover_data=['Appliance'])
# st.plotly_chart(scatter)

# # Pie Chart (Total consumption by appliance)
# st.subheader("🥧 Pie Chart - Total Consumption by Appliance")
# pie_df = filtered_df.groupby("Appliance")["Consumption_kWh"].sum().reset_index()
# pie_chart = px.pie(pie_df, names="Appliance", values="Consumption_kWh", title="Total Energy Used per Appliance")
# st.plotly_chart(pie_chart)

# # Footer
# st.markdown("Developed by Kaarthika 👩‍💻")
import pandas as pd
import streamlit as st
import plotly.express as px

# Page title
st.title("🏫 Classroom Power Consumption Dashboard")

# Load CSV data
@st.cache_data
def load_data():
    df = pd.read_csv("classroom_power.csv")  # <-- Your dataset file
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Load the data
df = load_data()

# Sidebar filters
device_options = df['Device'].unique()
selected_devices = st.sidebar.multiselect(
    "Select Devices",
    options=device_options,
    default=device_options
)

# Filter data
filtered_df = df[df['Device'].isin(selected_devices)]

# Show filtered data
st.subheader("📄 Filtered Power Consumption Data")
st.dataframe(filtered_df)

# Line Chart
st.subheader("📈 Daily Power Consumption by Device")
line_chart = px.line(
    filtered_df,
    x="Date",
    y="Consumption_kWh",
    color="Device",
    markers=True
)
st.plotly_chart(line_chart)

# Scatter Plot
st.subheader("🔵 Scatter Plot - Consumption Patterns")
scatter_plot = px.scatter(
    filtered_df,
    x="Date",
    y="Consumption_kWh",
    color="Device",
    size="Consumption_kWh",
    hover_data=['Device']
)
st.plotly_chart(scatter_plot)

# Pie Chart
st.subheader("🥧 Pie Chart - Total Consumption by Device")
pie_df = filtered_df.groupby("Device")["Consumption_kWh"].sum().reset_index()
pie_chart = px.pie(
    pie_df,
    names="Device",
    values="Consumption_kWh",
    title="Total Power Used per Device"
)
st.plotly_chart(pie_chart)

# Footer
st.markdown("Developed by Kaarthika 👩‍💻")
