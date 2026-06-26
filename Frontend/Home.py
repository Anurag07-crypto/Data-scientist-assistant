import streamlit as st

# ─────────────────────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Data Scientiest — AI-Powered ML Pipeline",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────────────────────
# CSS (via st.markdown - small enough to not truncate)
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header, .stDeployButton { display: none !important; }

.hero-section {
    position: relative;
    padding: 5rem 2rem 6rem 2rem;
    text-align: center;
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    border-radius: 0 0 40px 40px;
    margin: -6rem -4rem 0 -4rem;
    overflow: hidden;
}
.hero-section::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%);
    animation: pulse-glow 8s ease-in-out infinite;
}
@keyframes pulse-glow {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.1); opacity: 0.8; }
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(99, 102, 241, 0.3);
    color: #a5b4fc;
    padding: 8px 20px;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
    animation: fadeInDown 0.8s ease-out;
}
.hero-title {
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    font-weight: 800;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 1rem;
    letter-spacing: -0.02em;
    animation: fadeInUp 0.8s ease-out 0.2s both;
}
.hero-title span {
    background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-subtitle {
    font-size: clamp(1rem, 2vw, 1.25rem);
    color: #94a3b8;
    max-width: 600px;
    margin: 0 auto 2.5rem auto;
    line-height: 1.7;
    animation: fadeInUp 0.8s ease-out 0.4s both;
}
.cta-primary {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white !important;
    padding: 14px 36px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 1rem;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.4);
    display: inline-block;
    animation: fadeInUp 0.8s ease-out 0.6s both;
}
.cta-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(99, 102, 241, 0.6);
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}
.stats-section {
    display: flex;
    justify-content: center;
    gap: 4rem;
    padding: 3rem 2rem;
    flex-wrap: wrap;
}
.stat-item { text-align: center; }
.stat-number {
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.stat-label { color: #64748b; font-size: 0.9rem; font-weight: 500; }
.pipeline-section { padding: 4rem 2rem; text-align: center; }
.section-title { font-size: 2rem; font-weight: 700; color: #1e293b; margin-bottom: 0.5rem; }
.section-subtitle { color: #64748b; margin-bottom: 3rem; }
.pipeline-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    max-width: 1100px;
    margin: 0 auto;
}
.pipeline-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    min-width: 130px;
}
.step-icon {
    width: 60px; height: 60px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.6rem;
    margin-bottom: 0.75rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}
.step-icon:hover { transform: scale(1.1) rotate(5deg); }
.step-icon.purple { background: linear-gradient(135deg, #ede9fe, #ddd6fe); }
.step-icon.blue   { background: linear-gradient(135deg, #dbeafe, #bfdbfe); }
.step-icon.green  { background: linear-gradient(135deg, #d1fae5, #a7f3d0); }
.step-icon.orange { background: linear-gradient(135deg, #ffedd5, #fed7aa); }
.step-icon.pink   { background: linear-gradient(135deg, #fce7f3, #fbcfe8); }
.step-label { font-weight: 600; color: #334155; font-size: 0.9rem; }
.step-desc  { font-size: 0.75rem; color: #94a3b8; margin-top: 0.25rem; }
.pipeline-arrow {
    color: #cbd5e1;
    font-size: 1.5rem;
    margin-top: -20px;
    animation: float 3s ease-in-out infinite;
}
.features-section {
    padding: 3rem 2rem;
    background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
    border-radius: 40px 40px 0 0;
    margin: 0 -4rem;
}
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    max-width: 1100px;
    margin: 0 auto;
}
.feature-card {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    border: 1px solid #e2e8f0;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}
.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    transform: scaleX(0);
    transition: transform 0.3s ease;
}
.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    border-color: #c7d2fe;
}
.feature-card:hover::before { transform: scaleX(1); }
.feature-icon {
    width: 48px; height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    margin-bottom: 1rem;
}
.feature-title { font-size: 1.1rem; font-weight: 700; color: #1e293b; margin-bottom: 0.5rem; }
.feature-desc  { color: #64748b; font-size: 0.9rem; line-height: 1.6; }
.cta-section { text-align: center; padding: 4rem 2rem; }
.footer-section {
    text-align: center;
    padding: 2rem;
    color: #94a3b8;
    font-size: 0.85rem;
    border-top: 1px solid #e2e8f0;
    margin-top: 2rem;
}
@media (max-width: 768px) {
    .hero-section { padding: 3rem 1rem 4rem 1rem; margin: -6rem -1rem 0 -1rem; }
    .pipeline-container { flex-direction: column; gap: 0.5rem; }
    .pipeline-arrow { transform: rotate(90deg); margin: 0; }
    .features-section { margin: 0 -1rem; border-radius: 20px 20px 0 0; }
    .stats-section { gap: 2rem; }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# HERO SECTION
# ─────────────────────────────────────────────────────────────
st.html("""
<div class="hero-section">
    <div class="hero-badge">
        <span>✨</span> AI-Powered Data Science Automation
    </div>
    <h1 class="hero-title">
        Automate Your<br><span>Data Science Workflow</span>
    </h1>
    <p class="hero-subtitle">
        Upload your dataset, get AI-driven insights with model recommendations, 
        preprocess your data, and train production-ready ML models — all in one seamless pipeline.
    </p>
    <a href="preprocessing_&_insights" target="_self" class="cta-primary">🚀 Launch Pipeline</a>
</div>
""")

# ─────────────────────────────────────────────────────────────
# STATS
# ─────────────────────────────────────────────────────────────
st.html("""
<div class="stats-section">
    <div class="stat-item">
        <div class="stat-number">3</div>
        <div class="stat-label">Simple Steps</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">15+</div>
        <div class="stat-label">ML Models</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">0</div>
        <div class="stat-label">Code Required</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">∞</div>
        <div class="stat-label">Possibilities</div>
    </div>
</div>
""")

# ─────────────────────────────────────────────────────────────
# PIPELINE
# ─────────────────────────────────────────────────────────────
st.html("""
<div class="pipeline-section">
    <h2 class="section-title">How It Works</h2>
    <p class="section-subtitle">Your end-to-end machine learning pipeline in three simple steps</p>
    <div class="pipeline-container">
        <div class="pipeline-step">
            <div class="step-icon purple">📤</div>
            <div class="step-label">Upload CSV</div>
            <div class="step-desc">Drop your dataset</div>
        </div>
        <div class="pipeline-arrow">→</div>
        <div class="pipeline-step">
            <div class="step-icon blue">🧠</div>
            <div class="step-label">AI Insights</div>
            <div class="step-desc">Get model recommendations</div>
        </div>
        <div class="pipeline-arrow">→</div>
        <div class="pipeline-step">
            <div class="step-icon green">⚙️</div>
            <div class="step-label">Preprocess</div>
            <div class="step-desc">Clean & transform data</div>
        </div>
        <div class="pipeline-arrow">→</div>
        <div class="pipeline-step">
            <div class="step-icon orange">🎯</div>
            <div class="step-label">Train Model</div>
            <div class="step-desc">Auto-ML training</div>
        </div>
        <div class="pipeline-arrow">→</div>
        <div class="pipeline-step">
            <div class="step-icon pink">📊</div>
            <div class="step-label">Results</div>
            <div class="step-desc">Download & deploy</div>
        </div>
    </div>
</div>
""")

st.markdown("---")

# ─────────────────────────────────────────────────────────────
# FEATURES
# ─────────────────────────────────────────────────────────────
st.html("""
<div class="features-section">
    <h2 class="section-title" style="text-align:center;">Why Use This Platform?</h2>
    <p class="section-subtitle" style="text-align:center;">Everything you need to go from raw data to trained models</p>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #ede9fe, #ddd6fe);">🤖</div>
            <div class="feature-title">AI Model Recommendation</div>
            <div class="feature-desc">Let AI analyze your data and suggest the best machine learning model for your specific problem and dataset.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #dbeafe, #bfdbfe);">🧹</div>
            <div class="feature-title">Smart Preprocessing</div>
            <div class="feature-desc">Automatic handling of missing values, categorical encoding, and feature scaling with customizable options.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #d1fae5, #a7f3d0);">📈</div>
            <div class="feature-title">15+ ML Algorithms</div>
            <div class="feature-desc">From Logistic Regression to XGBoost — access a wide range of classification, regression, and clustering models.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #ffedd5, #fed7aa);">⚡</div>
            <div class="feature-title">Zero-Code Required</div>
            <div class="feature-desc">No programming knowledge needed. Upload, configure, and train — all through an intuitive point-and-click interface.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #fce7f3, #fbcfe8);">🔍</div>
            <div class="feature-title">Interactive Data Preview</div>
            <div class="feature-desc">Explore your dataset with expandable previews, column info, and data type summaries before processing.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon" style="background: linear-gradient(135deg, #e0f2fe, #bae6fd);">💾</div>
            <div class="feature-title">Export Trained Models</div>
            <div class="feature-desc">Download your trained models as pickle files for easy integration into production systems and APIs.</div>
        </div>
    </div>
</div>
""")

# ─────────────────────────────────────────────────────────────
# BOTTOM CTA
# ─────────────────────────────────────────────────────────────
st.html("""
<div class="cta-section">
    <h2 style="font-size: 2rem; font-weight: 700; color: #1e293b; margin-bottom: 0.5rem;">
        Ready to Automate Your Workflow?
    </h2>
    <p style="color: #64748b; max-width: 500px; margin: 0 auto 2rem auto; line-height: 1.6;">
        Start building intelligent models from your data in minutes, not days.
    </p>
    <a href="preprocessing_&_insights" target="_self" class="cta-primary">🚀 Get Started Now</a>
</div>
""")

# ─────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────
st.html("""
<div class="footer-section">
    <p>🧠 <strong>Data Scientiest</strong> — AI-Powered Machine Learning Pipeline</p>
    <p style="margin-top: 0.5rem;">Built with Streamlit • Powered by AI</p>
</div>
""")