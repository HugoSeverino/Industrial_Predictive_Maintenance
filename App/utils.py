import json
import pandas as pd

def decrypt_json(json_text):
    try:
        decrypted_data = json.loads(json_text)
        df = pd.DataFrame(decrypted_data)
        return df, ""
    except json.JSONDecodeError:
        return None, "Invalid JSON data"
    except Exception as e:
        return None, str(e)