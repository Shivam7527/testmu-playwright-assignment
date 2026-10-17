CLOUD_COMBOS = [
    {
        "id": "win10-chrome",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "platform": "Windows 10",
    },
    {
        "id": "win11-edge",
        "browserName": "MicrosoftEdge",
        "browserVersion": "latest",
        "platform": "Windows 11",
    },
]

# used only when RUN_MODE=local
LOCAL_COMBOS = [
    {"id": "local-chromium", "engine": "chromium"},
    {"id": "local-firefox", "engine": "firefox"},
]