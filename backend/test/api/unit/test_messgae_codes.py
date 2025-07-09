import pytest 
from app.core.middleware.get_accept_language_middleware import  _request_accept_language_var


from app.utils.message_codes import MessageCodes



class TestMessageCodes:
    @pytest.mark.asyncio
    async def test_accept_language_en(self)->None:...