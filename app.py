import streamlit as st
from dataclasses import dataclass
from typing import List

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Perfume Advisor Pro",
    layout="wide"
)

# =========================================================
# MODELOS DE DATOS
# =========================================================
@dataclass
class Perfume:
    name: str
    family: str
    intensity: str
    ideal_for: str
    price: str

@dataclass
class UserProfile:
    ph: float
    intensity_preference: str
    usage_context: str

# =========================================================
# ESTILOS PROFESIONALES
# =========================================================
def apply_styles(background):
    st.markdown(
        f"""
        <style>
        body {{
            background-color: {background};
        }}
        .stApp {{
            font-family: "Inter", sans-serif;
        }}
        .card {{
            background: white;
            border-radius: 14px;
            padding: 22px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# HEADER COMERCIAL
# =========================================================
st.markdown(
    """
    <div style="max-width:960px;margin:auto;text-align:center;padding-bottom:40px;">
        <h1>Perfume Advisor Pro</h1>
        <p>
            Intelligent fragrance recommendations based on skin chemistry,
            lifestyle preferences, and performance profiling.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# PERFIL DEL USUARIO
# =========================================================
st.markdown("### User Profile")

col1, col2, col3 = st.columns(3)

with col1:
    ph = st.slider("Skin pH", 0.0, 14.0, 5.5, 0.1)

with col2:
    intensity = st.selectbox(
        "Preferred intensity",
        ["Light", "Moderate", "Strong"]
    )

with col3:
    context = st.selectbox(
        "Primary usage",
        ["Daily wear", "Office", "Evening events", "Special occasions"]
    )

user = UserProfile(ph, intensity, context)

# =========================================================
# MOTOR DE RECOMENDACIÓN
# =========================================================
def generate_recommendation(profile: UserProfile):
    if profile.ph < 5:
        background = "#F4F8FF"
        family = "Fresh / Aquatic"
        perfumes = [
            Perfume("Acqua di Gio", "Fresh", "Moderate", "Daily wear", "$95"),
            Perfume("Nautica Voyage", "Aquatic", "Light", "Warm climates", "$25"),
            Perfume("Versace Pour Homme", "Fresh Aromatic", "Moderate", "Office", "$85"),
            Perfume("Issey Miyake L'Eau d'Issey", "Fresh Floral", "Light", "Professional", "$75"),
            Perfume("Davidoff Cool Water", "Aquatic", "Moderate", "Casual", "$60"),
        ]

    elif profile.ph <= 7:
        background = "#FFFDF4"
        family = "Balanced / Floral / Fresh"
        perfumes = [
            Perfume("Chanel Chance Eau Tendre", "Floral", "Light", "Daily wear", "$110"),
            Perfume("Dolce & Gabbana Light Blue", "Citrus", "Moderate", "Daytime", "$85"),
            Perfume("Burberry Her", "Fruity Floral", "Moderate", "Modern lifestyle", "$105"),
            Perfume("Versace Bright Crystal", "Floral Fresh", "Light", "Office", "$90"),
            Perfume("Miss Dior Blooming Bouquet", "Floral", "Light", "Formal", "$120"),
        ]

    else:
        background = "#FFF3F3"
        family = "Woody / Oriental / Intense"
        perfumes = [
            Perfume("Tom Ford Oud Wood", "Woody", "Strong", "Evening", "$250"),
            Perfume("Bleu de Chanel Parfum", "Woody Aromatic", "Moderate", "Professional", "$155"),
            Perfume("YSL Y EDP", "Sweet Woody", "Moderate", "Versatile", "$140"),
            Perfume("Spicebomb Extreme", "Spicy", "Strong", "Cold weather", "$120"),
            Perfume("Dior Sauvage Elixir", "Aromatic Spicy", "Strong", "Statement", "$160"),
        ]

    return background, family, perfumes

background, family, perfumes = generate_recommendation(user)

# =========================================================
# APLICAR TEMA
# =========================================================
apply_styles(background)

# =========================================================
# RESUMEN EJECUTIVO
# =========================================================
st.markdown(
    f"""
    <div class="card" style="max-width:960px;margin:auto;margin-bottom:30px;">
        <h3>Recommended Fragrance Profile</h3>
        <p><strong>{family}</strong></p>
        <p>
            Recommendations are tailored to your skin pH, preferred intensity,
            and usage context.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# RESULTADOS
# =========================================================
st.markdown("### Personalized Recommendations")

cols = st.columns(5)

for i, p in enumerate(perfumes):
    with cols[i]:
        st.markdown(
            f"""
            <div class="card">
                <h4>{p.name}</h4>
                <p>Family: {p.family}</p>
                <p>Intensity: {p.intensity}</p>
                <p>Ideal for: {p.ideal_for}</p>
                <p><strong>{p.price}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# FOOTER LEGAL
# =========================================================
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;color:#555;max-width:960px;margin:auto;">
        <p>
            Perfume Advisor Pro provides recommendations based on analytical models.
            Individual results may vary.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
