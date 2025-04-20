"""Unit tests for the ChatSessionRepo."""

import pytest
from unittest.mock import MagicMock
from agent_c_session.repositories.chat_session_repo import ChatSessionRepo
from agent_c_session.models import ChatUser

@pytest.fixture
def mock_zep_client():
    """Fixture for mocking the AsyncZep client.
    
    This creates a mock of the AsyncZep client that can be injected
    into the ChatSessionRepo for testing.
    """
    mock = MagicMock()
    return mock


class TestChatSessionRepo:
    """Test suite for the ChatSessionRepo."""
    
    def test_init(self, mock_zep_client):
        """Test initializing the ChatSessionRepo."""
        repo = ChatSessionRepo(zep_client=mock_zep_client)
        assert repo.zep_client == mock_zep_client
    
    @pytest.mark.asyncio
    async def test_add_chat_user(self, mock_zep_client):
        """Test adding a chat user."""
        # Mock the Zep client response
        mock_response = MagicMock()
        mock_zep_client.user.create.return_value = mock_response
        
        repo = ChatSessionRepo(zep_client=mock_zep_client)
        user = ChatUser(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User"
        )
        
        # Test will be expanded when implementation is completed
        # result = await repo.add_chat_user(user)
        # assert result.username == user.username
        # assert mock_zep_client.user.create.called
    
    @pytest.mark.asyncio
    async def test_new_session(self, mock_zep_client):
        """Test creating a new chat session."""
        # Mock the Zep client response
        mock_response = MagicMock()
        mock_response.session_id = "session123"
        mock_zep_client.session.create.return_value = mock_response
        
        repo = ChatSessionRepo(zep_client=mock_zep_client)
        
        # Test will be expanded when implementation is completed
        # result = await repo.new_session("testuser", "Test Session")
        # assert result.session_id == "session123"
        # assert result.user_id == "testuser"
        # assert result.title == "Test Session"
        # assert mock_zep_client.session.create.called