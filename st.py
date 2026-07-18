import streamlit as st
import pandas as pd
import numpy as np
# from streamlit_option_menu import option_menu
# import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
df=pd.read_csv("Amazon (3).csv")
df1=pd.read_csv("Amazon_c.csv")
# ---------- Professional Graph Theme --------
plt.rcParams.update({
    "figure.facecolor": "#1F2937",
    "axes.facecolor": "#1F2937",
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "text.color": "white",
    "grid.color": "#555555",
    "savefig.facecolor": "#1F2937"
})

st.set_page_config(
    page_title="Amazon Sales & Customer Behavior Dashboard",
    page_icon="📦",
    layout="wide"
)
import plotly.io as pio

# ---------- Amazon Orange Theme ----------
amazon_theme = pio.templates["plotly_dark"]

amazon_theme.layout.colorway = [
    "#FF9900",
    "#F7A100",
    "#E47911",
    "#FFB84D",
    "#FFD580",
    "#FFC266",
    "#CC7A00",
    "#FFA31A"
]

amazon_theme.layout.paper_bgcolor = "#131921"
amazon_theme.layout.plot_bgcolor = "#131921"

amazon_theme.layout.font = dict(
    color="white",
    family="Segoe UI",
    size=14
)

amazon_theme.layout.title = dict(
    font=dict(
        color="#FF9900",
        size=22
    )
)

amazon_theme.layout.xaxis = dict(
    gridcolor="#444444",
    zeroline=False
)

amazon_theme.layout.yaxis = dict(
    gridcolor="#444444",
    zeroline=False
)

pio.templates["amazon"] = amazon_theme
pio.templates.default = "amazon"
# ---------- Global Chart Theme ----------
import plotly.io as pio
import matplotlib.pyplot as plt

# Matplotlib Theme
plt.rcParams.update({
    "figure.facecolor": "#131921",
    "axes.facecolor": "#131921",
    "axes.edgecolor": "#FF9900",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "text.color": "white",
    "grid.color": "#555555",
    "savefig.facecolor": "#131921",
    "font.size": 11
})

# Plotly Theme
pio.templates["amazon"] = pio.templates["plotly_dark"]

pio.templates["amazon"].layout.paper_bgcolor = "#131921"
pio.templates["amazon"].layout.plot_bgcolor = "#131921"
pio.templates["amazon"].layout.font = dict(color="white")
pio.templates["amazon"].layout.title = dict(
    font=dict(color="#FF9900", size=22)
)
pio.templates["amazon"].layout.xaxis = dict(
    showgrid=True,
    gridcolor="#444444",
    zeroline=False
)
pio.templates["amazon"].layout.yaxis = dict(
    showgrid=True,
    gridcolor="#444444",
    zeroline=False
)
pio.templates.default = "amazon"
st.markdown("""
<style>

/* Sidebar Background */
[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0B0B0B,#161616,#0B0B0B);
    border-right:2px solid #ff9900;
}

/* Logo */
.sidebar-logo{
    text-align:center;
    color:white;
    font-size:34px;
    font-weight:bold;
    margin-top:10px;
}
.sidebar-logo span{
    color:#ff9900;
}

/* Divider */
.orange-line{
    width:90%;
    height:3px;
    margin:auto;
    margin-top:8px;
    margin-bottom:15px;
    background:#ff9900;
    border-radius:10px;
    box-shadow:0 0 15px #ff9900;
}

/* Footer */
.sidebar-footer{
    text-align:center;
    color:#bbbbbb;
    font-size:13px;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-logo">
🛒 AMAZON <span>EDA</span>
</div>

<div class="orange-line"></div>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Only graph containers */
div[data-testid="stPlotlyChart"],
div[data-testid="stImage"],
div[data-testid="stPyplot"]{
    background: rgba(15,23,42,0.65);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:18px;
    padding:15px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow:0 8px 25px rgba(0,0,0,0.35);
}

</style>
""", unsafe_allow_html=True)



import base64

with open("bg12.png", "rb") as f:
    img = base64.b64encode(f.read()).decode()

st.markdown(f"""
<style>
[data-testid="stSidebar"]::before {{
    content: "";
    display: block;
    width: 100%;
    height: 170px;
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
    border-radius: 0 0 15px 15px;
}}
</style>
""", unsafe_allow_html=True)



# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image:
#         encoded = base64.b64encode(image.read()).decode()
#         st.markdown(
#         f"""
#             <style>
#             .stApp {{
#                 background-image: url("data:image/jpg;base64,{encoded}");
#                 background-size: cover;
#                 background-position: center;
#                 background-repeat: no-repeat;
#                 background-attachment: fixed;
#             }}
#             </style>
#             """,
#             unsafe_allow_html=True
#         )
#         add_bg_from_local("bg1.jpg")
#         st.markdown("""
#         <style>

#         /* Main App Background */
#         .stApp{
#             background: linear-gradient(135deg,#131A22,#232F3E,#1A2533);
#             color:white;
#     }

#     /* Sidebar */
#         [data-testid="stSidebar"]{
#             background: linear-gradient(180deg,#232F3E,#131A22);
#             border-right:2px solid #FF9900;
#         }

#         /* Sidebar Text */
#         [data-testid="stSidebar"] *{
#             color:white !important;
#         }

#         /* Metric Cards */
#         [data-testid="metric-container"]{
#             background:#1F2937;
#             border:2px solid #FF9900;
#             border-radius:18px;
#             padding:18px;
#             box-shadow:0px 5px 15px rgba(255,153,0,0.35);
#         }

#         /* Charts */
#         .plot-container{
#             background:#1F2937;
#             border-radius:18px;
#             padding:10px;
#         }

#         /* Dataframe */
#         [data-testid="stDataFrame"]{
#             background:#1F2937;
#             border-radius:15px;
#         }

#         /* Buttons */
#         .stButton>button{
#             background:#FF9900;
#             color:white;
#             border:none;
#             border-radius:12px;
#             font-weight:bold;
#             transition:0.3s;
#         }

#         .stButton>button:hover{
#             background:#F3A847;
#             transform:scale(1.05);
#         }

#         /* Selectbox */
#         .stSelectbox div[data-baseweb="select"]{
#             background:#1F2937;
#             border-radius:10px;
#         }

#         /* Slider */
#         .stSlider{
#             color:#FF9900;
#         }

#         /* Tabs */
#         .stTabs [data-baseweb="tab"]{
#             background:#232F3E;
#             color:white;
#             border-radius:12px;
#             margin-right:8px;
#         }

#         .stTabs [aria-selected="true"]{
#             background:#FF9900;
#             color:black;
#             font-weight:bold;
#         }

#         /* Expander */
#         .streamlit-expanderHeader{
#             background:#232F3E;
#             color:white;
#             border-radius:10px;
#         }

#         /* Headers */
#         h1,h2,h3{
#             color:#FF9900;
#             font-weight:bold;
#         }

#         /* Horizontal line */
#         hr{
#             border:1px solid #FF9900;
#         }

#         /* Success Message */
#         .stAlert{
#             border-radius:12px;
#         }

#         /* Hover Effect */
#         section.main > div{
#             animation: fadeIn 0.8s ease;
#         }

#         @keyframes fadeIn{
#         from{opacity:0;transform:translateY(10px);}
#         to{opacity:1;transform:translateY(0);}
#         }
#         </style>
#     """, unsafe_allow_html=True)
#     # st.markdown("""
#     # <style>

#     # /* Main Background */
#     # .stApp{
#     #     background: linear-gradient(135deg,#F8F9FA,#EAF4FF,#FFF8E6);
#     # }

#     # /* Sidebar */
#     # section[data-testid="stSidebar"]{
#     #     background: linear-gradient(180deg,#131921,#232F3E,#37475A);
    # }

    # /* Sidebar Text */
    # section[data-testid="stSidebar"] *{
    #     color:white !important;
    #     font-weight:600;
    # }

    # /* Title */
    # h1{
    #     color:#FF9900;
    #     text-align:center;
    # }

    # /* Subtitles */
    # h2,h3{
    #     color:#232F3E;
    # }

    # /* Metric Cards */
    # div[data-testid="stMetric"]{
    #     background:white;
    #     border-left:6px solid #FF9900;
    #     padding:15px;
    #     border-radius:12px;
    #     box-shadow:0px 4px 12px rgba(0,0,0,0.15);
    # }

    # /* DataFrame */
    # div[data-testid="stDataFrame"]{
    #     background:white;
    #     border-radius:12px;
    #     padding:8px;
    #     box-shadow:0px 4px 12px rgba(0,0,0,0.15);
    # }

    # /* Buttons */
    # .stButton>button{
    #     background:#FF9900;
    #     color:white;
    #     border-radius:10px;
    #     font-weight:bold;
    #     border:none;
    # }

    # .stButton>button:hover{
    #     background:#232F3E;
    #     color:white;
    # }

    # /* Tabs */
    # button[data-baseweb="tab"]{
    #     background:#ECECEC;
    #     border-radius:10px;
    #     margin-right:5px;
    #     font-weight:bold;
    # }

    # button[data-baseweb="tab"][aria-selected="true"]{
#     background:#FF9900;
#     color:white;
# }

# /* Charts Container */
# div[data-testid="stPlotlyChart"]{
#     background:white;
#     padding:10px;
#     border-radius:15px;
#     box-shadow:0px 4px 15px rgba(0,0,0,0.15);
# }

# </style>
# """, unsafe_allow_html=True)

# # # Title & Description
# st.title("📦 Amazon Sales & Customer Behavior Analysis")



# st.markdown("""
# This dashboard provides an in-depth **Exploratory Data Analysis (EDA)** of Amazon sales data. 
# It helps visualize key business metrics, including:
# * **Sales Trends:** Tracking revenue patterns over daily, monthly, and yearly periods.
# * **Product Performance:** Identifying top-selling vs low-performing categories.
# * **Customer Behavior:** Analyzing purchasing choices and demographic distributions.
# * **Pricing Insights:** Understanding the direct impact of ratings and discounts on overall demand.
# """)

   






# # Sidebar Navigation
# Behavior:** Analyzing purchasing choices and demographic distributions.
#     * **Pricing Insights:** Understanding the direct impact of ratings and discounts on overall demand.
#     """)
    
    
    
# # --- Data Sets Page ---
# elif menu == "📂Data Sets":
#     st.title("📂 Dataset Selection")
    
#     # Do alag files choose karne ke liye selectbox
#     file_choice = st.sidebar.selectbox("Select File", ["Amazon (3).csv", "Amazon_c.csv"])
        
#     try:
#             if file_choice == "Amazon (3).csv":
#                 df = pd.read_csv("Amazon (3).csv")
#                 st.write("Displaying Amazon.csv")
#             else:
#                 # Apni doosri file ka sahi naam yahan likhein
#                 df = pd.read_csv("Amazon_c.csv") 
#                 st.write("Displaying Amazon_c.csv")
            
st.sidebar.title("AMAZON 📦")
menu = st.sidebar.radio("Go to", ["🏠Dashboard", "📂Data Sets","🧹 Data Cleaning", "📊Graph Data","🛍️3D Visualization","🔍Filters","📈Business Insights","🛒About"])

# --- Dashboard Page ---
if menu == "🏠Dashboard":
    
    st.title("📦 Amazon Sales & Customer Behavior Analysis")
    st.subheader("📈 Dashboard Overview")

    c1, c2 = st.columns(2)

# ---------------- Small Graph 1 ----------------
    with c1:
        monthly = df.groupby(pd.to_datetime(df["OrderDate"]).dt.month)["TotalAmount"].sum()

        fig = px.area(
            x=monthly.index,
            y=monthly.values,
            labels={"x":"Month","y":"Sales"},
            color_discrete_sequence=["#FF9900"]
        )

        fig.update_layout(
            title="Monthly Sales Trend",
            template="plotly_dark",
            height=280,
            margin=dict(l=10,r=10,t=40,b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig, use_container_width=True)

# ---------------- Small Graph 2 ----------------
    with c2:

        cat = (
            df.groupby("Category")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
            .reset_index()
        )

        fig = px.bar(
            cat,
            x="Category",
            y="TotalAmount",
            color="TotalAmount",
            color_continuous_scale="Oranges"
        )

        fig.update_layout(
            title="Top Categories",
            template="plotly_dark",
            height=280,
            margin=dict(l=10,r=10,t=40,b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True)

    # ==================================================

    c3, c4 = st.columns(2)

# ---------------- Small Graph 3 ----------------
    with c3:

        pay = df["PaymentMethod"].value_counts().reset_index()
        pay.columns=["Payment","Count"]

        fig = px.pie(
            pay,
            values="Count",
            names="Payment",
            hole=0.60,
            color_discrete_sequence=px.colors.sequential.Oranges_r
        )

        fig.update_layout(
            title="Payment Methods",
            template="plotly_dark",
            height=280,
            margin=dict(l=10,r=10,t=40,b=10),
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig, use_container_width=True)

# ---------------- Small Graph 4 ----------------
    with c4:

        brand = (
            df.groupby("Brand")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
            .reset_index()
        )

        fig = px.funnel(
            brand,
            x="TotalAmount",
            y="Brand",
            color_discrete_sequence=["#FF9900"]
        )

        fig.update_layout(
            title="Top Brands",
            template="plotly_dark",
            height=280,
            margin=dict(l=10,r=10,t=40,b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
This dashboard provides an in-depth **Exploratory Data Analysis (EDA)** of Amazon sales data. 
It helps visualize key business metrics, including:
* **Sales Trends:** Tracking revenue patterns over daily, monthly, and yearly periods.
* **Product Performance:** Identifying top-selling vs low-performing categories.
* **Customer Behavior:** Analyzing purchasing choices and demographic distributions.
* **Pricing Insights:** Understanding the direct impact of ratings and discounts on overall demand.
""")
    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
                st.metric("💰 Total Sales", f"₹{df['TotalAmount'].sum():,.0f}")

    with c2:
                st.metric("📦 Orders", df.shape[0])

    with c3:
                st.metric("🛒 Products", df["ProductName"].nunique())

    # with c4:
    #             st.metric("⭐ Avg Rating", round(df["Rating"].mean(),2))

    st.markdown("""
<div style="
background: linear-gradient(135deg,#FF9900,#F7A100,#E47911);
padding:30px;
border-radius:20px;
box-shadow:0px 10px 25px rgba(255,153,0,0.45);
border:2px solid #FFD580;
margin-top:30px;
margin-bottom:20px;
text-align:center;
">

<h2 style="
color:#1A1A1A;
font-size:34px;
font-weight:700;
margin-bottom:12px;
font-family:Segoe UI;
">
📦 Amazon Sales & Customer Behavior Dashboard
</h2>

<p style="
color:#2B2B2B;
font-size:18px;
line-height:1.8;
margin-bottom:18px;
font-family:Segoe UI;
font-weight:500;
">
Professional Interactive Dashboard for analyzing Amazon Sales Performance,
Customer Buying Behavior, Product Trends, Revenue Insights and Business Intelligence.
</p>

<hr style="
border:0;
height:2px;
background:#FFFFFF;
margin:18px 0;
">

<p style="
color:#111111;
font-size:15px;
letter-spacing:1px;
margin:0;
font-weight:600;
">
📈 Sales Analytics &nbsp;&nbsp;|&nbsp;&nbsp;
👥 Customer Insights &nbsp;&nbsp;|&nbsp;&nbsp;
📦 Product Performance &nbsp;&nbsp;|&nbsp;&nbsp;
💰 Revenue Analysis &nbsp;&nbsp;|&nbsp;&nbsp;
📊 Business Intelligence
</p>

</div>
""", unsafe_allow_html=True)



        # ---------------- DATA CLEANING ----------------
elif menu == "🧹 Data Cleaning":
    st.subheader("📄 Original Dataset Information")

    # Dataset Info
    col1, col2 = st.columns(2)


    with col1:
        st.metric("Total Rows", df.shape[0])

    with col2:
        st.metric("Total Columns", df.shape[1])

    st.markdown("---")

    # Missing Values and Duplicate Records
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("🔍 Missing Values")
        missing = df.isnull().sum()
        st.dataframe(missing[missing > 0], use_container_width=True)

    with col4:
        st.subheader("🧹 Duplicate Records")
        duplicates = df.duplicated().sum()
        st.metric("Duplicate Rows", duplicates)

        st.markdown("---")

    # Data Cleaning
        st.subheader("🔧 Handling Missing Values")
        df = df.drop_duplicates()
        df = df.dropna()
        st.success("Missing values removed successfully")

        st.subheader("✏️ Column Name Cleaning")
        df.columns = df.columns.str.strip()
        st.success("Extra spaces removed from column names")

        if "Month" in df.columns:
            df["Month"] = pd.to_datetime(df["Month"], errors="coerce")
            st.success("Month column converted into date format")
                # # --- Data Sets Page ---
elif menu == "📂Data Sets":
    st.title("📂 Dataset Selection")
    
#     # Do alag files choose karne ke liye selectbox
    file_choice = st.sidebar.selectbox("Select File", ["amazon (3).csv", "Amazon_c.csv"])
        
    try:
        if file_choice == "amazon (3).csv":
            df = pd.read_csv("amazon (3).csv")
            st.write("Displaying amazon.csv")
        else:
            df = pd.read_csv("Amazon_c.csv")
            st.write("Displaying Amazon_c.csv")

        st.dataframe(df.head(10))

    except FileNotFoundError:
        st.error("File nahi mili!")

    except Exception as e:
        st.error(f"Error: {e}")



elif menu =="📊Graph Data":
    t1,t2=st.tabs(["Sales","coustmer behaviour"])

    
        # ---------------- FIRST TAB ----------------
    with t1:
         

    #         # Histogram
            fig, ax = plt.subplots(figsize=(10,5))
            ax.hist(df["Quantity"], bins=20, color="skyblue", edgecolor="black")
            ax.set_title("Quantity Distribution")
            ax.set_xlabel("Quantity")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
            

            # Top 10 Selling Products by Sales
            top_products = (
                df.groupby("ProductName", as_index=False)["TotalAmount"]
                .sum()
                .sort_values(by="TotalAmount", ascending=False)
                .head(10)
            )

            fig, ax = plt.subplots(figsize=(12,6))

            sns.barplot(
                data=top_products,
                x="TotalAmount",
                y="ProductName",
                palette="viridis",
                ax=ax
            )

            ax.set_title("Top 10 Selling Products by Sales", fontsize=16, fontweight="bold")
            ax.set_xlabel("Total Sales")
            ax.set_ylabel("Product Name")

            plt.tight_layout()
            st.pyplot(fig)

        
            

            status = df.groupby("OrderStatus",as_index=False)["TotalAmount"].sum()

            fig = px.funnel(
                status,
                x="TotalAmount",
                y="OrderStatus",
                title="Order Status Funnel"
            )
            st.plotly_chart(fig, use_container_width=True)

            # Monthly Sales Trend
            df["OrderDate"] = pd.to_datetime(df["OrderDate"])
            monthly = df.groupby(df["OrderDate"].dt.month)["TotalAmount"].sum()

            fig, ax = plt.subplots(figsize=(8,4))
            ax.plot(monthly.index, monthly.values, marker="o", linewidth=2)
            ax.set_title("Monthly Sales Trend")
            ax.set_xlabel("Month")
            ax.set_ylabel("Sales")
            ax.grid(True)
            st.pyplot(fig)

        

            # Category-wise Sales
            top = df.groupby("Category")["TotalAmount"].sum().sort_values(ascending=False)

            fig, ax = plt.subplots(figsize=(10,5))
            top.plot(kind="bar", ax=ax)
            ax.set_title("Category-wise Sales")
            ax.set_ylabel("Sales")
            plt.xticks(rotation=45)
            st.pyplot(fig)

            # Discount vs Sales
            fig, ax = plt.subplots(figsize=(10,5))
            ax.scatter(df["Discount"], df["TotalAmount"], alpha=0.5)
            ax.set_title("Discount vs Sales")
            ax.set_xlabel("Discount")
            ax.set_ylabel("Total Amount")
            st.pyplot(fig)


               
            # Radar Chart
            import numpy as np

            top6 = df1["Improvement_Areas"].value_counts().head(6)

            labels = top6.index.tolist()
            values = top6.values.tolist()

            values += values[:1]

            angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
            angles += angles[:1]

            fig = plt.figure(figsize=(5.5,5.5))
            ax = plt.subplot(111, polar=True)

            ax.fill(angles, values, color="deepskyblue", alpha=0.35)
            ax.plot(angles, values, color="crimson", linewidth=3, marker="o")

            colors = ["red", "orange", "gold", "limegreen", "blue", "purple"]

            colors = ["red", "orange", "gold", "limegreen", "blue", "purple"]

            for angle, value, color in zip(angles[:-1], values[:-1], colors):
                ax.scatter(angle, value, color=color, s=120)

            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(labels)

            plt.title("Top Improvement Areas")
            st.pyplot(fig)

    #     # ---------------- SECOND TAB ---------------
    with t2:


    # # Payment Methods Pie Chart
        fig, ax = plt.subplots(figsize=(3.5,3.5))

        df["PaymentMethod"].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90,
            colors=["skyblue", "lightgreen", "orange", "violet"],
            ax=ax
        )

        ax.set_title("Payment Methods")
        ax.set_ylabel("")

        st.pyplot(fig)

        # Gender Dot Plot
        gender = df1["Gender"].value_counts()

        fig, ax = plt.subplots(figsize=(6,4))

        for i, (label, count) in enumerate(gender.items()):
            ax.scatter(
                range(count),
                [i] * count,
                s=60
            )

        ax.set_yticks(range(len(gender)))
        ax.set_yticklabels(gender.index)
        ax.set_xlabel("Count")
        ax.set_title("Gender Distribution")

        st.pyplot(fig)

        # Recommendation Helpfulness
        fig, ax = plt.subplots(figsize=(10,4))

        df1["Recommendation_Helpfulness"].value_counts().plot(
            kind="bar",
            color="coral",
            ax=ax
        )

        ax.set_title("Recommendation Helpfulness")
        ax.set_xlabel("Response")
        ax.set_ylabel("Count")

        st.pyplot(fig)

        brand_sales = df.groupby("Brand", as_index=False)["TotalAmount"].sum()

        brand_sales = brand_sales.sort_values(
            by="TotalAmount",
            ascending=False
        ).head(10)

        fig = px.treemap(
            brand_sales,
            path=["Brand"],
            values="TotalAmount",
            color="TotalAmount",
            color_continuous_scale="Viridis",
            title="Top 10 Brands by Sales"
        )
        st.plotly_chart(fig, use_container_width=True)

    

        
        # Purchase Frequency Donut Chart
        purchase = df1["Purchase_Frequency"].value_counts()

        fig, ax = plt.subplots(figsize=(3,3))

        ax.pie(
            purchase.values,
            labels=purchase.index,
            autopct="%1.1f%%",
            wedgeprops=dict(width=0.4),
            startangle=90
        )

        ax.set_title("Purchase Frequency")

        st.pyplot(fig)

# import plotly.express as px
# import plotly.express as px
elif menu =="🛍️3D Visualization":

    sales = df.groupby("Category", as_index=False)[["Quantity","TotalAmount"]].sum()

    fig = px.scatter_3d(
                 sales,
                 x="Category",
                 y="Quantity",
                 z="TotalAmount",
                 color="Category",
                 size="TotalAmount"
             )

    st.plotly_chart(fig, use_container_width=True)
# 2
# import plotly.express as px
    fig = px.sunburst(
    df,
    path=["Category", "Brand"],
    values="TotalAmount",
    color="TotalAmount",
    color_continuous_scale="Viridis",
    title="Category and Brand Wise Sales Distribution")

    st.plotly_chart(fig, use_container_width=True)

# 3

# import plotly.express as px

    fig = px.sunburst(
    df,
    path=["Country", "State", "City"],
    values="TotalAmount",
    color="TotalAmount",
    color_continuous_scale="Plasma",
    title="Sales Distribution by Location")

    st.plotly_chart(fig, use_container_width=True)

elif menu == "🔍Filters":

    st.title("🔍 Data Filters")

    category = st.selectbox(
        "Select Category",
        ["All"] + sorted(df["Category"].dropna().unique().tolist())
    )

    brand = st.selectbox(
        "Select Brand",
        ["All"] + sorted(df["Brand"].dropna().unique().tolist())
    )

    country = st.selectbox(
        "Select Country",
        ["All"] + sorted(df["Country"].dropna().unique().tolist())
    )

    payment = st.selectbox(
        "Select Payment Method",
        ["All"] + sorted(df["PaymentMethod"].dropna().unique().tolist())
    )

    filtered_df = df.copy()

    if category != "All":
        filtered_df = filtered_df[filtered_df["Category"] == category]

    if brand != "All":
        filtered_df = filtered_df[filtered_df["Brand"] == brand]

    if country != "All":
        filtered_df = filtered_df[filtered_df["Country"] == country]

    if payment != "All":
        filtered_df = filtered_df[filtered_df["PaymentMethod"] == payment]

    st.success(f"Filtered Records: {len(filtered_df)}")

    st.dataframe(filtered_df, use_container_width=True)

elif menu == "📈Business Insights":

    st.title("📈 Business Insights")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Total Revenue", f"₹{df['TotalAmount'].sum():,.0f}")

    with col2:
        st.metric("📦 Total Orders", len(df))

    with col3:
        st.metric("🛒 Total Products", df["ProductName"].nunique())

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:
        top_category = (
            df.groupby("Category")["TotalAmount"]
            .sum()
            .idxmax()
        )
        st.success(f"🏆 Best Selling Category\n\n**{top_category}**")

        top_brand = (
            df.groupby("Brand")["TotalAmount"]
            .sum()
            .idxmax()
        )
        st.info(f"⭐ Top Brand\n\n**{top_brand}**")

        top_payment = df["PaymentMethod"].mode()[0]
        st.warning(f"💳 Most Used Payment Method\n\n**{top_payment}**")

    with c2:
        highest_city = (
            df.groupby("City")["TotalAmount"]
            .sum()
            .idxmax()
        )
        st.success(f"🏙️ Highest Sales City\n\n**{highest_city}**")

        top_customer = (
            df.groupby("CustomerName")["TotalAmount"]
            .sum()
            .idxmax()
        )
        st.info(f"👤 Top Customer\n\n**{top_customer}**")

        avg_order = df["TotalAmount"].mean()
        st.warning(f"🧾 Average Order Value\n\n₹ {avg_order:,.2f}")

    st.markdown("---")

    st.subheader("📌 Key Business Insights")

    st.markdown(f"""
✅ Total Revenue Generated: **₹{df['TotalAmount'].sum():,.0f}**

✅ **{top_category}** is the highest revenue-generating category.

✅ **{top_brand}** is the best-performing brand.

✅ Customers mostly prefer **{top_payment}** for payment.

✅ **{highest_city}** contributes the highest sales.

✅ Average Order Value is **₹{avg_order:,.2f}**.

✅ The dashboard helps identify customer buying behaviour, product performance, and revenue trends.
""")
      
elif menu == "🛒About":

    st.title("📘 About Project")

    st.header("1. Project Title")
    st.write("Amazon Sales Pattern and Customer Buying Behaviour Analysis Using Python")

    st.header("2. Project Introduction")
    st.write("""
    Online shopping has changed the way people purchase products. Every click, review,
    rating, and order creates valuable data. This project analyzes Amazon sales data
    to discover hidden patterns in customer purchasing behavior. By using Python for
    data analysis and visualization, the project converts raw sales data into meaningful
    business insights that help understand customer preferences, product performance,
    and market trends.
    """)

    st.header("3. Problem Statement")
    st.markdown("""
    - Best-selling products
    - Customer buying trends
    - Popular categories
    - Seasonal demand
    - Rating impact on sales
    - Discount effectiveness

    This project solves these problems through data-driven analysis.
    """)

    st.header("4. Project Objectives")
    st.markdown("""
    - Analyze Amazon sales data using Python
    - Identify top-performing product categories
    - Study customer buying behavior
    - Compare ratings with sales performance
    - Analyze pricing and discount trends
    - Build interactive visual dashboards
    - Generate useful business insights
    """)

    st.header("5. Technologies Used")
    st.markdown("""
    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Plotly
    - Streamlit
    - Jupyter Notebook
    """)
    
#     st.markdown("""
#     <hr>
#     <div style="
#     background:#232F3E;
#     padding:20px;
#     border-radius:12px;
#     text-align:center;
#     color:white;
#     margin-top:30px;">

#     <h3 style="color:#FF9900;">📦 Amazon Sales & Customer Behavior Analysis</h3>

#     <p>
#     Developed using <b>Python</b>, <b>Pandas</b>, <b>Matplotlib</b>,
#     <b>Seaborn</b> and <b>Streamlit</b>.
#     </p>

#     <p style="font-size:14px;">
#     © 2026 | Created by <b>Palak Sharma</b>
#     </p>

#     </div>
#     """, unsafe_allow_html=True)


#     st.markdown("""
#     <style>

#     /* Main Background */
#     .stApp{
#         background: linear-gradient(135deg,#E3F2FD,#FFF8E1,#F3E5F5);
#     }

#     /* Sidebar */
#     section[data-testid="stSidebar"]{
#         background: linear-gradient(180deg,#232F3E,#FF9900);
#     }

#     /* Sidebar Text */
#     section[data-testid="stSidebar"] *{
#         color:white;
#         font-weight:bold;
#     }

#     /* Buttons */
#     .stButton>button{
#         background:#FF9900;
#         color:white;
#         border-radius:12px;
#         border:none;
#         font-size:16px;
#         font-weight:bold;
#     }

#     .stButton>button:hover{
#         background:#232F3E;
#         color:white;
#     }

#     /* Tabs */
#     button[data-baseweb="tab"]{
#         background:#E3F2FD;
#         border-radius:10px;
#         margin-right:5px;
#         font-weight:bold;
#     }

#     button[data-baseweb="tab"][aria-selected="true"]{
#         background:#FF9900;
#         color:white;
#     }

#     /* DataFrame */
#     div[data-testid="stDataFrame"]{
#         border:3px solid #FF9900;
#         border-radius:10px;
#     }

#     /* Footer */
#     .footer{
#         margin-top:40px;
#         background:linear-gradient(to right,#232F3E,#FF9900);
#         color:white;
#         padding:18px;
#         border-radius:12px;
#         text-align:center;
#         font-size:17px;
#     }

#     </style>
#     """, unsafe_allow_html=True)

#     st.markdown("""
# <div class="footer">
# 📦 <b>Amazon Sales & Customer Behavior Analysis Dashboard</b><br>
# Developed using Python • Pandas • Matplotlib • Seaborn • Streamlit ❤️
# </div>
# """, unsafe_allo

import streamlit as st
import base64

st.set_page_config(page_title="Amazon Dashboard", layout="wide")

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("bg11.png")   # Apni image ka naam yahan likho

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)
