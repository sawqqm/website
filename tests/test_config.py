from app.core.config import settings

print(settings.project_name)
print(settings.debug)

print(bool(settings.database_url))