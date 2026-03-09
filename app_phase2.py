import streamlit as st
import time

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "session_expired" not in st.session_state:
    st.session_state.session_expired = False

query = st.query_params

# hanya restore login jika belum ada session aktif
if "auth" in query and not st.session_state.authenticated:
    st.session_state.authenticated = True
    st.session_state.login_time = time.time()
    
# Konfigurasi halaman
st.set_page_config(page_title="Shopper Category Insight", layout="wide")

# CSS untuk mereplikasi desain dashboard
st.markdown("""
<style>
    /* Background utama */
    .stApp {
        background-color: #ffffff;
    }

    /* Container Login */
    .login-container {
        max-width: 500px;
        margin: auto;
        padding-top: 3vh;
        text-align: center;
        font-family: 'Inter', sans-serif;
    }
    .block-container {
        max-width: 1200px !important;
        padding-top: 1rem !important;
    }

    .login-container {
        max-width: 520px;
    }

    /* Header Styling */
    .header-main {
        font-size: 48px;
        font-weight: 900;
        color: #1e293b;
        line-height: 0.9;
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    .header-accent {
        font-size: 48px;
        font-weight: 900;
        color: #991b1b; /* Deep Red Dashboard */
        line-height: 0.9;
        letter-spacing: -1px;
    }
    .header-sub {
        font-size: 15px;
        font-weight: 700;
        color: #1e293b;
        letter-spacing: 3px;
        margin-top: 15px;
        text-transform: uppercase;
    }

    /* Input Fields */
    div[data-baseweb="input"] {
        background-color: #f1f5f9 !important;
        border-radius: 18px !important;
        border: 1px solid transparent !important;
        padding: 8px !important;
        margin-bottom: 10px;
    }
    div[data-baseweb="input"]:focus-within {
        border: 1px solid #e2e8f0 !important;
    }

    /* Tombol Login (Deep Red dengan Glow) */
    div.stButton > button,
    div.stForm button {
        background-color: #800000 !important; /* Maroon/Deep Red */
        color: white !important;
        border: none !important;
        padding: 15px 45px !important;
        border-radius: 15px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        box-shadow: 0 10px 25px rgba(128, 0, 0, 0.3) !important;
        transition: all 0.3s ease !important;
        width: auto !important;
        display: block;
        margin-top: 20px;
    }

    /* Hover effect */
    div.stButton > button:hover,
    div.stForm button:hover {
        background-color: #991b1b !important;
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(128, 0, 0, 0.4) !important;
    }
    /* Hapus tombol di dalam field password */
    div[data-baseweb="input"] button {
        display: none !important;
    }

    /* Menghilangkan elemen default Streamlit */
    header {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


def login_page():

    SESSION_TIMEOUT = 600
    # cek apakah session masih valid
    if st.session_state.authenticated and st.session_state.login_time:
        elapsed = time.time() - st.session_state.login_time
        if elapsed > SESSION_TIMEOUT:
            st.session_state.session_expired = True
    # =========================
    # POPUP SESSION EXPIRED
    # =========================
    if st.session_state.session_expired:

        st.markdown("""
        <style>
        .session-popup{
            position:fixed;
            top:50%;
            left:50%;
            transform:translate(-50%,-50%);
            background:white;
            padding:40px 50px;
            border-radius:18px;
            box-shadow:0 25px 70px rgba(0,0,0,0.25);
            text-align:center;
            z-index:9999;
            font-family:'Inter', sans-serif;
        }

        /* Title */
        .session-title{
            font-size:28px;
            font-weight:900;
            color:#991b1b;
            letter-spacing:-0.5px;
            margin-bottom:8px;
        }

        /* Message */
        .session-text{
            font-size:15px;
            color:#334155;
            line-height:1.6;
        }
        </style>

        <div class="session-popup">
            <h3 style="color:#991b1b;margin-bottom:10px;">
            Session Expired
            </h3>
            <p>Your session has expired.<br>Please login again.</p>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(3)

        st.session_state.authenticated = False
        st.session_state.login_time = None
        st.session_state.session_expired = False

        st.query_params.clear()

        st.rerun()

    if not st.session_state.authenticated:

        st.markdown('<div class="login-container">', unsafe_allow_html=True)

        st.markdown("""
            <div class="header-main">SHOPPER CATEGORY</div>
            <div class="header-accent">INSIGHT</div>
            <div class="header-sub">DASHBOARD | TRIAL PHASE 2</div>
            <br><br>
        """, unsafe_allow_html=True)

        with st.form("login_form"):

            user = st.text_input(
                "Username",
                placeholder="Username",
                label_visibility="collapsed"
            )

            pw = st.text_input(
                "Password",
                type="password",
                placeholder="Password",
                label_visibility="collapsed"
            )

            login = st.form_submit_button("LOGIN")

            if login:
                if user == "SAT" and pw == "SAT234":

                    st.session_state.authenticated = True
                    st.session_state.login_time = time.time()

                    st.query_params["auth"] = "true"

                    st.rerun()

                else:
                    st.error("username atau password salah.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.stop()

# Jalankan Login
login_page()
st.markdown("""
<style>
/* Kecilkan lebar layout utama */
.block-container {
    max-width: 1400px;
    padding-top: 0.5rem;
}

/* ========================= */
/* FONT SCALING */
/* ========================= */

html, body, [class*="css"]  {
    font-size: 13px;
}

h1 { font-size: 26px; }
h2 { font-size: 20px; }
h3 { font-size: 16px; }

/* ========================= */
/* METRIC CARD COMPACT */
/* ========================= */

/* ========================= */
/* SIDEBAR TETAP NORMAL */
/* ========================= */

section[data-testid="stSidebar"] {
    width: 200px !important;
}

/* ========================= */
/* TAB COMPACT */
/* ========================= */

button[role="tab"] {
    padding: 6px 12px;
    border-radius: 10px;
}


</style>
""", unsafe_allow_html=True)

import pandas as pd
import numpy as np
import plotly.express as px
import os

pd.set_option("styler.render.max_elements", 1000000) 
st.set_page_config(layout="wide", page_title="SHOPPER INSIGHT", page_icon="📊")

# --- CUSTOM CSS (SIDEBAR, TABS, & AFFINITY DARK MODE) ---
# --- CUSTOM CSS (SIDEBAR, TABS, & AFFINITY DARK MODE) ---
st.markdown("""
    <style>
    /* 1. SIDEBAR BASE */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0;
        box-shadow: 10px 0px 70px rgba(0,0,0,0.08) !important;
    }

    /* Judul Sidebar Custom */
    .sidebar-title-custom {
        font-size: 25px !important; 
        
        font-weight: 800;
        color: #1E293B;
        line-height: 1.1;
        padding: 0px;
        
        /* SILAKAN UBAH ANGKA DI BAWAH INI UNTUK JARAK KE MENU */
        margin-bottom: 50px !important; 
    }

    /* Footer agar menempel di lantai sidebar */
    .sidebar-footer-fixed {
        position: fixed;
        bottom: 10px;
        width: 100%;
        color: #94A3B8 !important;
        font-size: 20px;
        background-color: transparent;
    }

    /* 4. TOMBOL NAVIGASI 3D */
    div[data-testid="stSidebar"] .stRadio label {
        background-color: #F8FAFC !important;
        border-radius: 14px !important;
        padding: 12px 20px !important;
        border: 1px solid #EDF2F7 !important;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }

    /* Efek Aktif Merah */
    div[data-testid="stSidebar"] .stRadio div[data-checked="true"] label {
        background: linear-gradient(135deg, #FF0000 0%, #CC0000 100%) !important;
        color: white !important;
        box-shadow: 0 10px 15px rgba(255, 0, 0, 0.2) !important;
    }

    /* Sembunyikan bullet point radio */
    div[data-testid="stSidebar"] .stRadio [data-testid="stWidgetLabel"] {
        display: none;
    }
    /* 4. FILTER STYLING (DIUBAH AGAR SERAGAM DENGAN TAB) */
    
    /* Wadah utama Selectbox & Multiselect */
    div[data-baseweb="select"] > div {
        background-color: #F0F2F6 !important; 
        border-radius: 12px !important;
        border: 1px solid #DFE1E5 !important;
        padding: 2px 5px !important;
        transition: all 0.2s ease;
    }

    /* Saat Filter di-klik (Focus) */
    div[data-baseweb="select"]:focus-within > div {
        border-color: #FF0000 !important; /* Warna border merah saat aktif */
        box-shadow: 0 0 0 1px #FF0000 !important;
        background-color: #FFFFFF !important;
    }

    /* Styling Tag/Pilihan di Multiselect (Dibuat seperti Tab Aktif) */
    span[data-baseweb="tag"] {
        background-color: #FFFFFF !important;
        border-radius: 8px !important;
        border: 1px solid #DDD !important;
        color: #333 !important;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
        font-weight: 500 !important;
    }

    /* Tombol X (Hapus) pada Tag */
    span[data-baseweb="tag"] div[role="button"] {
        color: #FF0000 !important;
    }

    /* Menghilangkan garis bawah default pada input filter */
    div[data-baseweb="select"] input {
        color: #000000 !important;
    }
    /* 5. TAB STYLING (MODERN SEGMENTED DENGAN SEKAT) */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #F0F2F6 !important; 
        border-radius: 10px;
        padding: 6px;
        gap: 0px; /* Gap dinolkan agar sekat terlihat menyambung */
        border: 1px solid #DFE1E5;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }

    .stTabs [data-baseweb="tab"] {
        height: 22px;
        background-color: transparent !important;
        border-radius: 0px !important; /* Kotak agar sekat konsisten */
        border: none !important;
        border-right: 1px solid #D1D5DB !important; /* INI SEKATNYA */
        color: #4B5563 !important;
        font-weight: 500;
        padding: 0px 20px !important;
        transition: all 0.2s;
    }

    /* Hilangkan sekat pada tab terakhir */
    .stTabs [data-baseweb="tab"]:last-child {
        border-right: none !important;
    }

    /* Styling Tab yang Aktif (Putih & Timbul) */
    .stTabs [aria-selected="true"] {
        background-color: #FFFFFF !important; 
        color: #FF0000 !important; 
        border-radius: 8px !important; /* Tab aktif dibuat melengkung sendiri */
        border-right: none !important; /* Hilangkan sekat saat tab aktif */
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        transform: scale(1.02);
    }

    /* Hilangkan sekat untuk tab tepat sebelum tab yang aktif agar tidak double */
    .stTabs [data-baseweb="tab"]:has(+ [aria-selected="true"]) {
        border-right: none !important;
    }

    /* Menghilangkan garis bawah default Streamlit */
    .stTabs [data-baseweb="tab-highlight"] {
        display: none !important;
    }
    /* 1. MENGECILKAN KONTAINER KARTU */
    [data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #f0f2f6; /* Opsional: tambah border halus */
        padding: 10px !important;
        border-radius: 8px;
    }

    /* 2. MENGECILKAN LABEL (Judul di atas angka, misal: 'Spend Per Buyer') */
    [data-testid="stMetricLabel"] {
        font-size: 0.75rem !important;
        font-weight: 500 !important;
        color: #64748b !important;
    }

    /* 3. MENGECILKAN ANGKA UTAMA (Misal: 'Rp 22,663') */
    [data-testid="stMetricValue"] {
        font-size: 1.2rem !important; /* Perkecil angka agar tidak makan tempat */
        font-weight: 700 !important;
    }

    /* 4. MENGECILKAN ANGKA PERTUMBUHAN/DELTA (Misal: '-0.59%') */
    [data-testid="stMetricDelta"] {
        font-size: 0.7rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. DATA LOADERS ---
@st.cache_data
def load_perf_file(level, versi):
    filename = f"perf_{level}_phase2_{versi.lower()}.csv"
    if os.path.exists(filename):
        df = pd.read_csv(filename)

        # 🔧 SAMAKAN NAMA KOLOM PENETRATION
        rename_map = {
            "PENETRATION_BEFORE": "TRANSACTION_PENETRATION_BEFORE",
            "PENETRATION_AFTER": "TRANSACTION_PENETRATION_AFTER",
            "PENETRATION_GROWTH": "TRANSACTION_PENETRATION_GROWTH"
        }

        df = df.rename(columns=rename_map)

        return df

    return pd.DataFrame()

@st.cache_data
def load_segment_unified():
    if os.path.exists("perf_segmentation_unified.csv"):
        return pd.read_csv("perf_segmentation_unified.csv")
    return pd.DataFrame()

@st.cache_data
def load_loyalty_data():
    try:
        import pandas as pd

        return {
            "br_loy_cat": pd.read_csv("BRAND_LOYALTY_CATEGORY_PHASE2.csv"),
            "br_loy_sub": pd.read_csv("BRAND_LOYALTY_SUBCATEGORY_PHASE2.csv"),
            "br_swi_cat": pd.read_csv("BRAND_SWITCH_CATEGORY_PHASE2.csv"),
            "br_swi_sub": pd.read_csv("BRAND_SWITCH_SUBCATEGORY_PHASE2.csv"),
            "cat_loy": pd.read_csv("CATEGORY_LOYALTY_PHASE2.csv"),
            "sub_loy": pd.read_csv("SUBCATEGORY_LOYALTY_PHASE2.csv")
        }

    except Exception as e:
        st.error(f"Gagal load data loyalty: {e}")
        return {}

@st.cache_data
def load_affinity_data():

    data = {}

    try:
        # ===============================
        # CATEGORY & SUBCATEGORY (NORMAL)
        # ===============================
        data["cat"] = pd.read_csv("AFFINITY_CAT_PHASE2.csv", sep=None, engine="python")
        data["subcat"] = pd.read_csv("AFFINITY_SUBCAT_PHASE2.csv", sep=None, engine="python")

        # ===============================
        # BRAND CAT (SPLIT FILE)
        # ===============================
        brand_cat_files = [
            "AFFINITY_BRAND_CAT_PHASE2_part0.csv",
            "AFFINITY_BRAND_CAT_PHASE2_part1.csv"
        ]

        brand_cat_list = []
        for f in brand_cat_files:
            if os.path.exists(f):
                brand_cat_list.append(pd.read_csv(f, sep=None, engine="python"))

        if brand_cat_list:
            data["brand_cat"] = pd.concat(brand_cat_list, ignore_index=True)
        else:
            data["brand_cat"] = pd.DataFrame()

        data["brand_sub"] = pd.read_csv("AFFINITY_BRAND_SUBCAT_PHASE2.csv", sep=None, engine="python")

        if os.path.exists("AFFINITY_BRAND_SAME_CAT_PHASE2.csv"):
            data["same_brand_cat"] = pd.read_csv(
                "AFFINITY_BRAND_SAME_CAT_PHASE2.csv",
                sep=None,
                engine="python"
            )
        else:
            data["same_brand_cat"] = pd.DataFrame()

        if os.path.exists("AFFINITY_BRAND_SAME_SUBCAT_PHASE2.csv"):
            data["same_brand_subcat"] = pd.read_csv(
                "AFFINITY_BRAND_SAME_SUBCAT_PHASE2.csv",
                sep=None,
                engine="python"
            )
        else:
            data["same_brand_subcat"] = pd.DataFrame()

    except Exception as e:
        st.error(f"Gagal load affinity data: {e}")
        return {}

    return data


# --- 2. DISPLAY HELPERS ---
import matplotlib.colors as mcolors

def render_performance_cards(df, is_category=False):
    """Versi Uniform & Clean: Ukuran diperbesar, teks div bocor dihapus"""
    if df.empty:
        return

    # Hitung rata-rata metrik
    metrics = {
        "freq_val": df["PURCHASE_FREQUENCY_AFTER"].mean() if "PURCHASE_FREQUENCY_AFTER" in df.columns else 0,
        "freq_gr": df["PURCHASE_FREQUENCY_GROWTH"].mean() if "PURCHASE_FREQUENCY_GROWTH" in df.columns else 0,
        "spb_val": df["SPB_AFTER"].mean() if "SPB_AFTER" in df.columns else 0,
        "spb_gr": df["SPB_GROWTH"].mean() if "SPB_GROWTH" in df.columns else 0,
        "spt_val": df["SPT_AFTER"].mean() if "SPT_AFTER" in df.columns else 0,
        "spt_gr": df["SPT_GROWTH"].mean() if "SPT_GROWTH" in df.columns else 0,
    }
    
    if is_category:

        metrics["pen_val"] = (
            df["TRANSACTION_PENETRATION_AFTER"].mean()
            if "TRANSACTION_PENETRATION_AFTER" in df.columns else 0
        )

        metrics["pen_gr"] = (
            df["TRANSACTION_PENETRATION_GROWTH"].mean()
            if "TRANSACTION_PENETRATION_GROWTH" in df.columns else 0
        )

        metrics["buyer_total"] = (
            df["BUYER_COUNT_AFTER"].sum()
            if "BUYER_COUNT_AFTER" in df.columns else 0
        )

    def get_delta_html(val):
        color = "#E8F5E9" if val > 0 else "#FFEBEE"
        t_color = "#2E7D32" if val > 0 else "#C62828"
        icon = "↑" if val > 0 else "↓"
        return f"""<div style="display:inline-block; background-color:{color}; color:{t_color}; 
                    padding:2px 10px; border-radius:12px; font-size:9px; font-weight:bold; margin-top:0px;">
                    {icon} {val:+.2%}</div>"""

    card_style = """
        background-color: #F8F9FA; 
        border-radius: 8px; 
        padding: 12px 14px; 
        height: 105px; 
        border: 1px solid #EEE;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    """

    cols = st.columns(4 if is_category else 3)

    # ==============================
    # 1. CATEGORY PENETRATION
    # ==============================
    if is_category:
        with cols[0]:

            gr = metrics['pen_gr']
            border_color = "#AEE3B2" if gr > 0 else "#E1B7B3"

            st.markdown(f"""
                <div style="{card_style}; border-bottom:2px solid {border_color};">
                    <p style="color:#6B7280; font-size:12px; margin:0; font-weight:600;">
                        Transaction Penetration
                    </p>
                    <div style="font-size:25px; font-weight:700; margin-top:0px;">
                        {metrics['pen_val']:.2%}
                    </div>
                    {get_delta_html(gr)}
                    <p style="color:#9CA3AF; font-size:8px; margin-top:0px;">
                        Total Buyers: {metrics['buyer_total']:,}
                    </p>
                </div>
            """, unsafe_allow_html=True)

    # ==============================
    # 2. OTHER METRICS
    # ==============================
    idx_start = 1 if is_category else 0

    m_list = [
        ("Purchase Frequency", metrics['freq_val'], metrics['freq_gr'], "{:.2f}"),
        ("Spend Per Buyer", metrics['spb_val'], metrics['spb_gr'], "Rp {:,.0f}"),
        ("Spend Per Trip", metrics['spt_val'], metrics['spt_gr'], "Rp {:,.0f}")
    ]

    for i, (label, val, gr, fmt) in enumerate(m_list):

        # warna border mengikuti growth
        border_color = "#AEE3B2" if gr > 0 else "#E1B7B3"

        with cols[idx_start + i]:
            st.markdown(f"""
                <div style="{card_style}; border-bottom:4px solid {border_color};">
                    <p style="color:#6B7280; font-size:12px; margin:0; font-weight:600;">
                        {label}
                    </p>
                    <div style="font-size:25px; font-weight:700; margin-top:0px;">
                        {fmt.format(val)}
                    </div>
                    {get_delta_html(gr)}
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

# ===============================================================
# GLOBAL HELPERS (Sesuai Kolom Baru)
# ===============================================================

def display_styled_table(df):
    if df.empty:
        st.warning("DATA TIDAK TERSEDIA")
        return

    # 1. Bersihkan data (Copy agar tidak merusak dataframe asli)
    df = df.copy()

# 🔥 FIX: hapus duplicate column name (penyebab pd.to_numeric error)
    df = df.loc[:, ~df.columns.duplicated()]

    # Bersihkan kolom yang tidak perlu agar tampilan rapi
    cols_to_drop = [c for c in df.columns if "PROMO_PCT" in c]
    df = df.drop(columns=cols_to_drop, errors='ignore')
    first_col = df.columns[0]
    second_col = df.columns[1]

    # Gunakan 2 kolom supaya index unik
    df = df.set_index([first_col, second_col])

    df.index.names = [first_col, second_col]
    # 2. Identifikasi kolom Growth secara dinamis dan pastikan ada di DF
    # Kita hanya mengambil kolom yang BENAR-BENAR ada di df.columns
    growth_cols = [c for c in df.columns if "GROWTH" in c]

    # Pastikan tipe data numerik untuk kolom growth agar tidak error saat diwarnai
    for col in growth_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 3. Logika pewarnaan
    def apply_growth_color(val):
        if pd.isna(val) or val == 0:
            return None # Jangan beri style jika kosong
        if val > 0:
            return 'background-color: #d4edda; color: #155724;'
        if val < 0:
            return 'background-color: #f8d7da; color: #721c24;'
        return None

    # 4. Dictionary Formatting
    format_dict = {}
    for col in df.columns:
        if "GROWTH" in col or "PENETRATION" in col:
            format_dict[col] = "{:.2%}"
        elif any(x in col for x in ["SPT", "SPB", "SALES_VALUE"]):
            format_dict[col] = "Rp {:,.0f}"
        elif any(x in col for x in ["AVG", "FREQUENCY", "QTY"]):
            format_dict[col] = "{:,.2f}"

    # 5. Terapkan styling dengan proteksi KeyError
    styled_df = df.style.format(format_dict, na_rep="-")

    if growth_cols:
        styled_df = styled_df.map(apply_growth_color, subset=growth_cols)

    # Tampilkan di Streamlit
    st.dataframe(
        styled_df,
        use_container_width=True, 
        hide_index=False
    )
    
    st.caption("ℹ️ Keterangan Tabel = **SPT** (Spend Per Trip) | **SPB** (Spend Per Buyer)")
   
# ===============================================================
# 1. FUNGSI HELPER GLOBAL (WAJIB DI ATAS AGAR TIDAK ERROR)
# ===============================================================

def apply_global_perf(df, sel_sec):
    """Fungsi filter section yang dipanggil di semua tab"""
    if df.empty: return df
    # Cek kolom SECTION (case sensitive)
    s_col = next((c for c in ["SECTION", "section"] if c in df.columns), None)
    if sel_sec and sel_sec != "ALL" and s_col:
        df = df[df[s_col] == sel_sec]
    return df.reset_index(drop=True)

def reorder_final(df, level):
    """Mengatur urutan kolom: Identity -> Metrics Utama -> Sisanya"""
    if df.empty: return df
    cols = df.columns.tolist()
    
    # 1. Tentukan Kolom Identitas Berdasarkan Level
    if level == "category": 
        # Cek jika ini dari tab segmentasi (punya SEGMENT_VALUE)
        if "SEGMENT_VALUE" in cols:
            id_cols = ["SEGMENT_VALUE", "CATEGORY", "SECTION"]
        else:
            id_cols = ["CATEGORY", "SECTION"] 
    elif level == "subcategory": 
        id_cols = ["SUBCATEGORY", "CATEGORY", "SECTION"]
    elif level == "brand": 
        id_cols = ["BRAND", "SUBCATEGORY", "CATEGORY", "SECTION"]
    elif level == "plu":
        id_cols = ["PLU", "DESCP", "CATEGORY", "SECTION"]
    else: 
        id_cols = ["CATEGORY", "SECTION"]

    # 2. Susun Urutan Metrik Secara Baku (Strict Order)
    metric_order = [
        "AVG_QTY_STRUK_MONTH_BEFORE", "AVG_QTY_STRUK_MONTH_AFTER", "AVG_QTY_STRUK_MONTH_GROWTH",
        "AVG_STRUK_MONTH_BEFORE", "AVG_STRUK_MONTH_AFTER", "AVG_STRUK_MONTH_GROWTH",
        "TRANSACTION_PENETRATION_BEFORE", "TRANSACTION_PENETRATION_AFTER", "TRANSACTION_PENETRATION_GROWTH",
        "SPT_BEFORE", "SPT_AFTER", "SPT_GROWTH",
        "SPB_BEFORE", "SPB_AFTER", "SPB_GROWTH"
    ]

    # Tambahkan Penetration HANYA untuk level category  
    if level == "category":
        metric_order += [
            # versi baru
            "TRANSACTION_PENETRATION_BEFORE",
            "TRANSACTION_PENETRATION_AFTER",
            "TRANSACTION_PENETRATION_GROWTH",
            
            # fallback versi lama
            "PENETRATION_BEFORE",
            "PENETRATION_AFTER",
            "PENETRATION_GROWTH"
        ]
    
    # 3. Filter kolom yang benar-benar ada di dalam dataset agar tidak error
    existing_ids = [c for c in id_cols if c in cols]
    existing_metrics = [c for c in metric_order if c in cols]
    others = [c for c in cols if c not in existing_ids and c not in existing_metrics]
    
    # Gabungkan semua dengan urutan yang sudah dipatenkan
    return df[existing_ids + existing_metrics + others]
df_p = pd.DataFrame()

def render_affinity_tab(df, col_a, col_b, filter_cols, key_prefix, show_qty_impact=True, show_top10=True, extra_display_cols=[]):
    """
    Fungsi render yang fleksibel untuk menampilkan Matrix Affinity 
    dan Tabel QTY Impact dengan kolom tambahan.
    """
    global df_p 

    if df.empty:
        st.warning("***[Affinity Tidak Tersedia] : Filter Kembali Section atau Versi Plano***")
        return

    df = df.copy()
    df.columns = [c.lower() for c in df.columns]
    col_a, col_b = col_a.lower(), col_b.lower()
    filter_cols = [f.lower() for f in filter_cols]
    extra_display_cols = [c.lower() for c in extra_display_cols]
    
    df[col_a] = df[col_a].astype(str)
    df[col_b] = df[col_b].astype(str)
    
    numeric_cols = ['trans_ab', 'trans_a', 'trans_b', 'qty_ab', 'avg_qty_b_when_pair']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    epsilon = 1e-9
    total_trans = None
    if 'total_transactions' in df.columns:
        total_trans = df['total_transactions'].iloc[0]

    elif 'total_struk_global' in globals():
        total_trans = total_struk_global

    elif 'BUYER_COUNT_BEFORE' in df_p.columns:
        total_trans = df_p['BUYER_COUNT_BEFORE'].sum()

    if not total_trans or total_trans <= 0:
        total_trans = df['trans_a'].max() if 'trans_a' in df.columns else 1

    if total_trans <= 0:
        st.error("Gagal menghitung populasi transaksi (Universe). Periksa sumber data Anda.")
        return
    
    df['measure_support'] = df['trans_ab'] / (total_trans + epsilon)
    df['measure_confidence'] = df['trans_ab'] / (df['trans_a'] + epsilon)
    supp_a = df['trans_a'] / (total_trans + epsilon)
    supp_b = df['trans_b'] / (total_trans + epsilon)
    df['measure_lift'] = df['measure_support'] / ((supp_a * supp_b) + epsilon)

    df['conf_norm'] = df['measure_confidence'].clip(0, 1)
    df['supp_norm'] = df['measure_support'].clip(0, 1)
    df['lift_norm'] = df['measure_lift'].apply(lambda x: (x-1)/4 if x > 1 else 0).clip(0, 1)
    df['weighted_score'] = (
        (df['supp_norm'] * 0.35) + 
        (df['conf_norm'] * 0.60) + 
        (df['lift_norm'] * 0.05)
    )

    # 6. QTY Impact Calculation
    if 'avg_qty_b_when_pair' in df.columns and df['avg_qty_b_when_pair'].sum() > 0:
        df['qty_impact'] = df['avg_qty_b_when_pair']
    else:
        df['qty_impact'] = np.where(df['trans_ab'] > 0, df['qty_ab'] / (df['trans_ab'] + epsilon), 0)

    # 7. Filter UI Dinamis
    base_df = df.copy()
    cols_ui = st.columns(len(filter_cols))
    sel_dict = {}

    for i, f_col in enumerate(filter_cols):
        with cols_ui[i]:
            if f_col in base_df.columns:
                unique_vals = sorted(base_df[f_col].dropna().unique())
                
                # Mengganti expander+checkbox menjadi st.multiselect layaknya menu Performance
                sel_vals = st.multiselect(f"{f_col.upper()}:", unique_vals, key=f"{key_prefix}_{f_col}")
                
                if sel_vals:
                    sel_dict[f_col] = sel_vals

    df_filtered = base_df.copy()
    for f_col, sel_vals in sel_dict.items():
        if sel_vals:
            df_filtered = df_filtered[df_filtered[f_col].isin(sel_vals)]

    if df_filtered.empty:
        st.warning("Data kosong setelah difilter.")
        return

    # 8. Render Matrix Table
    matrix_weighted = df_filtered.groupby([col_a, col_b])['weighted_score'].mean().unstack().fillna(0)
    
    colors_aff = ["#ffffff", "#84f884"] 
    cmap_aff = mcolors.LinearSegmentedColormap.from_list("soft_aff", colors_aff)

    st.dataframe(
        matrix_weighted.style.format("{:.2%}")
        .background_gradient(cmap=cmap_aff, axis=None, vmin=0, vmax=0.5) 
        .set_properties(**{
            'color': '#333333', 
            'border': '1px solid #F0F0F0',
            'font-size': '12px'
        }),
        use_container_width=True
    )
 
    # ========================================================
    if show_top10:

        st.markdown("<br>", unsafe_allow_html=True)
        st.write("**TOP 10 AFFINITY PAIRS**")
        st.info("Menampilkan 10 kombinasi pasangan dengan skor Affinity tertinggi")
        
        top_10_df = df_filtered.groupby([col_a, col_b])['weighted_score'].mean().reset_index()
        top_10_df = top_10_df.sort_values(by='weighted_score', ascending=False).head(10)
        
        top_10_display = top_10_df.copy()
        top_10_display.columns = [col_a.upper(), col_b.upper(), 'AFFINITY SCORE']
        
        st.dataframe(
            top_10_display.style.format({'AFFINITY SCORE': '{:.2%}'})
            .set_properties(**{
                'background-color': 'transparent', 
                'color': '#333333', 
                'border': '1px solid #EEEEEE',
                'font-size': '12px',
                'font-weight': '500'
            }),
            use_container_width=True,
            hide_index=True
        )

    # ========================================================
    # 9. RENDER QTY IMPACT (PERUBAHAN 2: MENGHAPUS DUPLIKAT)
    # ========================================================
    if show_qty_impact:
        st.markdown("---")
        st.write("### 🛒 QTY IMPACT")
        st.info("Rata-rata QTY produk B yang dibeli user saat bersamaan membeli produk A")

        display_cols = [col_a, col_b] + extra_display_cols + ['qty_impact']
        available_cols = [c for c in display_cols if c in df_filtered.columns]
        
        # MENGHAPUS DUPLIKAT: Kita gunakan drop_duplicates berdasarkan pasangan produk A dan B
        # sehingga tidak ada lagi data yang tampil double.
        df_qty_table = df_filtered[available_cols].drop_duplicates(subset=[col_a, col_b]).sort_values(by="qty_impact", ascending=False)

        st.dataframe(
            df_qty_table.style.format({"qty_impact": "{:.2f}"})
            .set_properties(**{
                'background-color': 'transparent', 
                'color': '#333333', 
                'border': '1px solid #EEEEEE',
                'font-size': '12px'
            }),
            use_container_width=True,
            hide_index=True
        )

def render_plano_matrix(df):
    if df.empty: return
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### 📊 Ringkasan Matrix Perbandingan Plano")
    
    # Menyiapkan data untuk Pivot (V1 vs V2)
    # Pastikan kolom 'VERSI' dan 'SECTION' ada di data kamu
    try:
        # Kita ambil rata-rata pertumbuhan atau total sales sebagai nilai matrix
        val_col = 'SALES_VALUE' if 'SALES_VALUE' in df.columns else df.select_dtypes(include=[np.number]).columns[0]
        
        pivot_df = df.pivot_table(
            index='SECTION', 
            columns='VERSI', 
            values=val_col, 
            aggfunc='mean'
        ).round(2)
        
        # Tampilkan Matrix dengan Desain Premium
        st.dataframe(
            pivot_df.style.background_gradient(cmap='Reds', axis=1)
            .format("{:,.2f}"),
            use_container_width=True
        )
        st.caption(f"*) Data di atas adalah perbandingan rata-rata {val_col} antara Versi Plano.")
    except Exception as e:
        st.info("Matrix perbandingan tidak tersedia untuk level detail ini.")
def render_static_affinity_matrix():
    try:
        # 1. Ambil data affinity yang sudah di-load di awal
        aff = load_affinity_data()

        if not aff or aff["cat"].empty or aff["subcat"].empty:
            st.warning("Data Affinity tidak ditemukan atau file rusak.")
            return
        
        # 2. Gabungkan data Category & Subcategory untuk mendapatkan mapping varian lengkap
        df_map = pd.concat([aff["cat"], aff["subcat"]], ignore_index=True)
        df_map.columns = [c.upper() for c in df_map.columns] # Paksa ke UPPERCASE agar konsisten
        
        # 3. Proses Pivot: Baris = SECTION, Kolom = PLANO_GROUP_FINAL, Isi = KD_VARIANT
        df_pivoted = df_map.pivot_table(
            index='SECTION', 
            columns='PLANO_GROUP_FINAL', 
            values='KD_VARIANT',
            aggfunc=lambda x: ', '.join(x.astype(str).unique())
        ).reset_index().fillna("-")
        
        # 4. Ambil HANYA 3 kolom sesuai permintaan Anda
        cols_to_keep = ['SECTION', 'AFTER_V1', 'AFTER_V2']
        df_display = df_pivoted[[c for c in cols_to_keep if c in df_pivoted.columns]].copy()
        
        # 5. Rename kolom agar sesuai dengan keinginan Anda
        df_display.columns = ['SECTION', 'VERSI PLANO V1', 'VERSI PLANO V2']
        
        # 6. Tampilkan Tabel Statis (Desain disamakan dengan Affinity)
        st.markdown("---")
        with st.expander("📋 MATRIKS VARIAN BY VERSI PLANO (Reference)", expanded=False):
            st.dataframe(
                df_display.style.set_properties(**{
                    'background-color': 'transparent',
                    'color': '#333333',
                    'border': '1px solid #F5F5F5',
                    'font-size': '12px',
                    'text-align': 'left'
                }),
                use_container_width=True,
                hide_index=True # Menghilangkan angka indeks 0, 1, 2 di kiri
            )
        
    except Exception as e:
        st.info(f"Matriks varian belum tersedia: {e}")

def render_switching_cards(total_sw, total_no, top_dest_name, top_dest_pct):
    """Render 3 KPI Cards for Switching Menu (English)"""
    total = total_sw + total_no
    if total == 0: return

    pct_sw = total_sw / total
    pct_no = total_no / total

    card_style = """
        background-color: #F8F9FA; 
        border-radius: 8px; 
        padding: 15px; 
        min-height: 100px; 
        border: 1px solid #EEE;
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: relative;
        overflow: hidden;
    """

    cols = st.columns(3) # Dibagi rata menjadi 3 kolom
    
    with cols[0]:
        st.markdown(f"""
            <div style="{card_style}; border-bottom: 4px solid #E1B7B3;">
                <p style="color:#666; font-size:11px; margin:0; font-weight:600; text-transform:uppercase;">Switch Rate</p>
                <div style="font-size:26px; font-weight:800; color:#1E293B; line-height:1.2;">{pct_sw:.2%}</div>
                <p style="color:#888; font-size:11px; margin:0;">Total: {total_sw:,} Buyers</p>
            </div>
        """, unsafe_allow_html=True)
        
    with cols[1]:
        st.markdown(f"""
            <div style="{card_style}; border-bottom: 4px solid #AEE3B2;">
                <p style="color:#666; font-size:11px; margin:0; font-weight:600; text-transform:uppercase;">Retention Rate (No Switch)</p>
                <div style="font-size:26px; font-weight:800; color:#1E293B; line-height:1.2;">{pct_no:.2%}</div>
                <p style="color:#888; font-size:11px; margin:0;">Total: {total_no:,} Buyers</p>
            </div>
        """, unsafe_allow_html=True)

    with cols[2]:
        st.markdown(f"""
            <div style="{card_style}; border-bottom: 4px solid #3498DB;">
                <p style="color:#666; font-size:11px; margin:0; font-weight:600; text-transform:uppercase;">Top Destination</p>
                <div style="font-size:26px; font-weight:800; color:#1E293B; line-height:1.2; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{top_dest_name}">{top_dest_name}</div>
                <p style="color:#888; font-size:11px; margin:0;">Share: {top_dest_pct:.2%} of Switchers</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

def render_category_promo_driven(df):
    """
    Menampilkan kategori yang pembeliannya didominasi promo vs non promo
    Aman walaupun kolom belum ada (tidak crash)
    """

    if df.empty:
        return

    # VALIDASI KOLOM
    required_cols = {"PROMO_BUYER_AFTER", "NON_PROMO_BUYER_AFTER", "CATEGORY"}
    if not required_cols.issubset(df.columns):
        return

    # Hitung share
    temp = df.copy()

    temp["TOTAL_BUYER"] = (
        temp["PROMO_BUYER_AFTER"].fillna(0)
        + temp["NON_PROMO_BUYER_AFTER"].fillna(0)
    )

    # Hindari pembagian nol
    temp = temp[temp["TOTAL_BUYER"] > 0]

    temp["PROMO_SHARE"] = temp["PROMO_BUYER_AFTER"] / temp["TOTAL_BUYER"]
    temp["NON_PROMO_SHARE"] = temp["NON_PROMO_BUYER_AFTER"] / temp["TOTAL_BUYER"]

    # Urutkan kategori paling promo-driven
    temp = temp.sort_values("PROMO_SHARE", ascending=False)

    st.markdown("### 🚀 CATEGORY PROMO DRIVEN")

    st.dataframe(
        temp[
            [
                "CATEGORY",
                "PROMO_BUYER_AFTER",
                "NON_PROMO_BUYER_AFTER",
                "PROMO_SHARE",
                "NON_PROMO_SHARE",
            ]
        ]
        .style.format(
            {
                "PROMO_SHARE": "{:.1%}",
                "NON_PROMO_SHARE": "{:.1%}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )
def render_category_promo_share_chart(df):
    """
    Promo vs Non Promo (Average BEFORE & AFTER)
    1 chart saja per category
    """

    if df.empty:
        return

    required_cols = {
        "CATEGORY",
        "PROMO_SHARE_BEFORE",
        "PROMO_SHARE_AFTER",
        "NON_PROMO_SHARE_BEFORE",
        "NON_PROMO_SHARE_AFTER"
    }

    if not required_cols.issubset(df.columns):
        st.info("Promo share belum tersedia di dataset.")
        return

    import plotly.express as px

    st.markdown("------")
    st.markdown("### CATEGORY PROMO DRIVEN ")
    st.caption("Distribusi share pembelian karena promo vs non-promo per kategori")

    temp = df.copy()

    # ==============================
    # AVERAGE BEFORE & AFTER
    # ==============================
    temp["PROMO_FINAL"] = (
        temp["PROMO_SHARE_BEFORE"].fillna(0)
        + temp["PROMO_SHARE_AFTER"].fillna(0)
    ) / 2

    temp["NON_PROMO_FINAL"] = (
        temp["NON_PROMO_SHARE_BEFORE"].fillna(0)
        + temp["NON_PROMO_SHARE_AFTER"].fillna(0)
    ) / 2

    # ==============================
    # Reshape
    # ==============================
    chart_df = temp.melt(
        id_vars="CATEGORY",
        value_vars=["PROMO_FINAL", "NON_PROMO_FINAL"],
        var_name="TYPE",
        value_name="SHARE"
    )

    chart_df["TYPE"] = chart_df["TYPE"].map({
        "PROMO_FINAL": "PROMO",
        "NON_PROMO_FINAL": "NON PROMO"
    })

    # ==============================
    # Vertical 100% Stacked
    # ==============================
    fig = px.bar(
        chart_df,
        x="CATEGORY",
        y="SHARE",
        color="TYPE",
        barmode="stack",
        text=chart_df["SHARE"].apply(lambda x: f"{x:.0%}"),
        color_discrete_map={
            "PROMO": "#1F3A5F",       # Green executive
            "NON PROMO": "#94A3B8"    # Soft gray
        }
    )

    fig.update_layout(
        yaxis_tickformat=".0%",
        height=550,
        legend_title="",
        xaxis_title="",
        yaxis_title="Percentage",
        xaxis_tickangle=-45,
        bargap=0.15,
        template="plotly_white"
    )

    fig.update_traces(
        textposition="inside",
        insidetextfont=dict(color="white", size=12),
        marker_line_width=1,
        marker_line_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)
    
def normalize_brand_columns(df):
    """
    Auto-detect dan mapping kolom brand menjadi brand_a & brand_b
    Tahan terhadap berbagai variasi nama kolom:
    brand a, brand_before, brand-A, brand1, dll
    """
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()

    # Ambil semua kolom yang mengandung kata 'brand'
    brand_cols = [c for c in df.columns if "brand" in c]

    # Jika minimal ada 2 kolom brand → mapping otomatis
    if len(brand_cols) >= 2:
        df = df.rename(columns={
            brand_cols[0]: "brand_a",
            brand_cols[1]: "brand_b"
        })
    else:
        st.error(f"Kolom brand tidak cukup ditemukan! Kolom tersedia: {df.columns.tolist()}")
        st.stop()

    # Validasi final
    required_cols = {"brand_a", "brand_b"}
    if not required_cols.issubset(df.columns):
        st.error(f"Kolom brand_a & brand_b gagal dibentuk! Kolom tersedia: {df.columns.tolist()}")
        st.stop()

    return df

def main():
    global df_p 
    # 🔥 Ambil section dari semua versi plano
    section_set = set()

    for v in ["V1", "V2", "NOT_TRIAL"]:
        df_tmp = load_perf_file("category", v)
        if not df_tmp.empty and "SECTION" in df_tmp.columns:
            section_set.update(df_tmp["SECTION"].dropna().unique())

    sections_only = sorted(list(section_set))

    # 🔥 Hapus section tidak valid
    sections_only = [s for s in sections_only if s not in ["UNKNOWN", "-", "NAN", "NONE", ""]]

    start_idx = 0

    st.sidebar.markdown("""
    <p class="sidebar-title-custom">
        SHOPPER<br>
        CATEGORY<br>
        INSIGHT
        <br>
        <span style="
            font-size:14px;
            font-weight:500;
            color:#000000;
            letter-spacing:1px;
        ">
            PHASE 2
        </span>
    </p>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    # 2. MENU: Beri sedikit keterangan jika perlu
    st.sidebar.write("MENU:")
    menu = st.sidebar.radio("", ["📈 PERFORMANCE", "🔄 SWITCHING", "🛒 AFFINITY"], label_visibility="collapsed")
    st.sidebar.markdown("---")

    st.sidebar.markdown("""
    <a href="https://shopper-insight.streamlit.app/" target="_blank">
        <button style="
            width:100%;
            background: linear-gradient(135deg, #FF0000, #CC0000);
            color:white;
            border:none;
            padding:12px;
            border-radius:12px;
            font-weight:500;
            font-size:10px;
            cursor:pointer;
            box-shadow: 0 4px 10px rgba(255,0,0,0.25);
        ">
            Shopper Insight Phase 1
        </button>
    </a>
    """, unsafe_allow_html=True)

    if menu == "📈 PERFORMANCE":
        col_title, col_plano, col_sec = st.columns([5, 2.5, 2.5])
        with col_title: st.title("PERFORMANCE OVERVIEW")
        with col_plano: sel_plano = st.selectbox(
                            "VERSI PLANO",
                            ["V1", "V2", "NOT_TRIAL"],
                            key="plano_perf"
                        )
        df_p = load_perf_file("category", sel_plano)

        # 🔥 Bersihkan section tidak valid
        df_p = df_p[~df_p["SECTION"].isin(["UNKNOWN", "-", "", "NAN", "NONE"])]

        # 🔥 Build section list dari data tersebut
        sections_only = sorted(df_p["SECTION"].dropna().unique().tolist())

        start_idx = next((i for i, s in enumerate(sections_only) if str(s).startswith('B')), 0)

        # 🔥 Universe transaksi global
        global total_struk_global
        if 'df_raw' in globals():
            total_struk_global = df_raw['NO_STRUK'].nunique()
        else:
            total_struk_global = df_p['BUYER_COUNT_BEFORE'].max()
        with col_sec: 
            # HAPUS ["ALL"] + dan gunakan index=start_idx
            sel_sec = st.selectbox("SECTION FILTER", sections_only, index=start_idx, key="sec_perf")
        st.markdown(f"**[NOV 2025 - JAN 2026]**")

        st.markdown("---")

        def get_dynamic_options(df, col_name, current_selections, filter_dict):
            temp_df = df.copy()
            for k, v in filter_dict.items():
                if v: # Jika filter lain sedang terisi, saring datanya
                    temp_df = temp_df[temp_df[k].isin(v)]
            # Ambil opsi yang tersisa
            opts = set(temp_df[col_name].dropna().unique())
            # Cegah error Streamlit dengan tetap mempertahankan pilihan yang sedang aktif
            for sel in current_selections:
                opts.add(sel)
            return sorted(list(opts))

        # =================================================================
        t_cat, t_sub, t_brand, t_plu, t_seg = st.tabs(["CATEGORY", "SUBCATEGORY", "BRAND", "PLU", "SEGMENTASI"])

        def apply_filter(df):
            if df.empty: return df
            if sel_sec != "ALL": df = df[df["SECTION"] == sel_sec]
            return df.reset_index(drop=True)
        st.markdown (" ---- ")
        with t_cat:
            df_f = apply_filter(load_perf_file("category", sel_plano))
            if not df_f.empty:
                card_place = st.container()
                s_l = st.multiselect(" FILTER CATEGORY:", sorted(df_f["CATEGORY"].unique()), key="f_cat")
                if s_l: df_f = df_f[df_f["CATEGORY"].isin(s_l)]
                with card_place:
                    render_performance_cards(df_f, is_category=True)
                display_styled_table(reorder_final(df_f, "category"))

                render_category_promo_driven(df_f)

                # 🔥 TAMBAHKAN INI
                render_category_promo_share_chart(df_f)

                render_static_affinity_matrix()

        # ==========================================
        # TAB SUBCATEGORY
        # ==========================================
        # ==========================================
        # TAB SUBCATEGORY
        # ==========================================
        with t_sub:
            df_f = apply_filter(load_perf_file("subcategory", sel_plano))
            if not df_f.empty:
                # Ambil state filter saat ini
                curr_cat = st.session_state.get("m_sub_c", [])
                curr_sub = st.session_state.get("m_sub_s", [])
                
                # Hitung opsi dinamis (Saling menyusut)
                cat_opts = get_dynamic_options(df_f, "CATEGORY", curr_cat, {"SUBCATEGORY": curr_sub})
                sub_opts = get_dynamic_options(df_f, "SUBCATEGORY", curr_sub, {"CATEGORY": curr_cat})
                
                f_cols = st.columns([10, 10]) 
                with f_cols[0]: m_cat = st.multiselect("CAT:", cat_opts, key="m_sub_c")
                with f_cols[1]: m_sub = st.multiselect("SUBCAT:", sub_opts, key="m_sub_s")
                
                # Saring data akhir
                if m_cat: df_f = df_f[df_f["CATEGORY"].isin(m_cat)]
                if m_sub: df_f = df_f[df_f["SUBCATEGORY"].isin(m_sub)]
                
                render_performance_cards(df_f, is_category=False)
                display_styled_table(reorder_final(df_f, "subcategory"))
                render_static_affinity_matrix()

        # ==========================================
        # TAB BRAND
        # ==========================================
        with t_brand:
            df_f = apply_filter(load_perf_file("brand", sel_plano))
            if not df_f.empty:
                curr_cat = st.session_state.get("m_br_c", [])
                curr_sub = st.session_state.get("m_br_s", [])
                curr_br = st.session_state.get("m_br_b", [])
                
                cat_opts = get_dynamic_options(df_f, "CATEGORY", curr_cat, {"SUBCATEGORY": curr_sub, "BRAND": curr_br})
                sub_opts = get_dynamic_options(df_f, "SUBCATEGORY", curr_sub, {"CATEGORY": curr_cat, "BRAND": curr_br})
                br_opts = get_dynamic_options(df_f, "BRAND", curr_br, {"CATEGORY": curr_cat, "SUBCATEGORY": curr_sub})

                f_cols = st.columns([5, 5, 5]) 
                with f_cols[0]: m_cat = st.multiselect("CAT:", cat_opts, key="m_br_c")
                with f_cols[1]: m_sub = st.multiselect("SUBCAT:", sub_opts, key="m_br_s")
                with f_cols[2]: m_br = st.multiselect("BRAND:", br_opts, key="m_br_b")

                if m_cat: df_f = df_f[df_f["CATEGORY"].isin(m_cat)]
                if m_sub: df_f = df_f[df_f["SUBCATEGORY"].isin(m_sub)]
                if m_br: df_f = df_f[df_f["BRAND"].isin(m_br)]

                render_performance_cards(df_f, is_category=False)
                display_styled_table(reorder_final(df_f, "brand"))
                render_static_affinity_matrix()

        # ==========================================
        # TAB PLU
        # ==========================================
        with t_plu:
            df_f = apply_filter(load_perf_file("plu", sel_plano))
            if not df_f.empty:
                curr_cat = st.session_state.get("m_plu_c", [])
                curr_plu = st.session_state.get("m_plu_p", [])
                
                cat_opts = get_dynamic_options(df_f, "CATEGORY", curr_cat, {"PLU": curr_plu})
                plu_opts = get_dynamic_options(df_f, "PLU", curr_plu, {"CATEGORY": curr_cat})

                f_cols = st.columns([5, 5])
                with f_cols[0]: m_cat = st.multiselect("CAT:", cat_opts, key="m_plu_c")
                with f_cols[1]: m_plu = st.multiselect("PLU:", plu_opts, key="m_plu_p")

                if m_cat: df_f = df_f[df_f["CATEGORY"].isin(m_cat)]
                if m_plu: df_f = df_f[df_f["PLU"].isin(m_plu)]

                render_performance_cards(df_f, is_category=False)
                display_styled_table(reorder_final(df_f, "plu"))
                render_static_affinity_matrix()

        # ==========================================
        # TAB SEGMENTASI (BACK TO SUB-TABS DESIGN)
        # ==========================================
        with t_seg:
            df_seg = load_segment_unified()
            if not df_seg.empty:
                # 1. Base Filter (Plano & Section)
                df_seg_f = df_seg[df_seg["VERSI"].str.upper() == sel_plano.upper()].copy()
                df_seg_f = apply_global_perf(df_seg_f, sel_sec) 
                
                # 2. Filter Hierarki Produk (Smart Cross-Filtering)
                curr_cat = st.session_state.get("seg_c", [])
                curr_sub = st.session_state.get("seg_s", [])
                curr_br = st.session_state.get("seg_b", [])
                
                cat_opts = get_dynamic_options(df_seg_f, "CATEGORY", curr_cat, {"SUBCATEGORY": curr_sub, "BRAND": curr_br})
                sub_opts = get_dynamic_options(df_seg_f, "SUBCATEGORY", curr_sub, {"CATEGORY": curr_cat, "BRAND": curr_br})
                br_opts = get_dynamic_options(df_seg_f, "BRAND", curr_br, {"CATEGORY": curr_cat, "SUBCATEGORY": curr_sub})

                f1, f2, f3 = st.columns(3)
                with f1: m_cat_seg = st.multiselect("FILTER CATEGORY", cat_opts, key="seg_c")
                with f2: m_sub_seg = st.multiselect("FILTER SUBCATEGORY", sub_opts, key="seg_s")
                with f3: m_brand_seg = st.multiselect("FILTER BRAND", br_opts, key="seg_b")

                # Terapkan filter hierarki ke dataframe utama tab ini
                if m_cat_seg: df_seg_f = df_seg_f[df_seg_f["CATEGORY"].isin(m_cat_seg)]
                if m_sub_seg: df_seg_f = df_seg_f[df_seg_f["SUBCATEGORY"].isin(m_sub_seg)]
                if m_brand_seg: df_seg_f = df_seg_f[df_seg_f["BRAND"].isin(m_brand_seg)]

                if not df_seg_f.empty:
                    # 3. Render Kartu (Tanpa Category Penetration)
                    # Kita ambil baris unik per SEGMENT_VALUE agar kartu tidak double count
                    df_for_cards = df_seg_f.drop_duplicates(subset=['SEGMENT_TYPE', 'SEGMENT_VALUE', 'CATEGORY'])
                    render_performance_cards(df_for_cards, is_category=False)
                    
                    # 4. Render Sub-Tabs berdasarkan SEGMENT_TYPE
                    seg_list = sorted(df_seg_f["SEGMENT_TYPE"].dropna().unique())
                    tabs_seg = st.tabs([s.upper() for s in seg_list])
                    
                    for i, s_type in enumerate(seg_list):
                        with tabs_seg[i]:
                            # Filter data khusus tipe segmen ini
                            df_tab = df_seg_f[df_seg_f["SEGMENT_TYPE"] == s_type].copy()
                            
                            # Aggregasi untuk Tabel
                            group_cols = ["SEGMENT_VALUE", "CATEGORY", "SECTION"]
                            num_cols = df_tab.select_dtypes(include=[np.number]).columns.tolist()
                            agg_dict = {c: ('mean' if any(x in c for x in ['GROWTH', 'PENETRATION']) else 'sum') for c in num_cols}
                            df_clean = df_tab.groupby(group_cols).agg(agg_dict).reset_index()

                            display_styled_table(reorder_final(df_clean, "category"))
                            render_static_affinity_matrix()
                else:
                    st.warning("Data tidak ditemukan untuk filter ini.")
                    
    elif menu == "🔄 SWITCHING":
        col_title, col_sec_filter = st.columns([6, 4])
        with col_title:
            st.markdown('<h1 style="margin:0;">🔄 SWITCHING & LOYALTY ANALYSIS</h1>', unsafe_allow_html=True)
        with col_sec_filter:
            sel_sec_sw = st.selectbox("SECTION FILTER", sections_only, index=start_idx, key="sec_sw_top")
        st.markdown(f"**[NOV 2025 - JAN 2026]**")

        st.markdown("---")
        loy_data = load_loyalty_data()
        
        if not loy_data:
            st.error("Switching data not found!")
        else:
            tab_configs = [
                {"name": "BRAND LOYALTY (CAT)", "df_key": "br_loy_cat", "filters": ["CATEGORY", "BRAND_BEFORE"], "main_col": "BRAND_BEFORE", "after_col": "BRAND_AFTER", "id_level": ["CATEGORY", "BRAND_BEFORE"]},
                {"name": "BRAND LOYALTY (SUBCAT)", "df_key": "br_loy_sub", "filters": ["SUBCATEGORY", "BRAND_BEFORE"], "main_col": "BRAND_BEFORE", "after_col": "BRAND_AFTER", "id_level": ["SUBCATEGORY", "CATEGORY", "BRAND_BEFORE"]},
                {"name": "BRAND SWITCH (CAT)", "df_key": "br_swi_cat", "filters": ["BRAND", "CATEGORY_BEFORE"], "main_col": "CATEGORY_BEFORE", "after_col": "CATEGORY_AFTER", "id_level": ["BRAND", "CATEGORY_BEFORE"]},
                {"name": "BRAND SWITCH (SUBCAT)", "df_key": "br_swi_sub", "filters": ["BRAND", "SUBCATEGORY_BEFORE"], "main_col": "SUBCATEGORY_BEFORE", "after_col": "SUBCATEGORY_AFTER", "id_level": ["BRAND", "SUBCATEGORY_BEFORE"]},
                {"name": "CATEGORY SWITCHING", "df_key": "cat_loy", "filters": ["SECTION", "CATEGORY_BEFORE"], "main_col": "CATEGORY_BEFORE", "after_col": "CATEGORY_AFTER", "id_level": ["CATEGORY_BEFORE"]},
                {"name": "SUBCATEGORY SWITCHING", "df_key": "sub_loy", "filters": ["CATEGORY", "SUBCATEGORY_BEFORE"], "main_col": "SUBCATEGORY_BEFORE", "after_col": "SUBCATEGORY_AFTER", "id_level": ["CATEGORY", "SUBCATEGORY_BEFORE"]}
            ]

            tabs = st.tabs([cfg["name"] for cfg in tab_configs])
            
            for i, cfg in enumerate(tab_configs):
                with tabs[i]:
                    df_raw = loy_data[cfg["df_key"]].copy()
                    
                    if sel_sec_sw != "ALL":
                        df_raw = df_raw[df_raw["SECTION"] == sel_sec_sw]

                    # --- ROW 1: FILTERS (Single Select with "ALL" Option) ---
                    extra_after_filter = None

                    if cfg["name"] in ["BRAND LOYALTY (CAT)", "BRAND LOYALTY (SUBCAT)"]:
                        extra_after_filter = "BRAND_AFTER"

                    elif cfg["name"] in ["BRAND SWITCH (CAT)", "CATEGORY SWITCHING"]:
                        extra_after_filter = "CATEGORY_AFTER"

                    elif cfg["name"] in ["BRAND SWITCH (SUBCAT)", "SUBCATEGORY SWITCHING"]:
                        extra_after_filter = "SUBCATEGORY_AFTER"


                    # Gabungkan filter existing + filter AFTER
                    all_filters = cfg["filters"].copy()
                    if extra_after_filter:
                        all_filters.append(extra_after_filter)

                    col_filters = st.columns([1]*len(all_filters), gap="large")


                    active_filters = {}

                    for j, filt_col in enumerate(all_filters):
                        with col_filters[j]:
                            if filt_col in df_raw.columns:

                                unique_vals = sorted(df_raw[filt_col].dropna().unique().tolist())
                                item_keys = [f"chk_sw_{i}_{j}_{val}" for val in unique_vals]

                                # INIT default checked
                                for k in item_keys:
                                    if k not in st.session_state:
                                        st.session_state[k] = True

                                label = f"{filt_col}:"
                                with st.popover(label):

                                    colA, colB = st.columns(2)

                                    # SELECT ALL
                                    with colA:
                                        if st.button("Select All", key=f"btn_all_{i}_{j}"):
                                            for k in item_keys:
                                                st.session_state[k] = True

                                    # CLEAR ALL
                                    with colB:
                                        if st.button("Clear All", key=f"btn_clear_{i}_{j}"):
                                            for k in item_keys:
                                                st.session_state[k] = False

                                    selected_vals = []

                                    for val in unique_vals:
                                        k = f"chk_sw_{i}_{j}_{val}"
                                        if st.checkbox(val, key=k):
                                            selected_vals.append(val)
                                    if selected_vals and len(selected_vals) < len(unique_vals):
                                        tag_html = ""
                                        for v in selected_vals:
                                            tag_html += f"""
                                            <span style="
                                                display:inline-block;
                                                background:#F1F5F9;
                                                padding:6px 12px;
                                                border-radius:20px;
                                                margin:3px;
                                                font-size:12px;
                                                border:1px solid #E2E8F0;">
                                                {v}
                                            </span>
                                            """
                                        st.markdown(tag_html, unsafe_allow_html=True)            

                                # simpan state filter
                                active_filters[filt_col] = selected_vals

                                # apply filter
                                if selected_vals:
                                    df_raw = df_raw[df_raw[filt_col].isin(selected_vals)]

                    if df_raw.empty:
                        st.warning("No data available for this filter.")
                        continue
                    
                    st.markdown("<br>", unsafe_allow_html=True)

                    # --- ROW 2: KPI CARDS ---
                    total_sw = df_raw[df_raw["SWITCH_FLAG"] == "SWITCH"]["BUYER_ID"].nunique()
                    total_no = df_raw[df_raw["SWITCH_FLAG"] == "NO_SWITCH"]["BUYER_ID"].nunique()
                    
                   # Logika untuk mencari Top Destination (FIXED)
                    top_dest_name = "-"
                    top_dest_pct = 0.0

                    df_only_sw = df_raw[df_raw["SWITCH_FLAG"] == "SWITCH"]

                    if not df_only_sw.empty:

                        # 🔥 WAJIB: pastikan 1 buyer hanya 1 row
                        df_unique_sw = (
                            df_only_sw
                            .drop_duplicates(subset=["BUYER_ID"])
                        )

                        dest_counts = (
                            df_unique_sw
                            .groupby(cfg["after_col"])["BUYER_ID"]
                            .nunique()
                            .reset_index()
                        )

                        if not dest_counts.empty:
                            top_dest_row = dest_counts.loc[dest_counts["BUYER_ID"].idxmax()]

                            top_dest_name = str(top_dest_row[cfg["after_col"]])
                            top_dest_count = top_dest_row["BUYER_ID"]

                            # denominator pakai total switchers
                            top_dest_pct = top_dest_count / total_sw if total_sw > 0 else 0.0

                    # Panggil render 3 kartu
                    render_switching_cards(total_sw, total_no, top_dest_name, top_dest_pct)

                    # --- ROW 3: AGGREGATION TABLE ---
                    st.markdown("#### 📑 Detailed Switching Data")
                    group_cols = cfg["id_level"] + ["SECTION"]
                    agg_df = df_raw.groupby(group_cols + ["SWITCH_FLAG"])["BUYER_ID"].nunique().unstack(fill_value=0)
                    
                    for col in ["SWITCH", "NO_SWITCH"]:
                        if col not in agg_df.columns: agg_df[col] = 0
                    
                    agg_df["TOTAL"] = agg_df["SWITCH"] + agg_df["NO_SWITCH"]
                    agg_df["% SWITCH"] = (agg_df["SWITCH"] / agg_df["TOTAL"])
                    agg_df["% NO_SWITCH"] = (agg_df["NO_SWITCH"] / agg_df["TOTAL"])
                    
                    table_display = agg_df.reset_index()[group_cols + ["% SWITCH", "% NO_SWITCH"]]
                    table_display = table_display.sort_values([group_cols[0], "% SWITCH"], ascending=[True, False])

                    styled_table = (
                        table_display.style.format({"% SWITCH": "{:.2%}", "% NO_SWITCH": "{:.2%}"})
                        .set_properties(**{'background-color': '#FFFFFF', 'color': '#333333', 'border': '1px solid #F1F5F9'})
                        .background_gradient(cmap="Reds", subset=["% SWITCH"])
                        .background_gradient(cmap="Greens", subset=["% NO_SWITCH"])
                    )
                    st.dataframe(styled_table, use_container_width=True, height=400, hide_index=True)

                    st.markdown("<br>", unsafe_allow_html=True)

                    # --- ROW 4: TWO PIE CHARTS SIDE BY SIDE ---
                    st.markdown("<br>", unsafe_allow_html=True)
                    col_pie1, col_pie2 = st.columns(2)

                    # =========================================================
                    # LEFT — DONUT SWITCH VS NO SWITCH (GREEN EXECUTIVE)
                    # =========================================================
                    with col_pie1:

                        total = total_sw + total_no

                        if total > 0:

                            pct_sw = total_sw / total

                            fig_overall = px.pie(
                                values=[total_sw, total_no],
                                names=["SWITCH", "NO SWITCH"],
                                hole=0.65,
                                color_discrete_sequence=["#16A34A", "#BBF7D0"]  # Hijau solid + soft
                            )

                            fig_overall.update_traces(
                                textinfo="percent",
                                textfont_size=14,
                                marker=dict(line=dict(color="white", width=2))
                            )

                            fig_overall.update_layout(
                                height=420,
                                margin=dict(t=70, b=20, l=20, r=20),

                                title=dict(
                                    text="SWITCH VS NO SWITCH",
                                    x=0.5,
                                    xanchor="center",
                                    font=dict(size=20, color="#475569")
                                ),

                                annotations=[
                                    dict(
                                        text=(
                                            f"<b style='font-size:28px'>{pct_sw:.0%}</b><br>"
                                            f"<span style='font-size:14px'>{total_sw:,} Switchers</span><br>"
                                            f"<span style='font-size:14px; color:#6B7280'>of {total:,} Total Buyers</span>"
                                        ),
                                        x=0.5,
                                        y=0.5,
                                        showarrow=False,
                                        align="center"
                                    )
                                ],

                                showlegend=True,
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)'
                            )

                            st.plotly_chart(fig_overall, use_container_width=True, key=f"overall_{i}")

                            st.caption(
                                f"Switchers: {total_sw:,} | Retained: {total_no:,}"
                            )

                        else:
                            st.info("No data available.")


                    # =========================================================
                    # RIGHT — TOP DESTINATION (GREEN TONE + INSIGHT)
                    # =========================================================
                    with col_pie2:

                        if not df_only_sw.empty:

                            dest_data = (
                                df_only_sw
                                .drop_duplicates(subset=["BUYER_ID"])  # penting!
                                .groupby(cfg["after_col"])["BUYER_ID"]
                                .nunique()
                                .reset_index()
                                .sort_values("BUYER_ID", ascending=False)
                            )

                            total_dest = total_sw

                            fig_dest_pie = px.pie(
                                dest_data,
                                values="BUYER_ID",
                                names=cfg["after_col"],
                                color_discrete_sequence=[
                                "#1F3A5F",  # deep navy
                                "#2A9D8F",  # teal
                                "#E9C46A",  # soft gold
                                "#F4A261",  # warm orange
                                "#E76F51",  # muted coral
                                "#6D597A",  # soft purple
                                "#8AB17D",  # sage green
                                "#457B9D",  # steel blue
                                "#B5838D",  # dusty rose
                                "#84A59D",  # grey teal
                                "#3D405B",  # dark slate
                                "#A8DADC"   # light aqua
                            ]
                            )

                            fig_dest_pie.update_traces(
                                textinfo="percent",          # atau "none" kalau mau super clean
                                textposition="inside",       # paksa di dalam
                                insidetextorientation="horizontal",
                                pull=0,                      # pastikan tidak ada slice ditarik
                                marker=dict(line=dict(color="white", width=2))
                            )

                            fig_dest_pie.update_layout(
                                height=420,
                                margin=dict(t=70, b=20, l=20, r=20),
                                title=dict(
                                    text="DESTINATION SWITCH",
                                    x=0.5,
                                    xanchor="center",
                                    font=dict(size=20, color="#475569")
                                ),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)'
                            )

                            st.plotly_chart(fig_dest_pie, use_container_width=True, key=f"dest_{i}")

                            # 🔥 Insight tambahan otomatis
                            top_row = dest_data.iloc[0]
                            top_share = top_row["BUYER_ID"] / total_dest


                        else:
                            st.info("No switch data to analyze for this filter.")

                    st.markdown("<hr style='border: 1px dashed #E2E8F0; margin: 30px 0;'>", unsafe_allow_html=True)

                    # --- ROW 5: PROMO INFLUENCE ---
                    st.markdown("<h4 style='text-align: center; color: #475569; font-weight: 600;'>PROMO INFLUENCE ON DESTINATION SWITCH</h4>", unsafe_allow_html=True)
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # 🔥 Ambil hanya SWITCHERS
                    # 🔥 Ambil hanya SWITCHERS
                    df_switch = df_raw[df_raw["SWITCH_FLAG"] == "SWITCH"].copy()

                    # 🔥 Pastikan benar-benar pindah (BEFORE != AFTER)
                    df_switch = df_switch[
                        df_switch[cfg["main_col"]] != df_switch[cfg["after_col"]]
                    ]

                    # 🔥 Ambil top destination dari switchers saja
                    top_brands = (
                        df_switch.groupby(cfg["after_col"])["BUYER_ID"]
                        .nunique()
                        .nlargest(15)
                        .index
                    )

                    df_promo = df_switch[df_switch[cfg["after_col"]].isin(top_brands)]
                    
                    if not df_promo.empty:
                        promo_agg = df_promo.groupby([cfg["after_col"], "PROMO_FLAG"])["BUYER_ID"].nunique().reset_index()
                        totals = promo_agg.groupby(cfg["after_col"])["BUYER_ID"].transform('sum')
                        promo_agg['PERCENTAGE'] = promo_agg['BUYER_ID'] / totals
                        
                        fig_promo = px.bar(
                            promo_agg, x=cfg["after_col"], y="PERCENTAGE", color="PROMO_FLAG",
                            color_discrete_map={"PROMO": "#27AE60", "NON PROMO": "#919191"},
                            barmode="stack",    
                            text=promo_agg["PERCENTAGE"].apply(lambda x: f"{x:.1%}") 
                        )
                        fig_promo.update_layout(
                            template='plotly_white', height=400, 
                            xaxis_title="", yaxis_title="Percentage",
                            yaxis=dict(tickformat=".0%"),
                            # Posisi legend agak diangkat agar tidak menabrak bar
                            legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1),
                            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                            margin=dict(t=20, b=0, l=0, r=0)
                        )
                        st.plotly_chart(fig_promo, use_container_width=True, key=f"promo_{i}")
                    else:
                        st.info("No promo data available.")

    elif menu == "🛒 AFFINITY":
        # ==========================================
        # TOP FILTER HEADER (SECTION & PLANO GROUP)
        # ==========================================
        col_title, col_plano_filter, col_sec_filter = st.columns([5, 2.5, 2.5])
        with col_title:
            st.title("🛒 MARKET BASKET ANALYSIS")

        # SETUP OPSI PLANO
        plano_options = ["BEFORE_V1", "BEFORE_V2", "AFTER_V1", "AFTER_V2", "NOT_TRIAL"]
        st.markdown(f"**[NOV 2025 - JAN 2026]**")
        with col_plano_filter:
            sel_plano = st.selectbox(
                "VERSI PLANO",
                plano_options,
                index=2, # Default ke index 2 ("AFTER_V1")
                key="plano_aff_top"
            )

        with col_sec_filter:
            sel_sec_aff = st.selectbox(
                "SECTION FILTER",
                sections_only,
                key="sec_aff_top_right"
            )

        st.markdown("---")

        aff = load_affinity_data()

        if not aff:
            st.error("Data Affinity tidak ditemukan!")
        else:

            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
                "CATEGORY",
                "SUB-CATEGORY",
                "BRAND/CAT",
                "BRAND/SUBCAT",
                "SAME BRAND / CROSS CAT",
                "SAME BRAND / CROSS SUBCAT"
            ])

            # ======================================================
            # FILTER MASTER: MENGAPLIKASIKAN SECTION & PLANO
            # ======================================================
            def filter_affinity_base(df, section_val, plano_val):
                df = df.copy()
                df.columns = [c.lower() for c in df.columns]

                # Filter by Section
                if "section" in df.columns:
                    df["section"] = df["section"].astype(str).str.strip().str.upper()
                    df = df[df["section"] == str(section_val).strip().upper()]

                # Filter by Plano Group Final
                if "plano_group_final" in df.columns:
                    df["plano_group_final"] = df["plano_group_final"].astype(str).str.strip().str.upper()
                    df = df[df["plano_group_final"] == str(plano_val).strip().upper()]

                return df.reset_index(drop=True)

            # ======================================================
            # TAB 1 — CATEGORY
            # ======================================================
            with tab1:
                df_cat = aff["cat"].copy()
                df_f = filter_affinity_base(df_cat, sel_sec_aff, sel_plano)

                categories_in_section = set(df_f["category_a"].astype(str).unique()).intersection(
                    set(df_f["category_b"].astype(str).unique())
                )

                df_f = df_f[
                    df_f["category_a"].astype(str).isin(categories_in_section) &
                    df_f["category_b"].astype(str).isin(categories_in_section)
                ].reset_index(drop=True)

                st.subheader(f"AFFINITY CATEGORY BY SECTION : {sel_sec_aff}")
                render_affinity_tab(df_f, "category_a", "category_b", ["category_a", "category_b"], "c_aff")

            # ======================================================
            # TAB 2 — SUB CATEGORY
            # ======================================================
            with tab2:
                df_sub = aff["subcat"].copy()
                df_f = filter_affinity_base(df_sub, sel_sec_aff, sel_plano)

                valid_sub = set(pd.concat([df_f["subcategory_a"], df_f["subcategory_b"]]).astype(str).unique())

                df_f = df_f[
                    df_f["subcategory_a"].astype(str).isin(valid_sub) &
                    df_f["subcategory_b"].astype(str).isin(valid_sub)
                ].reset_index(drop=True)

                st.subheader(f"AFFINITY SUBCATEGORY BY SECTION : {sel_sec_aff}")
                render_affinity_tab(df_f, "subcategory_a", "subcategory_b", ["subcategory_a", "subcategory_b"], "s_aff")

            # ======================================================
            # TAB 3 — BRAND BY CATEGORY
            # ======================================================
            with tab3:
                df_bc = aff["brand_cat"].copy()
                df_f = filter_affinity_base(df_bc, sel_sec_aff, sel_plano)

                # 🚨 STOP jika data kosong
                if df_f.empty:
                    st.warning("Data BRAND affinity tidak tersedia untuk kombinasi Section & Plano ini.")
                    st.stop()

                df_f = df_f.dropna(subset=["brand_a", "brand_b"]).reset_index(drop=True)

                st.subheader(f"AFFINITY BRAND BY CATEGORY SECTION : {sel_sec_aff}")

                render_affinity_tab(
                    df_f,
                    "brand_a",
                    "brand_b",
                    ["brand_a", "brand_b", "category_a", "category_b"],
                    "bc_aff",
                    show_qty_impact=False,
                    show_top10=False
                )

            # ======================================================
            # TAB 4 — BRAND BY SUB CATEGORY
            # ======================================================
            with tab4:
                df_bs = aff["brand_sub"].copy()
                df_f = filter_affinity_base(df_bs, sel_sec_aff, sel_plano)

                if df_f.empty:
                    st.warning("Data BRAND affinity tidak tersedia untuk kombinasi Section & Plano ini.")
                    st.stop()

                df_f = df_f.dropna(subset=["brand_a", "brand_b"]).reset_index(drop=True)

                st.subheader(f"AFFINITY BRAND BY SUBCATEGORY SECTION : {sel_sec_aff}")

                render_affinity_tab(
                    df_f,
                    "brand_a",
                    "brand_b",
                    ["brand_a", "brand_b", "subcategory_a", "subcategory_b"],
                    "bs_aff",
                    show_qty_impact=False,
                    show_top10=False
                )
            # ======================================================
            # TAB 5 — SAME BRAND CROSS CATEGORY (1 SECTION)
            # ======================================================
            with tab5:
                df_sbc = aff["same_brand_cat"].copy()
                df_f = filter_affinity_base(df_sbc, sel_sec_aff, sel_plano)

                if df_f.empty:
                    st.warning("Data Same Brand Cross Category tidak tersedia.")
                    st.stop()

                df_f = df_f.dropna(subset=["brand"]).reset_index(drop=True)

                st.subheader(f"SAME BRAND - CROSS CATEGORY : {sel_sec_aff}")

                render_affinity_tab(
                    df_f,
                    "category_a",
                    "category_b",
                    ["brand", "category_a", "category_b"],
                    "sbc_aff",
                    show_qty_impact=False
                )
                # ======================================================
                # TAB 6 — SAME BRAND CROSS SUBCATEGORY (1 CATEGORY)
                # ======================================================
                with tab6:
                    df_sbs = aff["same_brand_subcat"].copy()
                    df_f = filter_affinity_base(df_sbs, sel_sec_aff, sel_plano)

                    if df_f.empty:
                        st.warning("Data Same Brand Cross Subcategory tidak tersedia.")
                        st.stop()

                    df_f = df_f.dropna(subset=["brand"]).reset_index(drop=True)

                    st.subheader(f"SAME BRAND - CROSS SUBCATEGORY : {sel_sec_aff}")

                    render_affinity_tab(
                        df_f,
                        "subcategory_a",
                        "subcategory_b",
                        ["brand", "subcategory_a", "subcategory_b"],
                        "sbs_aff",
                        show_qty_impact=False
                    )

        # ======================================================
        # TABEL MAPPING REFERENSI (PIVOT VERSION - CLEAN)
        # ======================================================
        st.markdown("---")
        with st.expander("📋 MATRIKS VARIAN BY VERSI PLANO", expanded=False):
            
            # 1. Ambil data unik dari dataset affinity
            df_map = pd.concat([aff["cat"], aff["subcat"]], ignore_index=True)
            df_map.columns = [c.lower() for c in df_map.columns]
            
            # 2. List kolom yang dibutuhkan (Tanpa KD_SECTION)
            cols_needed = ['section', 'kd_variant', 'plano_group_final']
            available = [c for c in cols_needed if c in df_map.columns]
            
            if len(available) == 3:
                # 3. Proses Pivot
                # Index: SECTION, Columns: PLANO_GROUP_FINAL, Values: KD_VARIANT
                df_ref_pivot = df_map[available].drop_duplicates()
                
                df_pivoted = df_ref_pivot.pivot_table(
                    index='section', 
                    columns='plano_group_final', 
                    values='kd_variant',
                    aggfunc=lambda x: ', '.join(x.astype(str).unique())
                ).reset_index().fillna("-")
                
                # Urutkan kolom agar BEFORE muncul sebelum AFTER jika memungkinkan
                cols = df_pivoted.columns.tolist()
                sorted_cols = [cols[0]] + sorted(cols[1:])
                df_pivoted = df_pivoted[sorted_cols]
                
                # 4. Render Tabel
                st.dataframe(
                    df_pivoted.style.set_properties(**{
                        'background-color': 'transparent',
                        'color': '#333333',
                        'border': '1px solid #F5F5F5',
                        'font-size': '12px',
                        'text-align': 'left'
                    }),
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("Kolom mapping (Section/Variant/Plano) tidak lengkap di dataset.")


if __name__ == "__main__":
    main()