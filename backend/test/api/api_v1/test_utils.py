import time 
import pytest 
from httpx import AsyncClient, BasicAuth

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.crud import * 

 