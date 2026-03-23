import asyncio

from app.services.req_store import get_request, set_request_status
from config import REQUEST_TIMEOUT

async def expire_request(request_id, bot):
    await asyncio.sleep(REQUEST_TIMEOUT)

    request = get_request(request_id)

    if not request: return
    if request['status'] != 'pending': return

    set_request_status(request_id, 'expired')

    await bot.send_message(
        request['user_id'],
        text="К сожалению, никто из администраторов не смог принять запрос."
    )