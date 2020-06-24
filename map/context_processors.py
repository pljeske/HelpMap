from config.project_config import PROJECT_TITLE, LOGO_PATH, CUSTOM_CSS, MAPBOX_API_KEY


def get_project_title(request):
    return {
        'project_title': PROJECT_TITLE,
        'logo_path': LOGO_PATH,
        'custom_css': CUSTOM_CSS,
        'mapbox_api_key': MAPBOX_API_KEY,
    }
