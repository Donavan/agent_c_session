"""Unit tests for the ChatUser model."""

import pytest
from datetime import datetime
from agent_c.session.models.chat_user import ChatUser


class TestChatUser:
    """Test suite for the ChatUser model."""
    
    def test_create_chat_user(self):
        """Test creating a ChatUser instance."""
        user = ChatUser(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User"
        )
        
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.first_name == "Test"
        assert user.last_name == "User"
        assert user.metadata == {}
        assert user.managed_metadata == {}
    
    def test_get_set_meta(self):
        """Test getting and setting metadata."""
        user = ChatUser(username="testuser")
        
        # Test setting and getting metadata
        user.set_meta("key1", "value1")
        assert user.get_meta("key1") == "value1"
        
        # Test default value for non-existent key
        assert user.get_meta("non_existent", "default") == "default"
        
        # Test updating existing key
        user.set_meta("key1", "new_value")
        assert user.get_meta("key1") == "new_value"