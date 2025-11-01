pip install streamlit pandas scikit-learn matplotlib requests
Save the code as global_dashboard.py
streamlit run global_dashboard.py
Open the browser link (usually http://localhost:8501).




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

st.set_page_config(page_title="Global Challenges Dashboard 2025", layout="wide")

st.title("🌍 Global Challenges Dashboard (2025)")
st.sidebar.header("Select a Global Problem to Explore")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Choose a module:",
    [
        "💧 Water Scarcity & Drought Monitoring",
        "🌾 Food Security / Crop Yield Prediction",
        "🌫️ Air Pollution Monitoring",
        "📰 Misinformation Detection",
        "⚡ Electricity Grid Monitoring"
    ]
)

# -----------------------------------------------------------------------------------
# 💧 Water Scarcity
# -----------------------------------------------------------------------------------
if page == "💧 Water Scarcity & Drought Monitoring":
    st.header("💧 Water Scarcity & Drought Monitoring")

    st.write("Upload rainfall data (`Date`, `Region`, `Rainfall_mm`) or use sample data:")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        df = pd.DataFrame({
            "Date": pd.date_range("2024-01-01", periods=12, freq="M"),
            "Rainfall_mm": [120, 85, 60, 40, 25, 30, 50, 70, 90, 110, 130, 95]
        })

    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    st.line_chart(df['Rainfall_mm'])
    drought_threshold = st.slider("Set Drought Threshold (mm/month)", 10, 200, 50)

    drought_months = df[df['Rainfall_mm'] < drought_threshold]
    if not drought_months.empty:
        st.warning("⚠️ Drought Alert in these months:")
        st.dataframe(drought_months)
    else:
        st.success("✅ No drought alerts this period!")

# -----------------------------------------------------------------------------------
# 🌾 Food Security
# -----------------------------------------------------------------------------------
elif page == "🌾 Food Security / Crop Yield Prediction":
    st.header("🌾 Food Security / Crop Yield Prediction")

    st.write("Upload agricultural dataset (`Rainfall`, `Temperature`, `Soil_quality`, `Yield`):")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        df = pd.DataFrame({
            "Rainfall": [200, 150, 100, 300, 250],
            "Temperature": [25, 30, 35, 28, 26],
            "Soil_quality": [7, 6, 5, 8, 7],
            "Yield": [4.5, 3.8, 2.9, 5.2, 4.9]
        })
        st.info("Using sample data for crop yield prediction.")

    X = df[['Rainfall', 'Temperature', 'Soil_quality']]
    y = df['Yield']
    model = LinearRegression().fit(X, y)

    st.subheader("Predict Crop Yield")
    r = st.number_input("Rainfall (mm)", 50, 500, 200)
    t = st.number_input("Temperature (°C)", 10, 45, 28)
    s = st.number_input("Soil Quality Index (1–10)", 1, 10, 7)
    pred = model.predict([[r, t, s]])[0]
    st.success(f"🌾 Predicted Crop Yield: {pred:.2f} tons/ha")

# -----------------------------------------------------------------------------------
# 🌫️ Air Pollution
# -----------------------------------------------------------------------------------
elif page == "🌫️ Air Pollution Monitoring":
    st.header("🌫️ Air Pollution Monitoring & Health Risk")

    city = st.text_input("Enter City Name", "Delhi")
    st.write(f"Fetching air quality data for **{city}**...")

    try:
        url = f"https://api.openaq.org/v2/latest?city={city}&parameter=pm25"
        data = requests.get(url).json()
        if data.get("results"):
            results = data["results"]
            df = pd.DataFrame([
                {
                    "Location": loc["location"],
                    "PM2.5": loc["measurements"][0]["value"]
                } for loc in results
            ])
            st.dataframe(df)
            high_pollution = df[df["PM2.5"] > 100]
            if not high_pollution.empty:
                st.warning("⚠️ High Pollution Alert!")
            else:
                st.success("✅ Air quality within acceptable range.")
        else:
            st.error("No live data found for this city.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# -----------------------------------------------------------------------------------
# 📰 Misinformation Detection
# -----------------------------------------------------------------------------------
elif page == "📰 Misinformation Detection":
    st.header("📰 Misinformation & AI Content Detection")

    # Basic training dataset
    data = [
        ("Vaccines cause autism", 1),
        ("Climate change is real", 0),
        ("Drinking bleach cures disease", 1),
        ("Earth is flat", 1),
        ("Vaccines save lives", 0)
    ]
    texts, labels = zip(*data)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    model = MultinomialNB().fit(X, labels)

    st.write("Enter a statement to check for misinformation:")
    user_input = st.text_area("Text to Analyze", "Type something here...")
    if st.button("Analyze"):
        X_test = vectorizer.transform([user_input])
        pred = model.predict(X_test)[0]
        if pred == 1:
            st.error("⚠️ Likely Misinformation Detected!")
        else:
            st.success("✅ Seems Reliable")

# -----------------------------------------------------------------------------------
# ⚡ Electricity Grid Monitoring
# -----------------------------------------------------------------------------------
elif page == "⚡ Electricity Grid Monitoring":
    st.header("⚡ Electricity Grid / Blackout Risk Monitoring")

    st.write("Upload electricity data (`Date`, `Demand_MW`, `Supply_MW`) or use sample:")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        df = pd.DataFrame({
            "Date": pd.date_range("2024-01-01", periods=12, freq="M"),
            "Demand_MW": [950, 970, 990, 1010, 1020, 980, 970, 960, 940, 930, 920, 910],
            "Supply_MW": [940, 950, 970, 1000, 1010, 970, 950, 940, 930, 920, 910, 900]
        })

    df['Date'] = pd.to_datetime(df['Date'])
    df['Deficit'] = df['Demand_MW'] - df['Supply_MW']

    st.line_chart(df.set_index('Date')[['Demand_MW', 'Supply_MW']])

    deficit_days = df[df['Deficit'] > 0]
    if not deficit_days.empty:
        st.warning("⚠️ Grid Risk Alerts:")
        st.dataframe(deficit_days[['Date', 'Deficit']])
    else:
        st.success("✅ Grid stable – no deficit detected.")
