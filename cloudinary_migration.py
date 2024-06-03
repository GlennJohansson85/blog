import os
from dotenv import load_dotenv
import cloudinary.uploader

# Load environment variables from env.py into the environment
load_dotenv('env.py')

# Configure Cloudinary (assuming you've already configured it in your Django settings)

cloudinary.config(
    cloud_name='dnldfoz08',
    api_key='681735167721712',
    api_secret='7FIRAz3WeOzRSy-37aIi3zTuG1Y'
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_folder_path = os.path.join(BASE_DIR, 'static')

# Iterate through files in the static folder
for root, dirs, files in os.walk(static_folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        # Upload the file to Cloudinary
        result = cloudinary.uploader.upload(file_path, folder="static")
        # Process the result as needed
        print("Uploaded:", result["secure_url"])


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
media_folder_path = os.path.join(BASE_DIR, 'media')

# Iterate through files in the media folder
for root, dirs, files in os.walk(media_folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        # Upload the file to Cloudinary
        result = cloudinary.uploader.upload(file_path, folder="media")
        # Process the result as needed
        print("Uploaded:", result["secure_url"])