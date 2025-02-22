from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQHGGAwAQpm0GK3I2-OHSlje4gnzfg2B0IVhs8rIOyR6CXJNgC3wyG5CCz8UsQBQugL-KIxMkiN5w6k8bHNWbWzHvIgLPDPAoC880OasTdmtgoNRli1bNrPYQf59UkzSjRc7pHAg3CMV5IFtVxNfQ6E6oFIriSsHv2cwEU1CpQNyFohcfObZn6b216lGgxLNmig586T24wO9MwuOmmnxo_PM-bNUnc9AfyJYYyhxpunJoqj7nSdnbnZiKyxgsmpkT1I0l9S4YtdxrdAREuK18ovcKS5kHeYbxeRX7hv693slRRJuzLlPYogKvXkPrz2eEZNltnt4I-AswIxk5vnGunC7224gSQAAAAHGEUxbAA")
BOT_TOKEN = getenv("7865370162:AAGYEV7ngldwFgdsdv5vKAGXgkXGg6ov510")

API_ID = int(getenv(13485297))
API_HASH = getenv("4858ef14a1e4e5d1f496560f33ec9cb4")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv(7008510909).split()))

