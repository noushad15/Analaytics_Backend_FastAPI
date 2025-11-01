import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

TEST_DB_URL = "sqlite+aiosqlite:///./test.db"

@pytest.fixture(scope="session", autouse=True)
def patch_db_engine():
    import app.db.session as session_module
    test_engine = create_async_engine(TEST_DB_URL, echo=False, connect_args={"check_same_thread": False})
    session_module.engine = test_engine
    session_module.SessionLocal = async_sessionmaker(test_engine, expire_on_commit=False, class_=AsyncSession)
    yield
    # Dispose engine after tests
    import asyncio
    asyncio.get_event_loop().run_until_complete(test_engine.dispose())

@pytest.fixture()
def client():
    from app.main import app
    return TestClient(app)
