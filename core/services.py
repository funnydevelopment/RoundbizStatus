import uuid

import aiohttp

from create_bot import config


async def is_valid_uuid(uuid_str: str) -> bool:
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return True
    except ValueError:
        return False


async def get_message_text(data: dict) -> str:
    message = ""
    for key, value in data.items():
        message += f"{key}: <b>{value}</b>\n"
    return message


async def get_order_data(tx_id: str) -> dict:
    url = config.service.URL
    params = {
        "shop_id": config.service.SHOP_ID,
        "tx_id": tx_id,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=params) as response:
            order_data = dict()
            if response.status == 200:
                order_data["status"] = response.status
                order_data["content-type"] = response.headers["content-type"]
                print(type(order_data))

                data = await response.json()
                print(type(data))
                print(data)
                order_data.update(data)
                print(order_data)
            else:
                order_data["status"] = response.status
            return order_data
