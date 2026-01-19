import streamlit as st
import datetime
from datetime import datetime, date
import pandas as pd
import os
import plotly.graph_objects as go
import random
import json
import base64
from PIL import Image

# Constants
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
THEMES_PATH = os.path.join(BASE_PATH, "themes")
ACTIVE_THEME_FILE = os.path.join(THEMES_PATH, "active_theme.txt")
ASSETS_PATH = os.path.join(BASE_PATH, "assets")
LOGOS_PATH = os.path.join(ASSETS_PATH, "logos", "campanas")
DESTINOS_PATH = os.path.join(ASSETS_PATH, "destinos")
COMPANY_LOGO = os.path.join(ASSETS_PATH, "logos", "empresa", "ambriz_logo.png")
THEME_BANNER = os.path.join(ASSETS_PATH, "themes", "current_theme.png")

# Page Configuration
try:
    favicon = Image.open(COMPANY_LOGO)
except Exception:
    favicon = "🚀"

st.set_page_config(
    page_title="Ambriz Asesores",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_theme_data(theme_file):
    try:
        with open(os.path.join(THEMES_PATH, theme_file), 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def load_active_theme_file():
    if os.path.exists(ACTIVE_THEME_FILE):
        try:
            with open(ACTIVE_THEME_FILE, 'r') as f:
                return f.read().strip()
        except: pass
    return "modo_neon.json"

# --- UTILS ---
def get_base64_image(image_path):
    try:
        if not os.path.exists(image_path):
            return ""
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except:
        return ""

# --- MASTERY RENDERING ENGINE ---
def configurar_estilo_visual(tema_actual, config_json):
    import random

    # 1. Leer Configuración
    colores = config_json.get("colores", {})
    color_fondo = colores.get("fondo", "#0e1117")

    # 2. CSS MAESTRO (Estabilidad + Diseño Neón)
    css_global = f"""
    <style>
        /* --- BLOQUEO DE ESTABILIDAD (Anti-Temblor) --- */
        html {{
            overflow-y: scroll !important; /* Bloquea el ancho de la página */
            scrollbar-gutter: stable !important;
        }}
        
        body, .stApp {{
            width: 100vw;
            overflow-x: hidden !important;
        }}

        /* Sidebar Inmóvil */
        section[data-testid="stSidebar"] {{
            overflow: hidden !important;
        }}

        /* FONDO DINÁMICO */
        .stApp {{
            background: {color_fondo} !important;
            background-attachment: fixed !important;
        }}

        /* BOTONES NEÓN */
        .stButton > button {{
            background: linear-gradient(90deg, #00FF88 0%, #00E676 100%) !important;
            color: #004D40 !important;
            border: none;
            border-radius: 12px;
            padding: 12px 28px;
            font-weight: 800;
            box-shadow: 0 4px 15px rgba(0, 255, 136, 0.4);
            transition: transform 0.2s ease;
        }}
        .stButton > button:hover {{
            transform: scale(1.02);
            color: #000000 !important;
        }}

        /* CAJAS DE DATOS */
        div[data-testid="stMetric"] {{
            background-color: rgba(255, 255, 255, 0.08); 
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 15px;
            border-radius: 10px;
            backdrop-filter: blur(5px);
            text-align: center;
        }}

        /* CENTRADO CRÍTICO */
        h1, h2, h3, p {{
            text-align: center !important;
        }}
        
        code {{ display: none !important; }}
    </style>
    """
    st.markdown(css_global, unsafe_allow_html=True)

    # 3. GESTOR DE EFECTOS ESPECIALES (Estructura Final)

    # A. DICIEMBRE (Nieve Nativa Realista - ¡Nada de CSS extra!)
    if "diciembre" in tema_actual or "navidad" in tema_actual: 
        st.snow()

    # B. JULIO (El Sol Brillante)
    elif "julio" in tema_actual or "verano" in tema_actual:
        st.markdown("""
        <style>
            .sun-glow {
                position: fixed; top: -200px; right: -200px; width: 400px; height: 400px;
                background: radial-gradient(circle, rgba(255, 230, 80, 1) 20%, rgba(255, 180, 20, 0.9) 50%, rgba(255, 200, 50, 0) 85%);
                box-shadow: 0 0 150px 100px rgba(255, 200, 50, 0.7);
                border-radius: 50%; z-index: 0; pointer-events: none;
                animation: sol-latido 5s infinite alternate;
            }
            @keyframes sol-latido { 0% { opacity: 0.7; transform: scale(1); } 100% { opacity: 1; transform: scale(1.1); } }
        </style>
        <div class="sun-glow"></div>
        """, unsafe_allow_html=True)

    # C. ABRIL (Confeti Fiesta Infantil - Mantener como está)
    elif "abril" in tema_actual or "nino" in tema_actual:
        colores_confeti = ["#ff0000", "#0000ff", "#ffff00", "#00ff00"] # Red, Blue, Yellow, Green
        items_confeti = ""
        for _ in range(40):
            lp = random.randint(0, 100)
            dl = random.uniform(0, 6)
            dr = random.uniform(3, 7)
            clr = random.choice(colores_confeti)
            sz = random.randint(8, 14)
            items_confeti += f'<div class="confeti-box" style="left:{lp}%; animation-duration:{dr}s; animation-delay:{dl}s; background:{clr}; width:{sz}px; height:{sz}px;"></div>'
        
        st.markdown(f"""
        <style>
            .confeti-box {{
                position: fixed; top: -10vh; z-index: 0; pointer-events: none;
                animation: fall-rotate linear infinite; opacity: 0.8;
            }}
            @keyframes fall-rotate {{
                0% {{ top: -10vh; transform: rotate(0deg); }}
                100% {{ top: 110vh; transform: rotate(720deg); }}
            }}
        </style>
        <div style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:0; overflow:hidden;">{items_confeti}</div>
        """, unsafe_allow_html=True)

    # D. LLUVIA DE EMOJIS (Feb, Nov, Sep)
    else:
        emoji = ""
        if "feb" in tema_actual or "amor" in tema_actual: emoji = "❤️"
        elif "noviembre" in tema_actual or "muertos" in tema_actual: emoji = "🌼"
        elif "septiembre" in tema_actual or "mexico" in tema_actual: emoji = "🇲🇽"
        
        if emoji:
            items_emoji = ""
            for _ in range(35):
                lp = random.randint(0, 100)
                dl = random.uniform(0, 8)
                dr = random.uniform(4, 10)
                sz = random.uniform(1.2, 2.5)
                items_emoji += f'<div class="emoji-v" style="left:{lp}%; animation-duration:{dr}s; animation-delay:{dl}s; font-size:{sz}rem;">{emoji}</div>'
                
            st.markdown(f"""
            <style>
                .emoji-v {{
                    position: fixed; top: -15vh; z-index: 0; pointer-events: none;
                    animation: fall-pure-v linear infinite; opacity: 0.7;
                }}
                @keyframes fall-pure-v {{
                    0% {{ top: -15vh; transform: rotate(0deg); }}
                    100% {{ top: 115vh; transform: rotate(360deg); }}
                }}
            </style>
            <div style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:0; overflow:hidden;">{items_emoji}</div>
            """, unsafe_allow_html=True)

def apply_theme():
    theme_file = load_active_theme_file()
    theme_data = get_theme_data(theme_file)
    if not theme_data:
        return
    
    # Ejecutar la Función Maestra de Estilo Visual (Reset Total Estático)
    configurar_estilo_visual(theme_file, theme_data)
    
    colors = theme_data.get('colores', {})
    progress = colors.get('barras_progreso', 'linear-gradient(90deg, #00FFC8, #D4AF37)')
    card = colors.get('tarjetas', '#1B1E23')

    theme_css = f"""
    <style>
        /* Estilos de Contenido Global */
        * {{ color: #FFFFFF !important; }}
        [data-testid="stSidebar"], .main, .block-container, p, span, h1, h2, h3, label, div {{
            color: #FFFFFF !important;
        }}
        .stProgress > div > div > div > div {{ background-image: {progress} !important; }}
        [data-testid="stSidebar"] {{ background-color: {card} !important; backdrop-filter: blur(15px); }}
        
        /* Dropdown Fix */
        div[data-baseweb="popover"] ul, div[data-baseweb="popover"] li {{
            background-color: #000000 !important; color: #FFFFFF !important;
        }}
    </style>
    """
    st.markdown(theme_css, unsafe_allow_html=True)

# Run theme application
apply_theme()

# Motivational Quotes
def get_motivational_quote():
    quotes = [
        "El éxito no es el final, el fracaso no es fatal: lo que cuenta es el valor para continuar.",
        "Tu actitud, no tu aptitud, determinará tu altitud.",
        "La excelencia no es un acto, sino un hábito.",
        "Vender es servir. Servir es ganar.",
        "No encuentres clientes para tus productos, encuentra productos para tus clientes.",
        "El 80% del éxito es aparecer.",
        "Donde hay una empresa de éxito, alguien tomó alguna vez una decisión valiente.",
        "La mejor forma de predecir el futuro es creándolo.",
        "El único lugar donde el éxito viene antes que el trabajo es en el diccionario."
    ]
    return random.choice(quotes)

# Helper Functions
def get_campaigns():
    exclude = ['assets', '.git', '__pycache__', '.pytest_cache']
    campaigns = [d for d in os.listdir(BASE_PATH) if os.path.isdir(os.path.join(BASE_PATH, d)) and d not in exclude and not d.startswith('.')]
    return sorted(campaigns)

def read_excel_data(folder_name):
    folder_path = os.path.join(BASE_PATH, folder_name)
    files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx') and not f.startswith('~$')]
    if not files:
        return None
    file_path = os.path.join(folder_path, files[0])
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        return None

@st.cache_data(ttl=600)  # Cache for 10 minutes
def get_all_advisors():
    campaigns = get_campaigns()
    all_names = set()
    for camp in campaigns:
        df = read_excel_data(camp)
        if df is not None and 'Asesor' in df.columns:
            names = df['Asesor'].dropna().unique()
            all_names.update(names)
    
    # Strict Sync & No Normalization Policy:
    # Use a set to aggregate all unique raw strings directly from the database
    advisor_list = list(all_names)
    
    # Manual surgical removal of the "corrected" version to keep ONLY the raw DB version
    # Target: "ANA LAURA CONTRERAS IÑIGUEZ" (The one with 'ñ' usually created by auto-correction)
    # Keeping: "ANA LAURA CONTRERAS IÐIGUEZ" (The raw DB version with the symbol)
    forbidden_version = "ANA LAURA CONTRERAS IÑIGUEZ"
    advisor_list = [name for name in advisor_list if name != forbidden_version]
    
    return sorted(advisor_list)

def get_progress_color(progress_pct):
    if progress_pct < 40:
        return "metric-red"
    elif progress_pct < 80:
        return "metric-warning"
    else:
        return "metric-green"

# Session State for Navigation
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'selected_advisor' not in st.session_state:
    st.session_state.selected_advisor = None
if 'selected_campaign' not in st.session_state:
    st.session_state.selected_campaign = None
if 'quote' not in st.session_state:
    st.session_state.quote = get_motivational_quote()
if 'admin_authenticated' not in st.session_state:
    st.session_state.admin_authenticated = False
if 'show_login' not in st.session_state:
    st.session_state.show_login = False

# --- SIDEBAR BRANDING ---
def show_sidebar():
    with st.sidebar:
        st.markdown('<div class="sidebar-logo-container">', unsafe_allow_html=True)
        if os.path.exists(COMPANY_LOGO):
            st.image(COMPANY_LOGO, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")
        if st.session_state.page in ['dashboard', 'campaign_selector']:
            if st.button("🏠 Volver al Inicio", use_container_width=True):
                st.session_state.page = 'welcome'
                st.session_state.selected_advisor = None
                st.session_state.selected_campaign = None
                st.session_state.quote = get_motivational_quote()
                st.rerun()
            
            if st.session_state.page == 'dashboard':
                if st.button("📂 Cambiar Campaña", use_container_width=True):
                    st.session_state.page = 'campaign_selector'
                    st.session_state.selected_campaign = None
                    st.rerun()
        
        # --- ADMIN MASTER PANEL ---
        st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
        if not st.session_state.admin_authenticated:
            if st.button("⚙️", key="admin_lock_btn", help="Acceso Administrador"):
                st.session_state.show_login = not st.session_state.show_login
                st.rerun()
                
            if st.session_state.show_login:
                pwd = st.text_input("🔒 Contraseña Admin:", type="password")
                if pwd == "Diego080303":
                    st.session_state.admin_authenticated = True
                    st.session_state.show_login = False
                    st.rerun()
                elif pwd != "" and pwd != "Diego080303":
                    st.error("Acceso denegado.")
        else:
            st.markdown("### 👑 Panel Maestro")
            # Scan themes folder
            if os.path.exists(THEMES_PATH):
                # Filter out obsolete/duplicate themes as requested
                excluded_themes = ['julio_verano.json', 'modo_febrero.json', 'modo_mayo.json']
                themes = sorted([
                    f for f in os.listdir(THEMES_PATH) 
                    if f.endswith('.json') and f not in excluded_themes
                ])
                current_active = load_active_theme_file()
                
                # Create friendly labels
                theme_options = {t: get_theme_data(t)['nombre'] if get_theme_data(t) else t for t in themes}
                
                selected_theme_file = st.selectbox(
                    "Configuración Visual Global:", 
                    options=themes, 
                    format_func=lambda x: theme_options.get(x, x),
                    index=themes.index(current_active) if current_active in themes else 0
                )
                
                if selected_theme_file != current_active:
                    with open(ACTIVE_THEME_FILE, 'w') as f:
                        f.write(selected_theme_file)
                    st.success("Configuración aplicada.")
                    st.rerun()
            
            if st.button("🚪 Cerrar Sesión Admin", use_container_width=True):
                st.session_state.admin_authenticated = False
                st.rerun()

# --- PAGE 1: WELCOME ---
def show_welcome():
    theme_file = load_active_theme_file()
    theme_data = get_theme_data(theme_file)
    home_config = theme_data.get('config_home', {}) if theme_data else {}
    accent_color = theme_data.get('colores', {}).get('acentos', '#00FFC8') if theme_data else '#00FFC8'
    title_color = theme_data.get('colores', {}).get('texto_titulos', '#a0a0a0') if theme_data else '#a0a0a0'
    
    st.markdown('<div class="welcome-container">', unsafe_allow_html=True)
    
    # Seasonal Theme Banner
    try:
        if os.path.exists(THEME_BANNER):
            st.image(THEME_BANNER, use_container_width=True, caption="")
    except:
        pass

    # Thematic Logo Row with Dynamic Accessories
    logo_base64 = get_base64_image(COMPANY_LOGO)
    efecto = theme_data.get('efecto', '')
    theme_id = theme_data.get('id', '')
    
    logo_accessory_html = ""
    # April Accessory: Colorful Pinwheel (Rehilete)
    if efecto == 'confeti':
        logo_accessory_html = f'''
<div style="position: absolute; top: -15px; left: 10px; transform: rotate(-5deg); z-index: 10;">
<svg width="60" height="60" viewBox="0 0 100 100" style="animation: spin 3s linear infinite;">
<path d="M50 50 L50 10 A40 40 0 0 1 90 50 Z" fill="#FF5733" />
<path d="M50 50 L90 50 A40 40 0 0 1 50 90 Z" fill="#00FFC8" />
<path d="M50 50 L50 90 A40 40 0 0 1 10 50 Z" fill="#FFD700" />
<path d="M50 50 L10 50 A40 40 0 0 1 50 10 Z" fill="#00BFFF" />
<circle cx="50" cy="50" r="5" fill="#fff" />
</svg>
<div style="width: 3px; height: 35px; background: #ddd; margin-left: 28px; border-radius: 2px;"></div>
</div>'''
    # May Accessory: Elegant Flower (Orchid style)
    elif theme_id == 'mayo':
        logo_accessory_html = f'''
<div style="position: absolute; top: -10px; left: 5px; z-index: 10; transform: rotate(-10deg);">
<svg width="60" height="60" viewBox="0 0 100 100">
    <!-- Minimalist Flower Petals -->
    <path d="M50 50 Q30 20 50 5 Q70 20 50 50" fill="#FFFFFF" stroke="#967BB6" stroke-width="1" />
    <path d="M50 50 Q10 40 5 60 Q20 70 50 50" fill="#F8F4FF" stroke="#967BB6" stroke-width="1" />
    <path d="M50 50 Q90 40 95 60 Q80 70 50 50" fill="#F8F4FF" stroke="#967BB6" stroke-width="1" />
    <circle cx="50" cy="45" r="6" fill="#967BB6" opacity="0.8" />
</svg>
</div>'''
    # June Accessory: None (Clean original logo)
    elif theme_id == 'junio':
        logo_accessory_html = ""
    # Diciembre Accessory: Winter Glow / Stellar
    elif theme_id == 'diciembre_navidad':
        logo_accessory_html = f'''
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; filter: drop-shadow(0 0 15px rgba(255,255,255,0.4)); z-index: -1;"></div>
'''
    # Diciembre Accessory: Nevada Fija / Real
    elif 'diciembre' in theme_id:
        logo_accessory_html = f'''
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; filter: drop-shadow(0 0 15px rgba(255,255,255,0.4)); z-index: -1;"></div>
'''
    # Noviembre Accessory: Cempasúchil Glow / Candlelight
    elif theme_id == 'noviembre_ofrenda':
        logo_accessory_html = f'''
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; filter: drop-shadow(0 0 20px #FF8C00); z-index: -1; opacity: 0.6;"></div>
'''
    # Septiembre Accessory: Tricolor Confetti / Celebration
    elif theme_id == 'septiembre_patrio':
        logo_accessory_html = f'''
<div style="position: absolute; top: -10px; right: 20px; z-index: 10;">
<svg width="60" height="60" viewBox="0 0 100 100">
    <!-- Mexican Tricolor Confetti -->
    <circle cx="20" cy="20" r="4" fill="#059669" style="animation: pulse-glint 2s infinite;" />
    <circle cx="80" cy="30" r="5" fill="#DC2626" style="animation: pulse-glint 3s infinite;" />
    <circle cx="50" cy="10" r="3" fill="#FFFFFF" style="animation: pulse-glint 2.5s infinite;" />
    <path d="M45 45 L55 55 M55 45 L45 55" stroke="#FFFFFF" stroke-width="2" opacity="0.6" />
</svg>
</div>'''
    # July Accessory: Removed (Clean original logo)
    elif theme_id == 'julio' or theme_id == 'julio_verano_sol':
        logo_accessory_html = ""

    # Ensure logo area is perfectly transparent and at the front
    st.markdown(f'''
<div style="display: flex; justify-content: center; align-items: center; margin-bottom: 25px; background: transparent; position: relative; z-index: 100;">
<div style="position: relative; display: inline-block; width: 450px; background: transparent;">
<img src="data:image/png;base64,{logo_base64}" style="width: 100%; height: auto; display: block; object-fit: contain; background: transparent;">
{logo_accessory_html}
</div>
</div>
''', unsafe_allow_html=True)
    
    # 1. Fixed Main Title
    st.markdown(f"<h2 style='text-align: center; color: {title_color}; margin-top: 10px;'>Bienvenido al Portal de Seguimiento de Campañas</h2>", unsafe_allow_html=True)
    
    # 2. Dynamic Selector for Personalized Greeting
    advisors = get_all_advisors()
    selected_name = None
    
    if advisors:
        # Centering the selectbox using columns for a cleaner delivery
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            selected_name = st.selectbox(
                "Encuentra tu nombre en la lista:", 
                advisors, 
                index=None, 
                placeholder="Selecciona un asesor...",
                key="welcome_advisor_select",
                label_visibility="collapsed" # Added to reduce bulk/boxes
            )
    
    # 3. Personalized Dynamic Greeting
    greeting = f"¡Hola, {selected_name}! 👋" if selected_name else "¡Hola! 👋"
    welcome_sub = home_config.get('subtitulo', "Tu camino hacia el éxito financiero comienza aquí.")
    welcome_icon = home_config.get('icono', "🚀")
    
    st.markdown(f"""
    <div class="title-container">
        <h1 style='color: {accent_color} !important;'>{greeting}</h1>
        <p style='color: #a0a0a0; font-size: 1.2rem; margin-top: -10px;'>{welcome_icon} {welcome_sub}</p>
        <h3 style='text-align: center;'>"{st.session_state.quote}"</h3>
    </div>
    """, unsafe_allow_html=True)

    # 3. Centro de Avisos Inteligente (Fijos + Dinámicos)
    # A. Avisos FIJOS (Metas Anuales)
    avisos_fijos = [
        "🛡️ <b>Legión Centurión:</b> Premia tu consistencia. ¡Llega a las 48 pólizas y conviértete en leyenda!",
        "🏆 <b>Meta MDRT:</b> La meta es de $1,810,400 PA. ¡Cada póliza cuenta!",
        "🎓 <b>Graduación:</b> Las metas de Normal (36) y Honor (48) siguen vigentes."
    ]

    # B. Avisos DINÁMICOS (Relacionados con Mes/Carrera)
    avisos_mensuales = []
    if "abril" in theme_file or "nino" in theme_file:
        avisos_mensuales = [
            "🧸 <b>Mes del Niño:</b> Recuérdales a los padres que la mejor herencia es la educación garantizada.",
            "🚀 Protege el futuro de los pequeños gigantes."
        ]
    elif "diciembre" in theme_file or "navidad" in theme_file:
        avisos_mensuales = [
            "🎄 <b>Cierre Anual:</b> El mejor regalo para una familia es una póliza entregada.",
            "❄️ Que el espíritu navideño te impulse a cerrar tu meta anual con fuerza."
        ]
    elif "julio" in theme_file or "verano" in theme_file:
        avisos_mensuales = [
            "☀️ <b>Mitad de Año:</b> Es el momento perfecto para revisar tu proyección y ajustar velas.",
            "🏖️ Mientras tus clientes descansan, tú aseguras su tranquilidad."
        ]
    elif "septiembre" in theme_file or "mexico" in theme_file:
        avisos_mensuales = ["🇲🇽 <b>Mes Patrio:</b> Celebra protegiendo el patrimonio de las familias mexicanas."]
    elif "noviembre" in theme_file or "muertos" in theme_file:
        avisos_mensuales = ["🕯️ <b>Trascendencia:</b> Nuestra labor es asegurar que el amor perdure más allá de la vida."]
    else:
        # Default
        avisos_mensuales = ["⚡ ¡Es un excelente mes para romper tus récords!"]

    # C. Lógica de Fusión Inteligente (Novedad primero)
    lista_final = avisos_mensuales + avisos_fijos
    avisos_html = "".join([f"<li style='margin-bottom: 8px;'>{aviso}</li>" for aviso in lista_final])

    st.markdown(f"""
    <div style='background: rgba(255,255,255,0.05); padding: 20px; border-radius: 12px; border-left: 5px solid {accent_color}; margin-bottom: 25px;'>
        <h4 style='margin-top: 0; color: {accent_color}; font-weight: 800;'>📢 Centro de Avisos de la Promotoría</h4>
        <ul style='list-style-type: none; padding-left: 0; margin-bottom: 0;'>
            {avisos_html}
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # 4. Action Button
    if selected_name:
        if st.button("Ver mis Resultados", use_container_width=True):
            st.session_state.selected_advisor = selected_name
            st.session_state.page = 'campaign_selector'
            st.rerun()
    elif not advisors:
        st.error("No se pudo cargar la lista de asesores. Verifica que existan archivos Excel en las carpetas de campaña.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 1.5: CAMPAIGN SELECTOR ---
def show_campaign_selector():
    show_sidebar()
    st.markdown('<div class="welcome-container">', unsafe_allow_html=True)
    st.markdown(f"## Hola, {st.session_state.selected_advisor}")
    st.markdown("### Selecciona la campaña que deseas consultar:")
    
    # Sort campaigns to ensure symmetrical Legion/MDRT/Convenciones order
    available = get_campaigns()
    # Ordered display as requested
    order = ["legion centurion", "mdrt", "convenciones", "camino cumbre", "graduacion"]
    display_campaign_names = [c for c in order if c in [ac.lower().replace('_', ' ') for ac in available]]
    
    # helper to find original directory name from display name
    def find_original_dir(display_name):
        return next(ac for ac in available if ac.lower().replace('_', ' ') == display_name.lower())

    cols = st.columns(len(display_campaign_names) if display_campaign_names else 1)
    for i, camp_display in enumerate(display_campaign_names):
        original_dir = find_original_dir(camp_display)
        with cols[i]:
            st.markdown('<div class="selector-item">', unsafe_allow_html=True)
            
            # Mapeo de rutas exactas solicitado por el usuario
            logo_mapping = {
                "legion_centurion": "assets/logos/campanas/legion_centurion.png",
                "mdrt": "assets/logos/campanas/mdrt_logo.png",
                "convenciones": "assets/logos/campanas/convenciones.png",
                "camino_cumbre": "assets/logos/campanas/camino_cumbre.png",
                "graduacion": "assets/logos/campanas/graduacion.png"
            }
            logo_path = logo_mapping.get(original_dir)
            
            if logo_path and os.path.exists(logo_path):
                st.image(logo_path, width=250) 
            else:
                st.markdown(f"<h3 style='text-align:center;'>{camp_display.upper()}</h3>", unsafe_allow_html=True)
            
            btn_label = f"ENTRAR A {camp_display.upper()}"
            if st.button(btn_label, key=f"btn_{original_dir}", use_container_width=True):
                st.session_state.selected_campaign = original_dir
                st.session_state.page = 'dashboard'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 2: DASHBOARD ---
def show_dashboard():
    show_sidebar()
    
    campaign = st.session_state.selected_campaign
    df = read_excel_data(campaign)
    
    if df is None:
        st.error(f"No se pudo cargar la información de la campaña {campaign}.")
        return

    if 'Asesor' not in df.columns:
        st.error("El archivo de la campaña no contiene la columna 'Asesor'.")
        return
        
    advisor_data = df[df['Asesor'] == st.session_state.selected_advisor]
    if advisor_data.empty:
        st.info(f"### ℹ️ Información\nEste asesor no participa en esta campaña ({campaign.upper().replace('_', ' ')}).")
        return
    
    row = advisor_data.iloc[0]
    fecha = row.get('Fecha_Corte', 'No disponible')
    # Definitive Patch: Ensuring module-level access and NaT checks
    if pd.notna(fecha) and isinstance(fecha, (pd.Timestamp, date, datetime)):
        fecha_corte = fecha.strftime('%d/%m/%Y')
    else:
        fecha_corte = "No disponible"

    # Campaign Logo and Title
    col_logo, col_title = st.columns([1, 4])
    logo_file = os.path.join(LOGOS_PATH, f"{campaign}.png")
    if not os.path.exists(logo_file):
         logo_file = os.path.join(LOGOS_PATH, f"{campaign}_logo.png")
    
    with col_logo:
        if os.path.exists(logo_file):
            width = 450 if campaign.lower().replace('_', ' ') == 'legion centurion' else 300
            st.image(logo_file, width=width)
        else:
            header_text = campaign.upper().replace('_', ' ')
            st.markdown(f"<h2 style='color:#00ff88'>{header_text}</h2>", unsafe_allow_html=True)
    
    with col_title:
        st.markdown(f"# Campaña: {campaign.upper().replace('_', ' ')}")
        # Global Dynamic Cut-off Date
        if fecha_corte and fecha_corte != 'No disponible':
            st.markdown(f"<p style='color: #a0a0a0; font-size: 1rem; margin-top: -10px;'>📅 Datos actualizados al corte del: <b>{fecha_corte}</b></p>", unsafe_allow_html=True)
            
        if campaign.lower().replace(' ', '_') == 'mdrt':
            st.info("La Million Dollar Round Table (MDRT) es el estándar de oro en seguros. Esta gráfica mide tu camino hacia la membresía de élite mundial.")
        elif campaign.lower().replace(' ', '_') == 'legion_centurion':
            st.info("Legión Centurión premia tu consistencia y volumen de pólizas. ¡Llega a las 48 y conviértete en una leyenda!")
        elif campaign.lower().replace(' ', '_') == 'convenciones':
            st.markdown(f"<p style='color: #00ff88; font-size: 1.2rem; font-weight: 700; background: rgba(0,255,136,0.1); padding: 10px; border-radius: 10px;'>Dato importante: Para clasificar a convenciones necesitamos un mínimo de 30 pólizas y un mínimo de $588,500 de comisiones.</p>", unsafe_allow_html=True)
        elif campaign.lower().replace(' ', '_') == 'camino_cumbre':
            st.info("Camino a la Cumbre es un programa de 18 meses diseñado para potenciar tu arranque y consolidar tu carrera. ¡Escala hacia la excelencia!")
        elif campaign.lower().replace(' ', '_') == 'graduacion':
            st.info("Campaña de Graduación: El reconocimiento a tu primer año de éxito. Alcanza la meta y celebra tu inicio profesional con honores.")

    # --- MDRT LAYOUT ---
    if campaign.lower().replace(' ', '_') == 'mdrt':
        goal = 1810400
        pa_acumulada = row.get('PA_Acumulada', 0)
        pa_faltante = row.get('PA_Faltante_Miembro', 0)
        mes_actual = row.get('Mes_Actual', 1)
        progress_pct = (pa_acumulada / goal) * 100
        progress_color_class = get_progress_color(progress_pct)
        
        st.divider()
        
        # Monthly meta calculation (Using Excel month for precise math)
        meses_restantes = max(1, 12 - int(mes_actual) + 1)
        meta_mensual = pa_faltante / meses_restantes if pa_faltante > 0 else 0
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown('<div class="metric-neutral">', unsafe_allow_html=True)
            st.metric("Meta MDRT", f"${goal:,.0f}")
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="{progress_color_class}">', unsafe_allow_html=True)
            st.metric("Prima Anualizada Acumulada", f"${pa_acumulada:,.2f}")
            st.markdown('</div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="metric-neutral">', unsafe_allow_html=True)
            # Security Shield for Faltante
            if pa_faltante <= 0:
                st.metric("Prima Anualizada Faltante", "$0.00", help="¡Meta MDRT lograda! 🎉")
            else:
                st.metric("Prima Anualizada Faltante", f"${pa_faltante:,.2f}")
            st.markdown('</div>', unsafe_allow_html=True)
        with c4:
            st.markdown('<div class="metric-neutral">', unsafe_allow_html=True)
            st.metric("Promedio Mensual Necesario", f"${meta_mensual:,.2f}", help=f"Para cumplir la meta a Diciembre, considerando que estamos en el mes {mes_actual}.")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")
        indicator_pos = max(5, min(progress_pct, 95))
        st.markdown(f"""
            <div class="green-bar">
                <div class="progress-label-container">
                    <span>Tu Avance Financiero (Prima Anualizada)</span>
                </div>
                <div class="progress-value-floating">
                    <div class="progress-indicator-text" style="left: {indicator_pos}%;">${pa_acumulada:,.2f}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        progress_val = min(float(pa_acumulada / goal), 1.0) if goal > 0 else 0.0
        st.progress(progress_val)
        
        status_txt = "¡Meta Lograda! 🎉" if pa_acumulada >= goal else f"Falta: ${max(0, goal - pa_acumulada):,.2f}"
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; font-size: 0.9em; margin-top: -10px;">
                <span>$0</span>
                <span style="font-weight: bold;">{status_txt}</span>
                <span>Meta: ${goal:,.0f}</span>
            </div>
        ''', unsafe_allow_html=True)
        
        # Time Progress
        time_progress = min(mes_actual / 12, 1.0)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="progress-label-container"><span>Tu Avance en el Tiempo</span></div>', unsafe_allow_html=True)
        st.progress(float(time_progress) if pd.notna(time_progress) else 0.0)
        
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; font-size: 0.9em; margin-top: -10px;">
                <span>Mes 0</span>
                <span style="font-weight: bold; color: #00ff88;">Mes {mes_actual} de 12 ({time_progress*100:.0f}%)</span>
                <span>Cierre</span>
            </div>
        ''', unsafe_allow_html=True)

    # --- LEGION CENTURION LAYOUT ---
    elif campaign.lower().replace(' ', '_') == 'legion_centurion':
        total_polizas = row.get('Total_Polizas', 0)
        promedio = row.get('Promedio_Mensual', 0)
        va_en_meta = str(row.get('Va_En_Meta', '')).upper()
        mes_actual = row.get('Mes_Actual', 1)
        
        meta_polizas = 48
        faltante_meta = max(0, meta_polizas - total_polizas)
        progress_pct = (total_polizas / meta_polizas) * 100
        
        # dynamic border class
        meta_class = "border-neon-green" if "EN META" in va_en_meta else "border-bright-red"
        
        st.divider()
        # BLOQUE 1: Información Importante (3 MAIN CARDS ONLY)
        st.markdown("### Información Importante")
        st.markdown(f'<div class="centurion-main-block {meta_class}-container">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Total Pólizas", f"{total_polizas:,.1f}")
        with c2:
            st.metric("Promedio Mensual", f"{promedio:,.2f}")
        with c3:
            st.metric("Va En Meta", va_en_meta)
        st.markdown('</div>', unsafe_allow_html=True)

        # BLOQUE 2: Faltantes para Siguiente Nivel (4 LEVEL CARDS ONLY)
        st.markdown('<div class="centurion-levels-grid">', unsafe_allow_html=True)
        st.markdown("### ¿Cuánto me hace falta para mi siguiente nivel?")
        l1, l2, l3, l4 = st.columns(4)
        levels = [('BRONCE', 'Bronce'), ('PLATA', 'Plata'), ('ORO', 'Oro'), ('PLATINO', 'Platino')]
        for i, (label, col_name) in enumerate(levels):
            val = row.get(col_name, 0)
            with [l1, l2, l3, l4][i]:
                st.metric(label, f"{val:,.1f}")
        st.markdown('</div>', unsafe_allow_html=True)

        # --- PROGRESS BARS ---
        st.divider()
        # Policy Progress Bar (Cyan)
        indicator_pos = max(5, min(progress_pct, 95))
        st.markdown(f"""
            <div class="cyan-bar">
                <div class="progress-label-container">
                    <span>Tu Avance en Pólizas</span>
                </div>
                <div class="progress-value-floating">
                    <div class="progress-indicator-text" style="left: {indicator_pos}%; color: #00f2ff;">{total_polizas:,.1f} Pólizas</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        # Security Shield: min(val, 1.0)
        prog_val = min(float(total_polizas / meta_polizas), 1.0) if meta_polizas > 0 else 0.0
        st.progress(prog_val)
        
        status_txt = "¡Meta Lograda! 🎉" if total_polizas >= meta_polizas else f"Faltan: {max(0, meta_polizas - total_polizas):,.1f}"
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; font-size: 0.9em; margin-top: -10px;">
                <span>0</span>
                <span style="font-weight: bold;">{status_txt}</span>
                <span>Meta: {meta_polizas}</span>
            </div>
        ''', unsafe_allow_html=True)

        # Time Progress (shared style)
        time_progress = min(mes_actual / 12, 1.0)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="progress-label-container"><span>Tu Avance en el Tiempo</span></div>', unsafe_allow_html=True)
        st.progress(float(time_progress) if pd.notna(time_progress) else 0.0)
        
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; font-size: 0.9em; margin-top: -10px;">
                <span>Mes 0</span>
                <span style="font-weight: bold; color: #00ff88;">Mes {mes_actual} de 12 ({time_progress*100:.0f}%)</span>
                <span>Cierre</span>
            </div>
        ''', unsafe_allow_html=True)

    # --- CONVENCIONES LAYOUT ---
    elif campaign.lower().replace(' ', '_') == 'convenciones':
        # Mapeo de Columnas (User specified)
        comision_vida = pd.to_numeric(row.get('Comision_Vida', 0), errors='coerce')
        if pd.isna(comision_vida): comision_vida = 0
        
        rda = pd.to_numeric(row.get('RDA', 0), errors='coerce')
        if pd.isna(rda): rda = 0
        
        # Cálculo de Totales: Siempre suma Comision_Vida + RDA
        comisiones_totales = comision_vida + rda
            
        polizas = pd.to_numeric(row.get('Polizas', 0), errors='coerce')
        if pd.isna(polizas): polizas = 0
        
        lugar = pd.to_numeric(row.get('Lugar', 0), errors='coerce')
        if pd.isna(lugar): lugar = 0
        
        # Logic for Estatus Viaje
        is_qualified = (lugar <= 480 and polizas >= 30 and comisiones_totales >= 588500)
        estatus_viaje = "✅ DENTRO DE RANGO" if is_qualified else "❌ POR CALIFICAR"
        status_class = "border-neon-green" if is_qualified else "border-bright-red"
        
        st.divider()
        # BLOQUE 1: Información Importante (6 CARDS)
        st.markdown("### Información Importante")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="metric-neutral">', unsafe_allow_html=True)
            st.metric("Créditos Vida", f"${comision_vida:,.2f}")
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="metric-neutral">', unsafe_allow_html=True)
            st.metric("RDA", f"${rda:,.2f}")
            st.markdown('</div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="metric-green">', unsafe_allow_html=True)
            st.metric("Créditos Totales", f"${comisiones_totales:,.2f}")
            st.markdown('</div>', unsafe_allow_html=True)
            
        c4, c5, c6 = st.columns(3)
        with c4:
            st.markdown('<div class="metric-neutral">', unsafe_allow_html=True)
            st.metric("Pólizas", f"{polizas:,.0f}")
            st.markdown('</div>', unsafe_allow_html=True)
        with c5:
            st.markdown('<div class="metric-neutral">', unsafe_allow_html=True)
            st.metric("Lugar", f"#{lugar:,.0f}")
            st.markdown('</div>', unsafe_allow_html=True)
        with c6:
            st.markdown(f'<div class="{status_class}">', unsafe_allow_html=True)
            st.metric("Estatus Viaje", estatus_viaje)
            st.markdown('</div>', unsafe_allow_html=True)

        # BLOQUE 2: Referencia de Cortes
        st.markdown("### ¿Cuánto tiene el último lugar?")
        r1, r2, r3, r4 = st.columns(4)
        targets = [
            ("Lugar_480", "1 Diamante (Lugar 480)", r1),
            ("Lugar_228", "2 Diamantes (Lugar 228)", r2),
            ("Lugar_108", "3 Diamantes (Lugar 108)", r3),
            ("Lugar_28", "Gran Diamante (Lugar 28)", r4)
        ]
        
        target_vals = {}
        for col, label, col_obj in targets:
            val = pd.to_numeric(row.get(col, 0), errors='coerce')
            if pd.isna(val): val = 0
            target_vals[col] = val
            with col_obj:
                st.markdown('<div class="metric-neutral-med">', unsafe_allow_html=True)
                st.metric(label, f"${val:,.2f}")
                st.markdown('</div>', unsafe_allow_html=True)

        # BLOQUE 3: Dashboards de Persecución
        st.divider()
        st.markdown("### Dashboards de Persecución")
        
        p_titles = [
            "Persecución: 1 Diamante (Cancún)",
            "Persecución: 2 Diamantes (Costa Rica)",
            "Persecución: 3 Diamantes (París)",
            "Persecución: Gran Diamante (Amalfi)"
        ]
        p_cols = ["Lugar_480", "Lugar_228", "Lugar_108", "Lugar_28"]
        
        for i in range(4):
            target = target_vals.get(p_cols[i], 1)
            progress = min(comisiones_totales / target, 1.0) if target > 0 else 0
            st.markdown(f"#### {p_titles[i]}")
            st.progress(float(progress) if pd.notna(progress) else 0.0)
            faltante_val = max(0, target - comisiones_totales)
            txt_faltante = "¡Meta Lograda! 🎉" if faltante_val <= 0 else f"Faltante: ${faltante_val:,.2f}"
            
            st.markdown(f'''
                <div style="display: flex; justify-content: space-between; font-size: 0.9em; margin-top: -10px;">
                    <span>$0</span>
                    <span style="font-weight: bold; color: #00ff88;">{txt_faltante}</span>
                    <span>Meta: ${target:,.0f}</span>
                </div>
            ''', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

        # BLOQUE 4: Sección de Destinos (Centrado y Orden Correcto)
        st.divider()
        st.markdown("<h3 style='text-align: center;'>¿Sabes cuáles son los destinos?</h3>", unsafe_allow_html=True)
        d1, d2, d3, d4 = st.columns(4)
        destinos = [
            ("Cancún (1 Diamante)", "cancun.jpeg", d1),
            ("Costa Rica (2 Diamantes)", "costa_rica.jpeg", d2),
            ("París (3 Diamantes)", "paris.jpeg", d3),
            ("Amalfitana (Gran Diamante)", "amalfi.jpeg", d4)
        ]
        for label, img_name, col_obj in destinos:
            img_path = os.path.join(ASSETS_PATH, "destinos", img_name)
            with col_obj:
                st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                    st.markdown(f"<p style='font-weight: bold;'>{label}</p>", unsafe_allow_html=True)
                else:
                    st.warning(f"{label} (Imagen no encontrada)")
                st.markdown('</div>', unsafe_allow_html=True)

    # --- CAMINO A LA CUMBRE LAYOUT ---
    elif campaign.lower().replace(' ', '_') == 'camino_cumbre':
        mes_asesor = int(row.get('Mes_Asesor', 1))
        polizas_totales = row.get('Polizas_Totales', 0)
        estatus_meta_orig = str(row.get('Estatus_meta', '')).upper()
        trimestre = row.get('Trimestre', 1)
        fecha_con = row.get('Fecha_Conexion', 'N/A')
        
        # Extract and format target date
        fecha_limite = row.get('Limite_Logro_Meta', row.get('Fecha Limite', row.get('Vencimiento', 'No disponible')))
        if pd.notna(fecha_limite) and isinstance(fecha_limite, (pd.Timestamp, date, datetime)):
            fecha_limite_fmt = fecha_limite.strftime('%d/%m/%Y')
        else:
            fecha_limite_fmt = str(fecha_limite)
        
        # Auditoría de Inicio (Mes 1, 2 o 3)
        alert_mode = False
        if mes_asesor in [1, 2, 3]:
            prod_col = f"Mes_{mes_asesor}_Prod"
            produccion_mes = row.get(prod_col, 0)
            if produccion_mes == 0:
                estatus_meta = "⚠️ ALERTA: MES SIN ACTIVIDAD (Riesgo de Descalificación)"
                status_class = "border-orange"
                alert_mode = True
            else:
                estatus_meta = estatus_meta_orig
                status_class = "border-neon-green" if "EN META" in estatus_meta else "border-bright-red"
        else:
            estatus_meta = estatus_meta_orig
            status_class = "border-neon-green" if "EN META" in estatus_meta else "border-bright-red"
            
        # Formatting date
        if isinstance(fecha_con, (date, datetime, pd.Timestamp)):
            if pd.notna(fecha_con) and isinstance(fecha_con, (pd.Timestamp, date, datetime)):
                fecha_con = fecha_con.strftime('%d/%m/%Y')
            else:
                fecha_con = "No disponible"
        
        meta_acumulada = mes_asesor * 4
        progress_pct = min(polizas_totales / meta_acumulada, 1.0) if meta_acumulada > 0 else 0
        
        st.divider()
        col_main, col_donut = st.columns([3, 1])
        
        with col_main:
            st.markdown("### Información Importante")
            # Use specific container class for alert or standard status
            container_css = "border-orange-container" if alert_mode else f"{status_class}-container"
            st.markdown(f'<div class="cumbre-main-block {container_css}">', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Pólizas Totales", f"{polizas_totales:,.1f}")
            with c2:
                # Use standard metric but the container border controlled by alert logic
                st.metric("Estatus Actual", estatus_meta)
            with c3:
                st.metric("Trimestre Actual", f"{trimestre}")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col_donut:
            # Donut Chart for Time (Metallic Cyan Theme)
            fig = go.Figure(go.Pie(
                values=[mes_asesor, max(0, 18 - mes_asesor)],
                labels=['Mes Actual', 'Meses Restantes'],
                hole=.7,
                marker_colors=['#00f2ff', 'rgba(255, 255, 255, 0.1)'],
                showlegend=False,
                textinfo='none'
            ))
            fig.update_layout(
                annotations=[dict(text=f'Mes {mes_asesor}<br>de 18', x=0.5, y=0.5, font_size=20, font_color="white", showarrow=False)],
                margin=dict(t=0, b=0, l=10, r=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                height=250
            )
            st.plotly_chart(fig, use_container_width=True)

        # --- PROGRESS BARS ---
        st.divider()
        st.markdown(f"#### Dashboard de Meta Mensual")
        st.markdown(f"<p style='color: #0088ff; font-weight: bold; background: rgba(0,136,255,0.1); padding: 10px; border-radius: 8px;'>Tu meta acumulada al mes {mes_asesor} es de {meta_acumulada} pólizas</p>", unsafe_allow_html=True)
        
        st.markdown('<div class="azul-cumbre-bar">', unsafe_allow_html=True)
        # Security Shield: min(val, 1.0)
        prog_shield = min(float(progress_pct), 1.0) if pd.notna(progress_pct) else 0.0
        st.progress(prog_shield)
        
        status_txt = "¡Meta Lograda! 🎉" if polizas_totales >= meta_acumulada else f"Avance: {polizas_totales:,.1f} de {meta_acumulada}"
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; font-size: 0.9em; margin-top: -10px;">
                <span>0</span>
                <span style="font-weight: bold; color: #00f2ff;">{status_txt} ({progress_pct*100:.1f}%)</span>
                <span>Meta: {meta_acumulada}</span>
            </div>
        ''', unsafe_allow_html=True)

        # --- LEGAL FOOTER ---
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.divider()
        st.markdown("""
        <div style='background: rgba(255,255,255,0.05); padding: 20px; border-radius: 12px; border-left: 4px solid #00f2ff;'>
            <h4 style='color: #00f2ff; margin-top: 0;'>Reglas de Continuidad Operativa</h4>
            <p style='font-size: 0.9rem; color: #d0d0d0;'>
                <b>Continuidad del programa:</b> Todo asesor participante debe mantener actividad constante. 
                Cerrar el primer trimestre con producción nula (0 pólizas) implica la baja automática del programa Camino a la Cumbre.
            </p>
            <p style='font-size: 0.9rem; color: #d0d0d0;'>
                <b>Ventanas de Recuperación:</b> El programa contempla dos cortes estratégicos de recuperación en el <b>Mes 9</b> y el <b>Mes 18</b>. 
                Estos son los únicos periodos donde se permite regularizar el estatus para continuar hacia la cumbre de excelencia.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # --- GRADUACIÓN LAYOUT ---
    elif campaign.lower().replace(' ', '_') == 'graduacion':
        mes_asesor = int(row.get('Mes_Asesor', 1))
        polizas_totales = row.get('Polizas_Totales', 0)
        comisiones = pd.to_numeric(row.get('Comisones', 0), errors='coerce')
        if pd.isna(comisiones): comisiones = 0
        produccion_mes = row.get('Produccion_Mes', row.get('Polizas_Mes', 0)) # fallback check
        
        # Extract and format target date
        fecha_limite = row.get('Limite_Logro_Meta', 'No disponible')
        if pd.notna(fecha_limite) and isinstance(fecha_limite, (pd.Timestamp, date, datetime)):
            fecha_limite_fmt = fecha_limite.strftime('%d/%m/%Y')
        else:
            fecha_limite_fmt = str(fecha_limite)
        
        # 1. Logic for Corte and Events
        # Calculate when month 12 falls based on current month and date
        current_date = date.today()
        # Month 12 is (12 - mes_asesor) months away
        months_to_12 = 12 - mes_asesor
        mes_12_month = (current_date.month + months_to_12 - 1) % 12 + 1
        
        if mes_12_month in [12, 1, 2, 3, 4, 5]:
            corte_nombre = "MAYO"
            evento_nombre = "AGOSTO"
            corte_month_int = 5
        else:
            corte_nombre = "NOVIEMBRE"
            evento_nombre = "FEBRERO"
            corte_month_int = 11

        # 2. Maintenance Logic (Post-Mes 12)
        maintenance_alert = False
        is_maintenance_phase = (mes_asesor > 12)
        
        # Check if Mes 12 was before the cut month
        # This is a bit complex without the exact mes_12 year, but we'll use the logic:
        # If we are in maintenance and the current month is NOT the cut month
        if is_maintenance_phase and current_date.month != corte_month_int:
            # We assume the user hit the meta if they are in maintenance phase 
            # and looking for the event. If production is 0, alert.
            if produccion_mes == 0:
                maintenance_alert = True

        st.divider()
        col_main, col_time = st.columns([3, 1])
        
        with col_main:
            st.markdown("### Información Importante")
            
            # Dynamic Info Based on Phase
            if mes_asesor <= 12:
                # CAREER PHASE: Focus on production
                c1, c2, lmf = st.columns(3)
                with c1:
                    st.markdown(f'<div class="metric-gold">', unsafe_allow_html=True)
                    st.metric("Pólizas Totales", f"{polizas_totales:,.1f}")
                    st.markdown('</div>', unsafe_allow_html=True)
                with c2:
                    st.markdown(f'<div class="metric-gold">', unsafe_allow_html=True)
                    st.metric("Comisiones Acumuladas", f"${comisiones:,.2f}")
                    st.markdown('</div>', unsafe_allow_html=True)
                with lmf:
                    st.markdown(f'<div class="metric-gold">', unsafe_allow_html=True)
                    st.metric("Fecha Límite de Meta", fecha_limite_fmt)
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                # MAINTENANCE PHASE: Show event info
                st.markdown("#### 🕒 Fase de Mantenimiento: Camino a tu Evento")
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.markdown(f'<div class="metric-gold">', unsafe_allow_html=True)
                    st.metric("Pólizas Totales", f"{polizas_totales:,.1f}")
                    st.markdown('</div>', unsafe_allow_html=True)
                with c2:
                    st.markdown(f'<div class="metric-gold">', unsafe_allow_html=True)
                    st.metric("Comisiones Acumuladas", f"${comisiones:,.2f}")
                    st.markdown('</div>', unsafe_allow_html=True)
                with c3:
                    st.markdown(f'<div class="metric-gold">', unsafe_allow_html=True)
                    st.metric("Corte", corte_nombre)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown(f'<div class="metric-gold" style="margin-top: 10px; padding: 10px; text-align: center; border-radius: 10px;">', unsafe_allow_html=True)
                st.markdown(f"**Evento de Graduación:** {evento_nombre}", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Maintenance Alert (Red Blinking)
                if maintenance_alert:
                    st.markdown("""
                    <div class="blinking-alert">
                        ⚠️ REGLA DE MANTENIMIENTO: No puedes cerrar este mes en 0 pólizas o perderás tu lugar en el evento.
                    </div>
                    """, unsafe_allow_html=True)
        
        with col_time:
            # Time Clock (Mes 1 to 12)
            progress_time = min(mes_asesor / 12, 1.0)
            fig = go.Figure(go.Pie(
                values=[mes_asesor if mes_asesor <= 12 else 12, max(0, 12 - mes_asesor)],
                labels=['Meses Cursados', 'Restantes'],
                hole=.7,
                marker_colors=['#ffd700', 'rgba(255, 215, 0, 0.05)'],
                showlegend=False,
                textinfo='none'
            ))
            fig.update_layout(
                annotations=[dict(text=f'Mes {mes_asesor}<br>de 12', x=0.5, y=0.5, font_size=20, font_color="white", showarrow=False)],
                margin=dict(t=0, b=0, l=10, r=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                height=250
            )
            st.plotly_chart(fig, use_container_width=True)

        # 3. Dual Progress Bars
        st.divider()
        st.markdown("### Dashboards de Persecución")
        
        # Meta 1: Graduación Normal (Meta Fija 36)
        meta_normal = 36
        prog_normal = min(polizas_totales / meta_normal, 1.0) if meta_normal > 0 else 0
        st.markdown(f"#### Graduación Normal (Meta: {meta_normal} Pólizas)")
        st.markdown('<div class="gold-bar">', unsafe_allow_html=True)
        # Security Shield: already has min(val, 1.0) in line 1134
        st.progress(float(prog_normal) if pd.notna(prog_normal) else 0.0)
        
        txt_norm = "¡Meta Lograda! 🎉" if polizas_totales >= meta_normal else f"Avance: {polizas_totales:,.1f} ({prog_normal*100:.1f}%)"
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; font-size: 0.9em; margin-top: -10px;">
                <span>0</span>
                <span style="font-weight: bold; color: #ffd700;">{txt_norm}</span>
                <span>Meta: {meta_normal}</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Meta 2: Graduación con Honores (Meta Fija 48)
        meta_honores = 48
        prog_honores = min(polizas_totales / meta_honores, 1.0) if meta_honores > 0 else 0
        st.markdown(f"#### Graduación con Honores (Meta: {meta_honores} Pólizas)")
        st.markdown('<div class="gold-bar">', unsafe_allow_html=True)
        # Security Shield: already has min(val, 1.0) in line 1144
        st.progress(float(prog_honores) if pd.notna(prog_honores) else 0.0)
        
        txt_hon = "¡Meta Lograda! 🎉" if polizas_totales >= meta_honores else f"Avance: {polizas_totales:,.1f} ({prog_honores*100:.1f}%)"
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; font-size: 0.9em; margin-top: -10px;">
                <span>0</span>
                <span style="font-weight: bold; color: #ffd700;">{txt_hon}</span>
                <span>Meta: {meta_honores}</span>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 4. Legal Footer
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.divider()
        st.markdown("""
        <div style='background: rgba(255,215,0,0.05); padding: 20px; border-radius: 12px; border-left: 4px solid #ffd700; border-right: 4px solid #ffd700;'>
            <h4 style='color: #ffd700; margin-top: 0; text-align: center;'>⚠️ AVISO DE CALIFICACIÓN</h4>
            <p style='font-size: 0.95rem; color: #ffffff; text-align: justify;'>
                Para asesores que logran la meta antes de su corte (Mayo/Noviembre), es obligatorio mantener una producción mínima de 
                una (1) póliza mensual durante todos los meses restantes hasta el cierre del corte. 
                La inactividad comercial en cualquier mes del periodo de mantenimiento anula automáticamente el derecho al evento de graduación.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # --- GENERIC CAMPAIGN ---
    else:
        st.divider()
        cols = st.columns(min(len(df.columns), 4))
        display_cols = [c for c in df.columns if c.lower() not in ['asesor', 'fecha_corte']][:4]
        for i, col_name in enumerate(display_cols):
            with cols[i]:
                st.metric(col_name, str(row.get(col_name, 'N/A')))

# Router
if st.session_state.page == 'welcome':
    show_welcome()
elif st.session_state.page == 'campaign_selector':
    show_campaign_selector()
else:
    show_dashboard()
