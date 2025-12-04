import os

# Load secret key from environment variables
SECRET_KEY = (
    os.environ.get("SUPERSET_SECRET_KEY")
    or os.environ.get("SECRET_KEY")
    or "fallback_key_that_wont_be_used"
)

# Required for Render reverse-proxy
ENABLE_PROXY_FIX = True

# Minimal config
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}
