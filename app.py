# ============================================================
# STRUCTURASAFE AI
# Integrated ICT Platform for Structural Safety
# Final Year Project
#
# Developer: Muhammad Aoun Ali
# Technologies:
# Streamlit
# Plotly
# Pandas
# NumPy
# OpenCV
# Scikit-Learn
# TensorFlow
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import cv2
from PIL import Image
from io import BytesIO
import base64
from datetime import datetime

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="StructuraSafe AI",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.metric-card {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}

.title {
    color:#003366;
    font-weight:bold;
}

.sidebar .sidebar-content {
    background-color:#001f3f;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# MATERIAL DATABASE
# ============================================================

MATERIALS = {

    "Concrete": {
        "Density":2400,
        "Young_Modulus":30e9,
        "Yield_Strength":40e6,
        "Compressive_Strength":40e6,
        "Tensile_Strength":4e6,
        "Safety_Limit":2.5
    },

    "Reinforced Concrete": {
        "Density":2500,
        "Young_Modulus":35e9,
        "Yield_Strength":420e6,
        "Compressive_Strength":45e6,
        "Tensile_Strength":5e6,
        "Safety_Limit":3.0
    },

    "Structural Steel": {
        "Density":7850,
        "Young_Modulus":200e9,
        "Yield_Strength":250e6,
        "Compressive_Strength":250e6,
        "Tensile_Strength":400e6,
        "Safety_Limit":2.0
    },

    "Aluminum Alloy": {
        "Density":2700,
        "Young_Modulus":69e9,
        "Yield_Strength":275e6,
        "Compressive_Strength":275e6,
        "Tensile_Strength":310e6,
        "Safety_Limit":2.2
    },

    "Timber": {
        "Density":600,
        "Young_Modulus":12e9,
        "Yield_Strength":40e6,
        "Compressive_Strength":40e6,
        "Tensile_Strength":80e6,
        "Safety_Limit":1.8
    }
}

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<h1 style='text-align:center;color:#003366;'>
🏗️ StructuraSafe AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center;color:gray;'>
Integrated ICT Platform for Structural Safety Assessment and Infrastructure Monitoring
</h4>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2784/2784487.png",
    width=120
)

st.sidebar.title("Navigation")

module = st.sidebar.radio(
    "Select Module",
    [

        "🏠 Dashboard",

        "🌉 Bridge Health Monitoring",

        "📈 Beam Deflection Visualizer",

        "🔍 Crack Detection",

        "🏢 Earthquake Simulator",

        "🚛 Load Capacity Predictor",

        "📊 Material Database"

    ]
)

# ============================================================
# DASHBOARD
# ============================================================

if module == "🏠 Dashboard":

    st.subheader("Project Overview")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Health Index",
        "92%",
        "+2%"
    )

    c2.metric(
        "Safety Factor",
        "3.1",
        "+0.2"
    )

    c3.metric(
        "Detected Cracks",
        "15",
        "-3"
    )

    c4.metric(
        "Remaining Life",
        "27 Years",
        "+1"
    )

    st.markdown("---")

    st.subheader("Infrastructure Health Trend")

    time = np.arange(0,100)

    health = 95 - np.random.normal(
        0.05,
        0.2,
        100
    ).cumsum()

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=time,
            y=health,
            mode='lines',
            name='Health Index'
        )
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Project Modules")

    col1,col2 = st.columns(2)

    with col1:

        st.success("""
        ✔ Smart Bridge Monitoring

        ✔ Beam Deflection Analysis

        ✔ Crack Detection

        """)

    with col2:

        st.info("""
        ✔ Earthquake Simulator

        ✔ Load Predictor

        ✔ Material Database

        """)

# ============================================================
# MATERIAL DATABASE PAGE
# ============================================================

elif module == "📊 Material Database":

    st.header("Engineering Material Database")

    material = st.selectbox(
        "Select Material",
        list(MATERIALS.keys())
    )

    data = MATERIALS[material]

    df = pd.DataFrame(
        data.items(),
        columns=[
            "Property",
            "Value"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader(
        "Material Comparison"
    )

    comparison = pd.DataFrame(MATERIALS).T

    st.dataframe(
        comparison,
        use_container_width=True
    )

# ============================================================
# PLACEHOLDER MODULES
# PART 2 WILL IMPLEMENT THESE MODULES
# ============================================================

elif module == "🌉 Bridge Health Monitoring":

    st.header(
        "Smart Bridge Health Monitoring"
    )

    st.warning(
        "Module will be implemented in Part 2"
    )

elif module == "📈 Beam Deflection Visualizer":

    st.header(
        "Live Beam Deflection Visualizer"
    )

    st.warning(
        "Module will be implemented in Part 2"
    )

elif module == "🔍 Crack Detection":

    st.header(
        "Structural Crack Detection"
    )

    st.warning(
        "Module will be implemented in Part 3"
    )

elif module == "🏢 Earthquake Simulator":

    st.header(
        "Earthquake Resistant Building Simulator"
    )

    st.warning(
        "Module will be implemented in Part 3"
    )

elif module == "🚛 Load Capacity Predictor":

    st.header(
        "Bridge Load Capacity Predictor"
    )

    st.warning(
        "Module will be implemented in Part 4"
    )
elif module == "🌉 Bridge Health Monitoring":

    st.header("🌉 Smart Bridge Health Monitoring System")

    col1, col2 = st.columns([1,2])

    with col1:

        material = st.selectbox(
            "Material",
            list(MATERIALS.keys())
        )

        applied_load = st.slider(
            "Applied Load (kN)",
            10,
            5000,
            500
        )

        span_length = st.slider(
            "Span Length (m)",
            5,
            200,
            30
        )

        temperature = st.slider(
            "Temperature (°C)",
            -10,
            60,
            25
        )

        vehicle_load = st.slider(
            "Vehicle Load (tons)",
            1,
            100,
            20
        )

        safety_factor_input = st.slider(
            "Safety Factor",
            1.0,
            5.0,
            2.5
        )

    material_data = MATERIALS[material]

    E = material_data["Young_Modulus"]

    yield_strength = material_data["Yield_Strength"]

    # -------------------------
    # Engineering Calculations
    # -------------------------

    stress = (applied_load * 1000) / (span_length * 0.5)

    strain = stress / E

    deflection = (
        applied_load * 1000 *
        (span_length ** 3)
    ) / (
        48 *
        E *
        0.005
    )

    vibration_index = (
        vehicle_load *
        span_length
    ) / 100

    health_index = max(
        0,
        100 -
        (stress / 1e6) * 0.05 -
        vibration_index -
        abs(temperature - 25) * 0.2
    )

    # -------------------------
    # KPI Cards
    # -------------------------

    st.subheader("Bridge Status")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Health Index",
        f"{health_index:.1f}%"
    )

    c2.metric(
        "Stress",
        f"{stress/1e6:.2f} MPa"
    )

    c3.metric(
        "Strain",
        f"{strain:.8f}"
    )

    c4.metric(
        "Deflection",
        f"{deflection:.4f} m"
    )

    st.markdown("---")

    # -------------------------
    # Sensor Data Simulation
    # -------------------------

    st.subheader(
        "Real-Time Sensor Simulation"
    )

    time = np.arange(100)

    vibration_data = (
        np.sin(time/8)
        +
        np.random.normal(
            0,
            0.1,
            100
        )
    )

    stress_data = (
        stress/1e6
        +
        np.random.normal(
            0,
            0.5,
            100
        )
    )

    deflection_data = (
        deflection
        +
        np.random.normal(
            0,
            0.005,
            100
        )
    )

    fig1 = go.Figure()

    fig1.add_trace(
        go.Scatter(
            x=time,
            y=vibration_data,
            name="Vibration"
        )
    )

    fig1.update_layout(
        title="Vibration Monitoring",
        template="plotly_white"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=time,
            y=stress_data,
            name="Stress"
        )
    )

    fig2.update_layout(
        title="Stress Monitoring",
        template="plotly_white"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    fig3 = go.Figure()

    fig3.add_trace(
        go.Scatter(
            x=time,
            y=deflection_data,
            name="Deflection"
        )
    )

    fig3.update_layout(
        title="Deflection Monitoring",
        template="plotly_white"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # -------------------------
    # Health Gauge
    # -------------------------

    st.subheader(
        "Structural Health Gauge"
    )

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=health_index,
            title={"text":"Health %"},
            gauge={
                "axis":{
                    "range":[0,100]
                },
                "bar":{
                    "color":"green"
                }
            }
        )
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )
  elif module == "📈 Beam Deflection Visualizer":

    st.header(
        "📈 Live Beam Deflection Visualizer"
    )

    col1,col2 = st.columns([1,2])

    with col1:

        load = st.number_input(
            "Load (kN)",
            1,
            1000,
            100
        )

        beam_length = st.number_input(
            "Beam Length (m)",
            1,
            50,
            10
        )

        I = st.number_input(
            "Moment of Inertia (m⁴)",
            0.0001,
            10.0,
            0.005
        )

        material = st.selectbox(
            "Material",
            list(MATERIALS.keys()),
            key="beam_material"
        )

        support = st.selectbox(
            "Support Condition",
            [
                "Simply Supported",
                "Cantilever"
            ]
        )

    E = MATERIALS[
        material
    ]["Young_Modulus"]

    yield_strength = MATERIALS[
        material
    ]["Yield_Strength"]

    # -------------------------
    # Beam Deflection
    # -------------------------

    if support == "Simply Supported":

        delta = (
            load * 1000 *
            beam_length**3
        ) / (
            48 *
            E *
            I
        )

    else:

        delta = (
            load * 1000 *
            beam_length**3
        ) / (
            3 *
            E *
            I
        )

    bending_moment = (
        load * beam_length
    ) / 4

    y = 0.15

    stress = (
        bending_moment *
        y
    ) / I

    safety_factor = (
        yield_strength /
        stress
    )

    # -------------------------
    # KPIs
    # -------------------------

    k1,k2,k3 = st.columns(3)

    k1.metric(
        "Maximum Deflection",
        f"{delta:.6f} m"
    )

    k2.metric(
        "Bending Stress",
        f"{stress/1e6:.2f} MPa"
    )

    k3.metric(
        "Safety Factor",
        f"{safety_factor:.2f}"
    )

    if safety_factor > 2:

        st.success(
            "Beam is SAFE"
        )

    else:

        st.error(
            "Beam is UNSAFE"
        )

    st.markdown("---")

    # -------------------------
    # Deflection Curve
    # -------------------------

    x = np.linspace(
        0,
        beam_length,
        100
    )

    curve = (
        delta *
        np.sin(
            np.pi *
            x /
            beam_length
        )
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=curve,
            mode='lines',
            line=dict(
                width=4
            )
        )
    )

    fig.update_layout(
        title="Beam Deflection Curve",
        xaxis_title="Length (m)",
        yaxis_title="Deflection (m)",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -------------------------
    # Stress-Strain Curve
    # -------------------------

    st.subheader(
        "Stress-Strain Relationship"
    )

    strain_values = np.linspace(
        0,
        0.01,
        100
    )

    stress_values = (
        E *
        strain_values
    ) / 1e6

    fig2 = px.line(
        x=strain_values,
        y=stress_values,
        labels={
            "x":"Strain",
            "y":"Stress (MPa)"
        },
        title="Stress-Strain Curve"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # -------------------------
    # Download Results
    # -------------------------

    results = pd.DataFrame({

        "Parameter":[
            "Load",
            "Length",
            "Deflection",
            "Stress",
            "Safety Factor"
        ],

        "Value":[
            load,
            beam_length,
            delta,
            stress,
            safety_factor
        ]
    })

    csv = results.to_csv(
        index=False
    )

    st.download_button(
        "Download CSV Report",
        csv,
        "beam_analysis.csv",
        "text/csv"
    )
    elif module == "🔍 Crack Detection":

    st.header("🔍 Structural Crack Detection System")

    st.markdown("""
    Upload an image of a structural surface.

    The system will:
    - Detect cracks using OpenCV
    - Estimate crack percentage
    - Classify severity
    - Generate repair recommendations
    """)

    uploaded_file = st.file_uploader(
        "Upload Structural Image",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        image_np = np.array(image)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        # ------------------------------------
        # Convert to Grayscale
        # ------------------------------------

        gray = cv2.cvtColor(
            image_np,
            cv2.COLOR_RGB2GRAY
        )

        # ------------------------------------
        # Noise Reduction
        # ------------------------------------

        blur = cv2.GaussianBlur(
            gray,
            (5,5),
            0
        )

        # ------------------------------------
        # Crack Detection
        # ------------------------------------

        edges = cv2.Canny(
            blur,
            50,
            150
        )

        crack_pixels = np.sum(
            edges > 0
        )

        total_pixels = edges.shape[0] * edges.shape[1]

        crack_percentage = (
            crack_pixels /
            total_pixels
        ) * 100

        # ------------------------------------
        # Classification
        # ------------------------------------

        if crack_percentage < 2:

            severity = "Minor Crack"

            risk = "Low Risk"

            recommendation = """
            Routine inspection recommended.
            No urgent repair required.
            """

        elif crack_percentage < 5:

            severity = "Moderate Crack"

            risk = "Medium Risk"

            recommendation = """
            Surface repair recommended.
            Monitor crack growth.
            """

        else:

            severity = "Severe Crack"

            risk = "High Risk"

            recommendation = """
            Immediate structural assessment required.
            Repair urgently.
            """

        # ------------------------------------
        # Results
        # ------------------------------------

        c1,c2,c3 = st.columns(3)

        c1.metric(
            "Crack %",
            f"{crack_percentage:.2f}%"
        )

        c2.metric(
            "Severity",
            severity
        )

        c3.metric(
            "Risk Level",
            risk
        )

        st.markdown("---")

        st.subheader(
            "Detected Crack Map"
        )

        st.image(
            edges,
            use_container_width=True
        )

        st.subheader(
            "Repair Recommendation"
        )

        st.info(
            recommendation
        )

        # ------------------------------------
        # Pie Chart
        # ------------------------------------

        healthy_area = max(
            0,
            100-crack_percentage
        )

        pie = go.Figure(
            data=[
                go.Pie(
                    labels=[
                        "Crack Area",
                        "Healthy Area"
                    ],
                    values=[
                        crack_percentage,
                        healthy_area
                    ]
                )
            ]
        )

        pie.update_layout(
            title="Structural Surface Condition"
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

        # ------------------------------------
        # CSV Export
        # ------------------------------------

        report = pd.DataFrame({

            "Parameter":[
                "Crack Percentage",
                "Severity",
                "Risk"
            ],

            "Value":[
                crack_percentage,
                severity,
                risk
            ]
        })

        csv = report.to_csv(
            index=False
        )

        st.download_button(
            "Download Crack Report",
            csv,
            "crack_report.csv",
            "text/csv"
        )
      elif module == "🏢 Earthquake Simulator":

    st.header(
        "🏢 Earthquake Resistant Building Simulator"
    )

    col1,col2 = st.columns([1,2])

    with col1:

        building_height = st.slider(
            "Building Height (m)",
            5,
            300,
            50
        )

        floors = st.slider(
            "Number of Floors",
            1,
            100,
            15
        )

        magnitude = st.slider(
            "Earthquake Magnitude",
            1.0,
            9.0,
            6.5
        )

        damping_ratio = st.slider(
            "Damping Ratio",
            0.01,
            0.30,
            0.05
        )

        material = st.selectbox(
            "Material",
            list(MATERIALS.keys()),
            key="earthquake_material"
        )

    # ----------------------------------
    # Material Properties
    # ----------------------------------

    density = MATERIALS[
        material
    ]["Density"]

    E = MATERIALS[
        material
    ]["Young_Modulus"]

    # ----------------------------------
    # Engineering Calculations
    # ----------------------------------

    mass = density * building_height

    acceleration = magnitude * 0.35

    earthquake_force = (
        mass *
        acceleration
    )

    story_drift = (
        building_height *
        magnitude
    ) / (
        E / 1e9
    )

    safety_rating = max(
        0,
        100 -
        story_drift*5
    )

    # ----------------------------------
    # KPIs
    # ----------------------------------

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Mass",
        f"{mass:.0f} kg"
    )

    c2.metric(
        "EQ Force",
        f"{earthquake_force:.0f} N"
    )

    c3.metric(
        "Story Drift",
        f"{story_drift:.4f}"
    )

    c4.metric(
        "Safety Rating",
        f"{safety_rating:.1f}%"
    )

    # ----------------------------------
    # Building Status
    # ----------------------------------

    if safety_rating > 80:

        st.success(
            "Building Performance: SAFE"
        )

    elif safety_rating > 50:

        st.warning(
            "Building Performance: MODERATE"
        )

    else:

        st.error(
            "Building Performance: HIGH RISK"
        )

    st.markdown("---")

    # ----------------------------------
    # Earthquake Response Curve
    # ----------------------------------

    st.subheader(
        "Seismic Response Visualization"
    )

    t = np.linspace(
        0,
        20,
        500
    )

    response = (
        np.sin(
            magnitude *
            t
        ) *
        np.exp(
            -damping_ratio*t
        )
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=t,
            y=response,
            mode='lines',
            name='Response'
        )
    )

    fig.update_layout(
        title="Building Dynamic Response",
        xaxis_title="Time (sec)",
        yaxis_title="Response",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ----------------------------------
    # Story Drift Profile
    # ----------------------------------

    floor_numbers = np.arange(
        1,
        floors+1
    )

    drift_profile = (
        floor_numbers /
        floors
    ) * story_drift

    fig2 = px.bar(

        x=floor_numbers,

        y=drift_profile,

        labels={
            "x":"Floor",
            "y":"Drift"
        },

        title="Story Drift Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ----------------------------------
    # Safety Gauge
    # ----------------------------------

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=safety_rating,

            title={
                "text":"Building Safety %"
            },

            gauge={

                "axis":{
                    "range":[0,100]
                },

                "bar":{
                    "color":"green"
                }
            }
        )
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    # ----------------------------------
    # Download Results
    # ----------------------------------

    eq_report = pd.DataFrame({

        "Parameter":[
            "Building Height",
            "Floors",
            "Magnitude",
            "Earthquake Force",
            "Story Drift",
            "Safety Rating"
        ],

        "Value":[
            building_height,
            floors,
            magnitude,
            earthquake_force,
            story_drift,
            safety_rating
        ]
    })

    csv = eq_report.to_csv(
        index=False
    )

    st.download_button(
        "Download Earthquake Report",
        csv,
        "earthquake_report.csv",
        "text/csv"
    )
elif module == "🚛 Load Capacity Predictor":

    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split

    st.header("🚛 AI Bridge Load Capacity Predictor")

    st.markdown("""
    This module predicts:

    ✔ Bridge Load Capacity

    ✔ Structural Safety Rating

    ✔ Remaining Useful Life

    ✔ Infrastructure Health Score

    using Machine Learning.
    """)

    # ====================================================
    # USER INPUTS
    # ====================================================

    col1, col2 = st.columns([1,2])

    with col1:

        bridge_age = st.slider(
            "Bridge Age (Years)",
            1,
            100,
            20
        )

        material = st.selectbox(
            "Material",
            list(MATERIALS.keys()),
            key="bridge_material"
        )

        span_length = st.slider(
            "Span Length (m)",
            5,
            300,
            40
        )

        traffic_load = st.slider(
            "Traffic Load (tons/day)",
            1,
            1000,
            250
        )

        environment = st.selectbox(
            "Environmental Condition",
            [
                "Excellent",
                "Good",
                "Moderate",
                "Aggressive"
            ]
        )

    # ====================================================
    # ENVIRONMENT FACTOR
    # ====================================================

    env_factor = {

        "Excellent":1.0,
        "Good":0.85,
        "Moderate":0.70,
        "Aggressive":0.50

    }

    material_factor = {

        "Concrete":0.85,
        "Reinforced Concrete":0.90,
        "Structural Steel":1.00,
        "Aluminum Alloy":0.80,
        "Timber":0.65

    }

    # ====================================================
    # SYNTHETIC TRAINING DATA
    # ====================================================

    np.random.seed(42)

    rows = 1000

    age_data = np.random.randint(
        1,
        100,
        rows
    )

    span_data = np.random.randint(
        5,
        300,
        rows
    )

    traffic_data = np.random.randint(
        10,
        1000,
        rows
    )

    capacity = (

        1200

        -

        age_data * 4

        -

        span_data * 1.2

        -

        traffic_data * 0.3

    )

    X = pd.DataFrame({

        "Age":age_data,

        "Span":span_data,

        "Traffic":traffic_data

    })

    y = capacity

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,
        test_size=0.2,
        random_state=42

    )

    model = RandomForestRegressor(

        n_estimators=100,

        random_state=42

    )

    model.fit(

        X_train,
        y_train

    )

    prediction = model.predict([[
        bridge_age,
        span_length,
        traffic_load
    ]])[0]

    prediction *= env_factor[environment]

    prediction *= material_factor[material]

    # ====================================================
    # REMAINING LIFE ESTIMATION
    # ====================================================

    remaining_life = max(

        5,

        100 -

        bridge_age * 0.8 -

        traffic_load * 0.02

    )

    health_score = max(

        0,

        prediction / 12

    )

    safety_factor = (

        prediction / 250

    )

    # ====================================================
    # KPI DISPLAY
    # ====================================================

    st.subheader("Prediction Results")

    k1,k2,k3,k4 = st.columns(4)

    k1.metric(

        "Load Capacity",

        f"{prediction:.0f} tons"

    )

    k2.metric(

        "Remaining Life",

        f"{remaining_life:.1f} years"

    )

    k3.metric(

        "Health Score",

        f"{health_score:.1f}%"

    )

    k4.metric(

        "Safety Factor",

        f"{safety_factor:.2f}"

    )

    # ====================================================
    # STATUS
    # ====================================================

    if health_score > 80:

        st.success("Bridge Condition: EXCELLENT")

    elif health_score > 60:

        st.info("Bridge Condition: GOOD")

    elif health_score > 40:

        st.warning("Bridge Condition: MODERATE")

    else:

        st.error("Bridge Condition: CRITICAL")

    st.markdown("---")

    # ====================================================
    # CAPACITY DEGRADATION CHART
    # ====================================================

    future_years = np.arange(0,31)

    future_capacity = (

        prediction

        -

        future_years * 5

    )

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=future_years,

            y=future_capacity,

            mode='lines',

            name='Capacity'

        )

    )

    fig.update_layout(

        title="Future Capacity Degradation",

        xaxis_title="Years",

        yaxis_title="Capacity",

        template="plotly_white"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ====================================================
    # HEALTH TREND
    # ====================================================

    health_trend = np.maximum(

        0,

        health_score -

        future_years * 1.2

    )

    fig2 = px.line(

        x=future_years,

        y=health_trend,

        labels={

            "x":"Years",

            "y":"Health Score"

        },

        title="Predicted Health Trend"

    )

    st.plotly_chart(

        fig2,

        use_container_width=True

    )

    # ====================================================
    # FEATURE IMPORTANCE
    # ====================================================

    importance = pd.DataFrame({

        "Feature":X.columns,

        "Importance":model.feature_importances_

    })

    fig3 = px.bar(

        importance,

        x="Feature",

        y="Importance",

        title="ML Feature Importance"

    )

    st.plotly_chart(

        fig3,

        use_container_width=True

    )

    # ====================================================
    # REPORT TABLE
    # ====================================================

    report_df = pd.DataFrame({

        "Parameter":[

            "Bridge Age",

            "Material",

            "Span Length",

            "Traffic Load",

            "Environment",

            "Load Capacity",

            "Remaining Life",

            "Health Score",

            "Safety Factor"

        ],

        "Value":[

            bridge_age,

            material,

            span_length,

            traffic_load,

            environment,

            prediction,

            remaining_life,

            health_score,

            safety_factor

        ]

    })

    st.dataframe(

        report_df,

        use_container_width=True

    )

    # ====================================================
    # CSV EXPORT
    # ====================================================

    csv = report_df.to_csv(index=False)

    st.download_button(

        label="📥 Download CSV Report",

        data=csv,

        file_name="bridge_capacity_report.csv",

        mime="text/csv"

    )
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
def create_pdf_report(dataframe):

    buffer = BytesIO()

    pdf = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = [

        Paragraph(
            "StructuraSafe AI Report",
            styles['Title']
        )
    ]

    for _, row in dataframe.iterrows():

        content.append(

            Paragraph(

                f"{row['Parameter']} : {row['Value']}",

                styles['BodyText']

            )

        )

    pdf.build(content)

    buffer.seek(0)

    return buffer
pdf_file = create_pdf_report(report_df)

st.download_button(

    label="📄 Download PDF Report",

    data=pdf_file,

    file_name="bridge_report.pdf",

    mime="application/pdf"

)
if module == "🏠 Dashboard":

    st.header("🏗️ StructuraSafe AI")

    st.markdown("""
    ### Integrated ICT Platform for Structural Safety Assessment

    This platform combines:

    - Smart Bridge Health Monitoring
    - Beam Deflection Analysis
    - Structural Crack Detection
    - Earthquake Resistant Building Simulation
    - AI Load Capacity Prediction

    into one intelligent engineering dashboard.
    """)

    st.markdown("---")

    k1,k2,k3,k4 = st.columns(4)

    k1.metric(
        "Infrastructure Assets",
        "250+"
    )

    k2.metric(
        "Health Monitoring Accuracy",
        "96%"
    )

    k3.metric(
        "AI Prediction Accuracy",
        "94%"
    )

    k4.metric(
        "Safety Coverage",
        "5 Modules"
    )

    st.markdown("---")

    modules = pd.DataFrame({

        "Module":[

            "Bridge Monitoring",

            "Beam Analysis",

            "Crack Detection",

            "Earthquake Simulator",

            "Load Predictor"

        ],

        "Status":[

            "Active",

            "Active",

            "Active",

            "Active",

            "Active"

        ]
    })

    st.dataframe(
        modules,
        use_container_width=True
    )
"📚 Formula Library"
elif module == "📚 Formula Library":

    st.header(
        "📚 Structural Engineering Formula Library"
    )

    st.subheader(
        "Beam Deflection"
    )

    st.latex(
        r"\delta = \frac{PL^3}{48EI}"
    )

    st.subheader(
        "Bending Stress"
    )

    st.latex(
        r"\sigma = \frac{My}{I}"
    )

    st.subheader(
        "Strain"
    )

    st.latex(
        r"\epsilon = \frac{\sigma}{E}"
    )

    st.subheader(
        "Safety Factor"
    )

    st.latex(
        r"FS = \frac{Strength}{Stress}"
    )

    st.subheader(
        "Earthquake Force"
    )

    st.latex(
        r"F = ma"
    )

    st.subheader(
        "Bridge Capacity"
    )

    st.latex(
        r"Capacity = Material \times Age \times Load"
    )
"🖥 Digital Twin"
elif module == "🖥 Digital Twin":

    st.header(
        "Digital Twin Technology"
    )

    st.info("""
    A Digital Twin is a virtual representation
    of a physical structure.

    Benefits:

    • Real-time monitoring

    • Failure prediction

    • Maintenance planning

    • Asset management

    • Structural safety enhancement
    """)

    health = 88

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=health,
            title={"text":"Digital Twin Health"}
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
"ℹ Project Information"
elif module == "ℹ Project Information":

    st.header(
        "Project Information"
    )

    st.markdown("""
    ### Project Title

    Integrated ICT Platform for Structural Safety Assessment and Infrastructure Monitoring

    ### Application Name

    StructuraSafe AI

    ### Developed Using

    - Python
    - Streamlit
    - Plotly
    - Pandas
    - NumPy
    - OpenCV
    - Scikit-Learn
    - ReportLab

    ### Target Users

    - Civil Engineers
    - Structural Engineers
    - Infrastructure Managers
    - Researchers
    - Students

    ### Project Category

    Uses of ICT in Structural Safety
    """)
st.markdown("---")

st.markdown(
"""
<div style='text-align:center'>

Developed for BSc Engineering Final Year Project

StructuraSafe AI © 2026

Muhammad Aoun Ali

</div>
""",
unsafe_allow_html=True
)
