def verify_api_key(api_key: str):
    if not api_key:
        raise PermissionError("Missing API key")
