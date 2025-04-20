"""Unit tests for the ChatSession model."""

import pytest
from datetime import datetime
from agent_c.session.models.chat_session import ChatSession, ChatMessage


class TestChatSession:
    """Test suite for the ChatSession model."""
    
    def test_create_chat_session(self):
        """Test creating a ChatSession instance."""
        session = ChatSession(
            session_id="session123",
            user_id="user456",
            title="Test Session"
        )
        
        assert session.session_id == "session123"
        assert session.user_id == "user456"
        assert session.title == "Test Session"
        assert session.metadata == {}
        assert session.managed_metadata == {}
        assert isinstance(session.created_at, datetime)
        assert isinstance(session.updated_at, datetime)
    
    def test_get_set_meta(self):
        """Test getting and setting metadata."""
        session = ChatSession(session_id="session123", user_id="user456")
        
        # Test setting and getting metadata
        session.set_meta("key1", "value1")
        assert session.get_meta("key1") == "value1"
        
        # Test default value for non-existent key
        assert session.get_meta("non_existent", "default") == "default"
        
        # Test updating existing key
        session.set_meta("key1", "new_value")
        assert session.get_meta("key1") == "new_value"
        
    def test_create_chat_message(self):
        """Test creating a ChatMessage instance."""
        message = ChatMessage(
            role="user",
            content="Hello, world!"
        )
        
        assert message.role == "user"
        assert message.content == "Hello, world!"
        assert isinstance(message.timestamp, datetime)
        assert message.metadata == {}