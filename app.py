import streamlit as st
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Venezuela Earthquake 2026 – Crisis Dashboard",
    page_icon="🆘",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main { background-color: #0f1117; }
    .stat-box {
        background-color: #1e2130;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        border-left: 5px solid;
        margin-bottom: 10px;
    }
    .stat-number { font-size: 2.2em; font-weight: bold; margin: 5px 0; }
    .stat-label { font-size: 0.9em; color: #aaaaaa; text-transform: uppercase; letter-spacing: 1px; }
    .red { border-color: #ff4b4b; color: #ff4b4b; }
    .orange { border-color: #ffa500; color: #ffa500; }
    .yellow { border-color: #ffd700; color: #ffd700; }
    .blue { border-color: #4b9fff; color: #4b9fff; }
    .org-card {
        background-color: #1e2130;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 4px solid #4b9fff;
    }
    .org-name { font-weight: bold; font-size: 1.05em; }
    .org-desc { color: #cccccc; font-size: 0.9em; margin-top: 4px; }
    .alert-box {
        background-color: #2a1a1a;
        border: 1px solid #ff4b4b;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        color: #ffcccc;
    }
    .info-box {
        background-color: #1a2035;
        border: 1px solid #4b9fff;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        color: #cce0ff;
    }
    .section-title {
        font-size: 1.3em;
        font-weight: bold;
        margin: 20px 0 10px 0;
        padding-bottom: 5px;
        border-bottom: 1px solid #333;
    }
    .update-badge {
        background-color: #ff4b4b;
        color: white;
        font-size: 0.75em;
        padding: 2px 8px;
        border-radius: 10px;
        margin-left: 8px;
        vertical-align: middle;
    }
    a { color: #4b9fff !important; }
    a:hover { color: #80c0ff !important; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("## 🆘 Venezuela Earthquake Crisis Dashboard")
st.markdown("**Twin earthquakes of Mw 7.2 and 7.5 — June 24, 2026 · San Felipe, Yaracuy**")
st.markdown(f"*Last updated: June 29, 2026 · Data sourced from USGS, UNICEF, CNN, ABC News, UN OCHA*")
st.divider()

# --- KEY STATS ---
st.markdown('<div class="section-title">📊 Current Situation <span class="update-badge">LIVE</span></div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-box red">
        <div class="stat-label">Confirmed Dead</div>
        <div class="stat-number red">1,719+</div>
        <div class="stat-label">and rising</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box orange">
        <div class="stat-label">Injured</div>
        <div class="stat-number orange">5,034+</div>
        <div class="stat-label">across all states</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box yellow">
        <div class="stat-label">Missing</div>
        <div class="stat-number yellow">68,900+</div>
        <div class="stat-label">reported missing</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-box blue">
        <div class="stat-label">Displaced</div>
        <div class="stat-number blue">12,721+</div>
        <div class="stat-label">lost their homes</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- TWO COLUMNS: LEFT = SITUATION / RIGHT = HOW TO HELP ---
left, right = st.columns([1.1, 0.9])

with left:

    # EARTHQUAKE DETAILS
    st.markdown('<div class="section-title">🌍 Earthquake Details</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <b>Foreshock:</b> Mw 7.2 · June 24, 2026 at 6:04 PM VET<br>
        <b>Mainshock:</b> Mw 7.5 · 39 seconds later — strongest in Venezuela since 1900<br>
        <b>Epicenter:</b> Veroes municipality, Yaracuy state (San Felipe area)<br>
        <b>Fault:</b> San Sebastián Fault — Caribbean/South American plate boundary<br>
        <b>Aftershocks:</b> 302+ reported as of June 28<br>
        <b>USGS PAGER:</b> Red alert — widespread damage, high loss of life
    </div>
    """, unsafe_allow_html=True)

    # HARDEST HIT AREAS
    st.markdown('<div class="section-title">📍 Hardest Hit Areas</div>', unsafe_allow_html=True)

    areas = [
        ("🔴 La Guaira", "Declared a disaster zone. Caraballeda and Catia La Mar devastated — entire neighborhoods reduced to rubble. ~1/3 of buildings in Catia La Mar damaged per satellite analysis."),
        ("🔴 Caracas", "Capital city severely affected. 432+ schools damaged in Capital District alone. Major rescue operations ongoing in multiple neighborhoods."),
        ("🟠 Carabobo", "Significant infrastructure damage. Hospitals strained beyond capacity."),
        ("🟠 Aragua", "Widespread damage reported. Access routes disrupted."),
        ("🟡 Falcón", "Damage to hospitals and public buildings."),
        ("🟡 Yaracuy", "Epicenter state. Veroes municipality near ground zero."),
        ("🟡 Miranda", "Affected communities receiving aid assessments."),
    ]

    for name, desc in areas:
        st.markdown(f"""
        <div class="org-card">
            <div class="org-name">{name}</div>
            <div class="org-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    # CRITICAL NEEDS
    st.markdown('<div class="section-title">🏥 Critical Needs on the Ground</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="alert-box">
        ⚠️ <b>Medical:</b> Hospitals short on water, antibiotics, IV solution, anesthetics. At least 2 hospitals collapsed. 13 hospitals damaged nationwide.<br><br>
        ⚠️ <b>Children:</b> UNICEF estimates 680,000 children need humanitarian assistance. 3.9 million children live in affected areas.<br><br>
        ⚠️ <b>Water & Sanitation:</b> Thousands of children without access to safe water. Risk of waterborne illness rising.<br><br>
        ⚠️ <b>Shelter:</b> 12,721+ people have lost homes. Schools being used as temporary shelters.<br><br>
        ⚠️ <b>Communications:</b> Venezuela has one of the world's most restricted media environments. 200+ websites blocked. Internet and phone access severely limited in affected areas.<br><br>
        ⚠️ <b>Search & Rescue:</b> Critical 72-hour window has passed but survivors are still being found. Rescue teams from Turkey, El Salvador, Mexico, and others on the ground.
    </div>
    """, unsafe_allow_html=True)

with right:

    # FIND LOVED ONES
    st.markdown('<div class="section-title">🔍 Find Loved Ones</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="alert-box">
        If you are trying to locate family members, use these resources:<br><br>
        🔗 <a href="https://twitter.com/CruzRojaVe" target="_blank">Venezuelan Red Cross (@CruzRojaVe on X)</a> — actively sharing info on affected communities<br><br>
        🔗 <b>Desaparecidos Terremoto Venezuela</b> — volunteer site to register missing persons with names, photos, last known locations<br><br>
        🔗 <b>Venezuela Te Busca</b> — community search registry<br><br>
        📱 WhatsApp groups and X (Twitter) are the primary channels for neighborhood-level welfare checks due to government internet restrictions.<br><br>
        🇺🇸 <b>Americans missing in Venezuela:</b> Contact the <a href="https://ve.usembassy.gov" target="_blank">U.S. Embassy emergency line</a> — 12 Americans remain missing as of June 29.
    </div>
    """, unsafe_allow_html=True)

    # HOW TO DONATE
    st.markdown('<div class="section-title">❤️ Verified Relief Organizations</div>', unsafe_allow_html=True)

    orgs = [
        ("🔴 Venezuelan Red Cross / IFRC", "On the ground: search & rescue, medical care, relief distribution. CHF 2M emergency fund activated.", "https://www.ifrc.org"),
        ("🟠 UNICEF", "Focused on 680,000+ children in need. Air shipments of medical supplies, water & sanitation, tents already arriving.", "https://www.unicefusa.org/stories/venezuela-earthquakes-children-need-help-now"),
        ("🔵 IRC – International Rescue Committee", "Health, nutrition, water, sanitation, protection & food security. Emergency gifts matched up to $2.2M through Sept 30.", "https://www.rescue.org/article/how-help-survivors-earthquakes-venezuela"),
        ("🟢 Direct Relief", "Medical supplies & support to health providers. 100% of donations go to Venezuela earthquake response.", "https://www.directrelief.org/emergency/venezuela-earthquakes-2026/"),
        ("🟡 World Vision", "Emergency response for children and families. Long-term recovery support.", "https://www.worldvision.org/disaster-relief-news-stories/venezuela-earthquake-facts"),
        ("🟣 GEM – Global Empowerment Mission", "Florida-based. Food, water, hygiene kits, medical supplies. Collection points across Miami area.", "https://www.globalempowermentmission.org"),
        ("⚪ Project HOPE", "100+ local staff already in Venezuela. Health & humanitarian response teams deployed.", "https://www.projecthope.org/news-stories/responses/earthquakes-in-venezuela-how-to-help/"),
        ("⚪ CRS / Caritas Venezuela", "Emergency food, water, and shelter through long-standing local partnership.", "https://www.crs.org"),
    ]

    for name, desc, url in orgs:
        st.markdown(f"""
        <div class="org-card">
            <div class="org-name">{name} — <a href="{url}" target="_blank">Donate →</a></div>
            <div class="org-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        ✅ Verify any organization at <a href="https://www.charitynavigator.org" target="_blank">Charity Navigator</a> or 
        <a href="https://www.givewell.org" target="_blank">GiveWell</a> before donating.<br>
        ⚠️ Beware of scams — fake charities surge after disasters. Stick to established organizations.<br>
        💸 <b>Ria Money Transfer</b> has waived all fees to Venezuela through July 15, 2026 for families sending money directly.
    </div>
    """, unsafe_allow_html=True)

    # US GOVERNMENT RESPONSE
    st.markdown('<div class="section-title">🇺🇸 U.S. Government Response</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        • USS Fort Lauderdale and USS Billings deployed<br>
        • C-17 and C-130 aircraft delivering supplies<br>
        • Elite urban search & rescue teams on the ground<br>
        • OFAC General License 60 issued — U.S. sanctions suspended for earthquake relief through Oct 23, 2026<br>
        • State Dept partnered with GEM + Walmart for supply delivery<br><br>
        🔗 <a href="https://ve.usembassy.gov/responding-to-venezuela-earthquakes/" target="_blank">U.S. Embassy Caracas — Full Response Update</a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- FOOTER ---
st.markdown("""
<div style="text-align:center; color:#666; font-size:0.85em; padding: 10px 0;">
    Data sourced from USGS · UNICEF · CNN · ABC News · UN OCHA · U.S. State Department · World Vision · Direct Relief<br>
    This dashboard is for informational purposes. For emergencies in Venezuela, contact local civil protection authorities.<br>
    Built with Streamlit · Updated June 29, 2026
</div>
""", unsafe_allow_html=True)