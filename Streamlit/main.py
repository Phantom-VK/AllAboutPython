import streamlit as st
import pandas as pd
import numpy as np

# ========================================
# 1. PAGE CONFIGURATION (must be first command)
# ========================================
st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================================
# 2. TITLE AND HEADERS
# ========================================
st.title("📈 Streamlit Data Explorer")
st.subheader("Interactive Data Visualization")
st.write("This app demonstrates Streamlit's core features")


# ========================================
# 3. DATA LOADING
# ========================================
@st.cache_data  # Cache for performance
def load_data():
    return pd.DataFrame({
        "first_col": [1, 2, 3, 4],
        "second_col": [3, 4, 5, 5],
        "random_values": np.random.randn(4)
    })


df = load_data()

# ========================================
# 4. DATA DISPLAY
# ========================================
st.header("📋 Data Display")
st.write("Current DataFrame:")
st.dataframe(df.style.highlight_max(axis=0), width=800)

# Expander for raw data
with st.expander("Show raw data"):
    st.write(df)

# ========================================
# 5. INTERACTIVE WIDGETS
# ========================================
st.header("🎛 Controls")
col1, col2 = st.columns(2)

with col1:
    n_rows = st.slider("Select rows to show", 1, len(df), 2)

with col2:
    selected_col = st.selectbox(
        "Choose column to plot",
        df.columns
    )

# ========================================
# 6. VISUALIZATIONS
# ========================================
st.header("📊 Charts")

tab1, tab2, tab3 = st.tabs(["Line Chart", "Area Chart", "Bar Chart"])

with tab1:
    st.line_chart(df[selected_col].head(n_rows))
    st.caption("Line chart showing selected data")

with tab2:
    st.area_chart(df.head(n_rows))

with tab3:
    st.bar_chart(df.head(n_rows))

# ========================================
# 7. SIDEBAR COMPONENTS
# ========================================
with st.sidebar:
    st.header("Settings")
    show_table = st.checkbox("Show full table", True)
    chart_type = st.radio(
        "Chart style",
        ["Default", "Altair", "Plotly"]
    )

    st.color_picker("Choose theme color", "#00f900")

# Conditional display based on sidebar
if show_table:
    st.dataframe(df)

# ========================================
# 8. ADVANCED FEATURES
# ========================================
st.header("✨ Advanced Features")

# File uploader
uploaded_file = st.file_uploader("Upload your own CSV")
if uploaded_file:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write(uploaded_df.head())

# Session state counter
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1

st.write(f"Current count: {st.session_state.counter}")

# ========================================
# 9. METRICS & KPIs
# ========================================
st.metric(label="Total Rows", value=len(df), delta=2)

# ========================================
# 10. LAYOUT OPTIMIZATION
# ========================================
col1, col2, col3 = st.columns(3)
col1.metric("Mean", df.mean().round(2)[0])
col2.metric("Median", df.median()[0])
col3.metric("Std Dev", df.std().round(2)[0])