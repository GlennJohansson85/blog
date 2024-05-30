import os

print(f"DEBUG: {os.environ.get('DEBUG')}")
print(f"SECRET_KEY: {os.environ.get('SECRET_KEY')}")
print(f"ALLOWED_HOST: {os.environ.get('ALLOWED_HOST')}")
print(f"CLIENT_ORIGIN: {os.environ.get('CLIENT_ORIGIN')}")

print(f"DATABASE_URL: {os.environ.get('DATABASE_URL')}")
print(f"DATABASE_PASSWORD: {os.environ.get('DATABASE_PASSWORD')}")

print(f"EMAIL_HOST_PASSWORD: {os.environ.get('EMAIL_HOST_PASSWORD')}")
print(f"EMAIL_HOST_USER: {os.environ.get('EMAIL_HOST_USER')}")