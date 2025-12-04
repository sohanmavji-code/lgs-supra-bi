import os

#
# ───────────────────────────────────────────────────────────
#   SECURITY + AUTHENTICATION
# ───────────────────────────────────────────────────────────
#

SECRET_KEY = (
    os.environ.get("SUPERSET_SECRET_KEY")
    or os.environ.get("SECRET_KEY")
    or "CHANGE_ME_IN_PRODUCTION"
)

# Required when running behind Render's reverse proxy
ENABLE_PROXY_FIX = True

#
# ───────────────────────────────────────────────────────────
#   CRITICAL: ENABLE MODERN UI + THEME EDITOR
# ───────────────────────────────────────────────────────────
#

# **MANDATORY FOR SETTINGS/THEME MENU IN PRODUCTION**
SIP_38_ENABLED = True

FEATURE_FLAGS = {
    # Dashboard & charts
    "DASHBOARD_NATIVE_FILTERS_SET": False,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_FILTER_PREVIEW": True,
    "DASHBOARD_RBAC": True,
    "THUMBNAILS": True,

    # SQL & query features
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ALLOW_ADHOC_SUBQUERY": True,
    "ENABLE_ADVANCED_DATA_TYPES": True,
    "ENABLE_JAVASCRIPT_CONTROLS": True,

    # Modern UI system
    "ENABLE_NEW_UI_COMPONENTS": True,
    "ENABLE_REACT_CRUD_VIEWS": True,
    "ENABLE_DASHBOARD_NAVIGATION": True,

    # **THEME EDITOR + SETTINGS MENU**
    "ENABLE_SETTINGS": True,
}

#
# ───────────────────────────────────────────────────────────
#   BRANDING
# ───────────────────────────────────────────────────────────
#

APP_NAME = "Supra BI - Local Grown Salads"

# You can add a logo later if needed:
# APP_ICON = "/static/assets/images/lgs_logo.png"
