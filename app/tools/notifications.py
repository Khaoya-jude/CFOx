def send_notification(channel: str, message: str):
    return {
        "status": "sent",
        "channel": channel,
        "message": message
    }
