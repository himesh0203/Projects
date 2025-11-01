Install dependencies
pip install streamlit pandas scikit-learn matplotlib requests folium streamlit-folium

▶️ Run
streamlit run global_dashboard_with_maps.py


Then open http://localhost:8501 in your browser.





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Global Challenges Dashboard 2025", layout="wide")

st.title("🌍 Global Challenges Dashboard (with Maps)")
st.sidebar.header("Select a Global Problem to Explore")

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
# 💧 WATER SCARCITY & DROUGHT MONITORING
# -----------------------------------------------------------------------------------
if page == "💧 Water Scarcity & Drought Monitoring":
    st.header("💧 Water Scarcity & Drought Monitoring")

    st.write("Upload rainfall data (`Region`, `Lat`, `Lon`, `Rainfall_mm`) or use sample data:")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        df = pd.DataFrame({
            "Region": ["India", "Kenya", "USA", "Brazil", "Australia"],
            "Lat": [20.59, -0.02, 37.09, -14.24, -25.27],
            "Lon": [78.96, 37.90, -95.71, -51.92, 133.77],
            "Rainfall_mm": [35, 45, 120, 90, 40]
        })
        st.info("Using sample rainfall data.")

    drought_threshold = st.slider("Set Drought Threshold (mm/month)", 10, 200, 50)
    drought_zones = df[df["Rainfall_mm"] < drought_threshold]

    # Map
    st.subheader("🗺️ Global Rainfall Map")
    m = folium.Map(location=[10, 10], zoom_start=2)
    for _, row in df.iterrows():
        color = "red" if row["Rainfall_mm"] < drought_threshold else "green"
        folium.CircleMarker(
            location=[row["Lat"], row["Lon"]],
            radius=8,
            color=color,
            fill=True,
            fill_opacity=0.7,
            popup=f"{row['Region']}: {row['Rainfall_mm']} mm"
        ).add_to(m)
    st_folium(m, width=700, height=400)

    if not drought_zones.empty:
        st.warning("⚠️ Drought Alert Regions:")
        st.dataframe(drought_zones)
    else:
        st.success("✅ No drought risk detected.")

# -----------------------------------------------------------------------------------
# 🌾 FOOD SECURITY / AGRICULTURE YIELD PREDICTION
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
# 🌫️ AIR POLLUTION MONITORING (with MAP)
# -----------------------------------------------------------------------------------
elif page == "🌫️ Air Pollution Monitoring":
    st.header("🌫️ Air Pollution Monitoring & Health Risk")

    st.write("Enter a city to visualize air quality (using OpenAQ API):")
    city = st.text_input("City Name", "Delhi")

    try:
        url = f"https://api.openaq.org/v2/latest?city={city}&parameter=pm25"
        data = requests.get(url).json()

        if data.get("results"):
            results = data["results"]
            df = pd.DataFrame([
                {
                    "Location": loc["location"],
                    "Lat": loc["coordinates"]["latitude"],
                    "Lon": loc["coordinates"]["longitude"],
                    "PM2.5": loc["measurements"][0]["value"]
                } for loc in results
            ])

            st.dataframe(df)

            # Map
            st.subheader("🗺️ Air Quality Map")
            m = folium.Map(location=[df["Lat"].mean(), df["Lon"].mean()], zoom_start=8)
            for _, row in df.iterrows():
                color = "red" if row["PM2.5"] > 100 else "green"
                folium.CircleMarker(
                    location=[row["Lat"], row["Lon"]],
                    radius=8,
                    color=color,
                    fill=True,
                    fill_opacity=0.7,
                    popup=f"{row['Location']}: {row['PM2.5']} μg/m³"
                ).add_to(m)
            st_folium(m, width=700, height=400)

            if (df["PM2.5"] > 100).any():
                st.warning("⚠️ High Pollution Detected!")
            else:
                st.success("✅ Air quality is acceptable.")
        else:
            st.error("No data found for this city.")
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# -----------------------------------------------------------------------------------
# 📰 MISINFORMATION DETECTION
# -----------------------------------------------------------------------------------
elif page == "📰 Misinformation Detection":
    st.header("📰 Misinformation & AI Content Detection")

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
# ⚡ ELECTRICITY GRID MONITORING
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
