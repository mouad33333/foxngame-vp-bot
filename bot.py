import requests
import time

# Telegram bot token and chat ID
token = "8465891566:AAE8QusY3D-z2PSLAZxS7IICsSjZtVGZx74"
chat_id = "6271009500"  # Your Telegram Chat ID

# FoxNGame product URL
FOXNGAME_URL = "https://www.foxngame.com/en/valorant"

# Function to send message via Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, json=payload)

# Function to check discounts
def check_discounts():
    try:
        response = requests.get(FOXNGAME_URL)
        if response.status_code != 200:
            print("Failed to fetch data from FoxNGame.")
            return
        
        html = response.text.lower()
        # Check for discount keywords
        for discount in [5, 10, 15, 20, 25, 30]:
            if f"-{discount}%" in html:
                message = (
                    f"⚡ Discount Alert! Valorant Points now at {discount}% OFF on FoxNGame!\n\n"
                    f"Check it here: {FOXNGAME_URL}"
                )
                send_telegram_message(message)
                print("Alert sent:", message)
                return
        print("No discounts above 5% found.")
    except Exception as e:
        print("Error checking discounts:", e)

# Run the checker every 30 minutes
print("Bot is running and checking discounts...")
while True:
    check_discounts()
    time.sleep(1800)  # 30 minutes
