import settings
import requests


def setwebhook(token, url):
    telegram_url = f"https://api.telegram.org/bot{token}/setWebhook"
    params = {"url": url}
    print(requests.get(telegram_url, json=params).json())


def deletewebhook(token):
    telegram_url = f"https://api.telegram.org/bot{token}/deleteWebhook"
    print(requests.get(telegram_url).json())


def getwebhookinfo(token):
    telegram_url = f"https://api.telegram.org/bot{token}/getWebhookInfo"
    print(requests.get(telegram_url).json())


if __name__ == "__main__":
    ret = getwebhookinfo(settings.api_key)
    print(ret)
    ret = deletewebhook(settings.api_key)
    print(ret)
    url = "https://andreit100.pythonanywhere.com/bot/7707284304/"
    ret = setwebhook(settings.api_key, url)
    print(ret)
