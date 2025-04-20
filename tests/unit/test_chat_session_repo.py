"""Unit tests for the ChatSessionRepo."""

import pytest
from unittest.mock import patch, MagicMock
from agent_c.session.repositories.chat_session_repo import ChatSessionRepo
from agent_c.session.models.chat_user import ChatUser
from agent_c.session.models.chat_session import ChatSession


@pytest.fixture
def mock_zep_client():
    """Fixture for mocking the Zep client."""
    with patch("agent_c.session.repositories.chat_session_repo.ZepClient") as mock:
        yield mock.return_value


class TestChatSessionRepo:
    """Test suite for the ChatSessionRepo."""
    
    def test_init(self, mock_zep_client):
        """Test initializing the ChatSessionRepo."""
        repo = ChatSessionRepo("https://api.zep.us/v2", "test_api_key")
        # Add assertions when implementation is completed
    
    @pytest.mark.asyncio
    async def test_add_chat_user(self, mock_zep_client):
        """Test adding a chat user."""
        # Mock the Zep client response
        mock_zep_client.add_user.return_value = MagicMock()
        
        repo = ChatSessionRepo("https://api.zep.us/v2", "test_api_key")
        user = ChatUser(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User"
        )
        
        # Test will be expanded when implementation is completed
        # result = await repo.add_chat_user(user)
        # assert result.username == user.username
    
    @pytest.mark.asyncio
    async def test_new_session(self, mock_zep_client):
        """Test creating a new chat session."""
        # Mock the Zep client response
        mock_zep_client.add_session.return_value = MagicMock(session_id="session123")
        
        repo = ChatSessionRepo("https://api.zep.us/v2", "test_api_key")
        
        # Test will be expanded when implementation is completed
        # result = await repo.new_session("testuser", "Test Session")
        # assert result.session_id == "session123"
        # assert result.user_id == "testuser"
        # assert result.title == "Test Session"