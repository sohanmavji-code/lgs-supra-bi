import os

SECRET_KEY = (
    os.environ.get("SUPERSET_SECRET_KEY")
    or os.environ.get("SECRET_KEY")
    or "fallback_key"
)

ENABLE_PROXY_FIX = True

# Enable all modern UI features, including Theme Editor
FEATURE_FLAGS = {
    "DASHBOARD_NATIVE_FILTERS_SET": False,
    "DASHBOARD_CROSS_FILTERS": True,
    "ENABLE_ADVANCED_DATA_TYPES": True,
    "ALLOW_ADHOC_SUBQUERY": True,
    "THUMBNAILS": True,
    "DASHBOARD_RBAC": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_FILTER_PREVIEW": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ALERT_REPORTS": True,
    "ENABLE_JAVASCRIPT_CONTROLS": True,

    # THIS IS THE ONE THAT ENABLES THE THEME MENU:
    "ENABLE_DASHBOARD_NAVIGATION": True,
    "ENABLE_NEW_UI_COMPONENTS": True,
    "ENABLE_REACT_CRUD_VIEWS": True,
    "ENABLE_SETTINGS": True,
}

APP_NAME = "Supra BI - Local Grown Salads"
