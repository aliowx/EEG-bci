import pytest 
from app.core.middleware.get_accept_language_middleware import  _request_accept_language_var


from app.utils.message_codes import MessageCodes



class TestMessageCodes:
    
    @pytest.mark.asyncio
    async def test_accept_language_en(self)-> None:
        test_case = "da, en-gb;q=0.8,"
        _request_accept_language_var.set(test_case)
        
        response_message = MessageCodes.get_message(MessageCodes.successful_operation)
        assert response_message == MessageCodes.english_messages_names[MessageCodes.successful_operation]