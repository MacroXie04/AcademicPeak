import requests

def get_csgo_item_price(app_id, item_name):
    base_url = "https://api.steampowered.com/ISteamEconomy/GetAssetPrices/v1/"
    api_key = "669B27C8F4A5A4D10E6069DADC0F1E3E"  # 替换为你自己的 Steam API Key

    params = {
        "key": api_key,
        "appid": app_id,
        "language": "en"   # 可以根据需要更改语言类型
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)  # 打印完整的 JSON 数据，以便查看结构
        # ... 在这里添加正确的数据提取逻辑
    else:
        print("Error: Unable to fetch data.")

    return None

if __name__ == "__main__":
    app_id = 730  # CSGO 的 Steam App ID
    item_name = "AK-47 | Redline"  # 需要查询的饰品名称

    price = get_csgo_item_price(app_id, item_name)
    if price is not None:
        print(f"The price of {item_name} is {price}")
    else:
        print("Price data not found.")
