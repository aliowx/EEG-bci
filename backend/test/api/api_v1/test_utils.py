import time 
import pytest 
from httpx import AsyncClient, BasicAuth

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app import crud

class TestUtils:
    
    @pytest.mark.asyncio
    async def test_db_log(self, client: AsyncClient, db:AsyncSession):
        
        tracker_id = "test_id"

        response = await client.post(
            f"{settings.API_V1_STR}/utils/test-db-log?tracker_id={tracker_id}",
            auth = BasicAuth(
                username=settings.FIRST_SUPERUSER,
                password=settings.FIRST_SUPERUSER_PASSWORD
            )
        )
        
        time.sleep(0.1)
        assert response.status_code == 500
        log_record = await crud.request_log.get_by_tracker_id(
            db=db, tracker_id=tracker_id
            
        )
        
        assert log_record != None
        assert log_record.tracker_id == tracker_id
        assert log_record.processing_time != None