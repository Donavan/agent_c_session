"""ChatSessionRepo for Agent C Session Manager.

Provides methods for managing chat users and sessions with Zep Cloud as the backend.
"""

from typing import Any, Dict, List, Optional, Union
from ..models.chat_user import ChatUser
from ..models.chat_session import ChatSession


class ChatSessionRepo:
    """Repository for managing chat users and sessions.
    
    Provides methods for creating, retrieving, updating, and deleting chat users and sessions,
    with Zep Cloud as the backing store.
    
    Attributes:
        zep_client: Client for interacting with Zep Cloud API
    """
    
    def __init__(self, zep_api_url: str, zep_api_key: str):
        """Initialize the chat session repository.
        
        Args:
            zep_api_url: URL of the Zep Cloud API
            zep_api_key: API key for authenticating with Zep Cloud
        """
        # Implementation to be added
        pass
    
    async def add_chat_user(self, user: ChatUser, initial_metadata: Optional[Dict[str, Any]] = None) -> ChatUser:
        """Add a new chat user.
        
        Args:
            user: ChatUser model with user details
            initial_metadata: Optional initial metadata for the user
            
        Returns:
            The created ChatUser
            
        Raises:
            ValueError: If a user with the same username already exists
        """
        # Implementation to be added
        pass
    
    async def update_chat_user(self, user: ChatUser) -> ChatUser:
        """Update an existing chat user.
        
        Args:
            user: ChatUser model with updated user details
            
        Returns:
            The updated ChatUser
            
        Raises:
            ValueError: If the user doesn't exist
        """
        # Implementation to be added
        pass
    
    async def delete_chat_user(self, username: str, hard_delete: bool = False) -> None:
        """Delete a chat user.
        
        Args:
            username: Username of the user to delete
            hard_delete: If True, permanently delete the user and all their sessions;
                         if False, just mark the user as inactive
                         
        Raises:
            ValueError: If the user doesn't exist
        """
        # Implementation to be added
        pass
    
    async def get_chat_user(self, username: str) -> ChatUser:
        """Get a chat user by username.
        
        Args:
            username: Username of the user to retrieve
            
        Returns:
            The requested ChatUser
            
        Raises:
            ValueError: If the user doesn't exist
        """
        # Implementation to be added
        pass
    
    async def get_user_sessions(self, username: str, limit: int = 10, offset: int = 0) -> List[ChatSession]:
        """Get chat sessions for a user.
        
        Args:
            username: Username of the user
            limit: Maximum number of sessions to return
            offset: Number of sessions to skip for pagination
            
        Returns:
            List of ChatSession objects belonging to the user
            
        Raises:
            ValueError: If the user doesn't exist
        """
        # Implementation to be added
        pass
    
    async def search_user_sessions(self, username: str, query: str, limit: int = 10) -> List[ChatSession]:
        """Search for chat sessions for a user.
        
        Args:
            username: Username of the user
            query: Search query string
            limit: Maximum number of sessions to return
            
        Returns:
            List of ChatSession objects matching the search criteria
            
        Raises:
            ValueError: If the user doesn't exist
        """
        # Implementation to be added
        pass
    
    async def get_user_session(self, username: str, session_id: str) -> ChatSession:
        """Get a specific chat session for a user.
        
        Args:
            username: Username of the user
            session_id: ID of the session to retrieve
            
        Returns:
            The requested ChatSession
            
        Raises:
            ValueError: If the user or session doesn't exist
        """
        # Implementation to be added
        pass
    
    async def remove_user_session(self, username: str, session_id: str) -> None:
        """Remove a chat session for a user.
        
        Args:
            username: Username of the user
            session_id: ID of the session to remove
            
        Raises:
            ValueError: If the user or session doesn't exist
        """
        # Implementation to be added
        pass
    
    async def new_session(self, username: str, title: Optional[str] = None, 
                         initial_metadata: Optional[Dict[str, Any]] = None) -> ChatSession:
        """Create a new chat session for a user.
        
        Args:
            username: Username of the user
            title: Optional title for the session
            initial_metadata: Optional initial metadata for the session
            
        Returns:
            The created ChatSession
            
        Raises:
            ValueError: If the user doesn't exist
        """
        # Implementation to be added
        pass