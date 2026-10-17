import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.testmuai.com/selenium-playground"

LT_USERNAME = os.getenv("LT_USERNAME", "")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY", "")
LT_GRID_URL = "wss://cdp.lambdatest.com/playwright?capabilities="


_default_mode = "cloud" if LT_USERNAME and LT_ACCESS_KEY else "local"
RUN_MODE = os.getenv("RUN_MODE", _default_mode).lower()

BUILD_NAME = "Playwright 101 - Final Run"
