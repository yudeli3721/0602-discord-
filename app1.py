import os
import requests

# ==========================================
# 1. 定義發送 Discord Webhook 的功能
# ==========================================
def send_discord_webhook(webhook_url, title, content):
    """直接發送漂亮的卡片訊息到 Discord"""
    payload = {
        "content": "📢 **注意！**",
        "embeds": [
            {
                "title": f" {title}",
                "description": content,
                "color": 15277667,  # 邊條 (十進位顏色碼)
                "footer": {
                    "text": "由 Github Actions 自動觸發"
                }
            }
        ]
    }
   
    # 發送 POST 請求給 Discord
    response = requests.post(webhook_url, json=payload)
    return response.status_code
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

status = send_discord_webhook(WEBHOOK_URL, "記得喝水", "@薛MANO小朋友")
