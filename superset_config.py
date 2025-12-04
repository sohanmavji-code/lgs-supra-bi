# Basic Superset config for demo / Supra BI

SECRET_KEY = "Ae49m!sdf9_29kLm!k32L9sdf9@3Kslf93lskf09!dfy"

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

# Ensure Superset works properly behind a proxy (Render)
ENABLE_PROXY_FIX = True

# Later, you could add theme-related config here if needed.
