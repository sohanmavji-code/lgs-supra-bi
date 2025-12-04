# Basic Superset config for demo / Supra BI

SECRET_KEY = "lgs_demo_secret_key"

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

# Ensure Superset works properly behind a proxy (Render)
ENABLE_PROXY_FIX = True

# Later, you could add theme-related config here if needed.
