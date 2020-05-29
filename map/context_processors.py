from config.project_config import PROJECT_TITLE, LOGO_PATH


def get_project_title(request):
    return {
        'project_title': PROJECT_TITLE,
        'logo_path': LOGO_PATH,
    }