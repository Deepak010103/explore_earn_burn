# Importing the API and instantiating the client using your keys
from terra.base_client import Terra
from config import CONFIG


terra = Terra(CONFIG.get("API_KEY"), CONFIG.get("DEV_ID"), CONFIG.get("SECRET"))

parsed_api_response = terra.list_providers().get_parsed_response()
print(parsed_api_response)