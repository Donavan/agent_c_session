"""ChatSessionRepo for Agent C Session Manager.

Provides methods for managing chat users and sessions with Zep Cloud as the backend.
"""
import os
from typing import Any, Dict, List, Optional, Union
from src.agent_c_session.models.chat_user import ChatUser
from src.agent_c_session.models.chat_session import ChatSession
from zep_cloud.client import AsyncZep
from zep_cloud.errors import NotFoundError, InternalServerError, BadRequestError, UnauthorizedError
from agent_c.util.slugs import MnemonicSlugs

import zep_cloud.types as zep_types


class ChatSessionRepo:
    """Repository for managing chat users and sessions.
    
    Provides methods for creating, retrieving, updating, and deleting chat users and sessions,
    with Zep Cloud as the backing store.
    
    Attributes:
        zep_client: Client for interacting with Zep Cloud API
    """
    
    def __init__(self, zep_client: Optional[AsyncZep] = None, zep_api_key: Optional[str] = None):
        """Initialize the chat session repository.
        
        Args:
            zep_client: A zep client instance for interacting with Zep Cloud API
            zep_api_key: API key for authenticating with Zep Cloud if not client provided
                         Will be pulled from ZEP_API_KEY env variable if not provided
        """
        if not zep_client:
            api_key = zep_api_key or os.getenv("ZEP_API_KEY")
            zep_client = AsyncZep(api_key=api_key)

        self.zep_client = zep_client
    
    async def add_chat_user(self, user: ChatUser) -> ChatUser:
        """Add a new chat user.
        
        Args:
            user: ChatUser model with user details
            initial_metadata: Optional initial metadata for the user
            
        Returns:
            The created ChatUser with a pounding Zep user object
            
        Raises:
            ValueError: If a user with the same username already exists
        """
        user.zep_user = await self.zep_client.user.add(**user.model_dump())

        return user

    
    async def update_chat_user_info(self, user: ChatUser) -> ChatUser:
        """Update an existing chat user.
        
        Args:
            user: ChatUser model with updated user details
            
        Returns:
            The updated ChatUser
            
        Raises:
            ValueError: If the user doesn't exist
        """
        user.zep_user = await self.zep_client.user.update(first_name=user.first_name, last_name=user.last_name,
                                                           email=user.email, user_id=user.user_id)
        return user
    
    async def delete_chat_user(self, user_id: str) -> None:
        """Delete a chat user.
        
        Args:
            usernuser_idame: Username of the user to delete

        Raises:
            ValueError: If the user doesn't exist
        """
        await self.zep_client.user.delete(user_id=user_id)
    
    async def get_chat_user(self, user_id: str) -> ChatUser:
        """Get a chat user by user_id.
        
        Args:
            username: user_id of the user to retrieve
            
        Returns:
            The requested ChatUser

        Raises:
            ValueError: If the user doesn't exist
        """
        return ChatUser.from_zep(await self.zep_client.user.get(user_id=user_id))
    
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
        """Centric India Dev"""
        sessions = await self.zep_client.memory.list_sessions(user_id=username, limit=limit, offset=offset)
        return [ChatSession.from_zep(session) for session in sessions]
    
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
        """Centric India Dev"""
        sessions = await self.zep_client.memory.search_sessions(user_id=username, text=query, limit=limit)
        return [ChatSession.from_zep(session) for session in sessions]
    
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
        """Centric India Dev"""
        session = await self.zep_client.memory.get_session(user_id=username,session_id=session_id)
        return ChatSession.from_zep(session)
    
    async def remove_user_session(self, username: str, session_id: str) -> None:
        """Remove a chat session for a user.
        
        Args:
            username: Username of the user
            session_id: ID of the session to remove
            
        Raises:
            ValueError: If the user or session doesn't exist
        """
        """Centric India Dev"""
        await self.zep_client.memory.delete_session(user_id=username,session_id=session_id)
    
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
        """Centric India Dev"""
        session = await self.zep_client.memory.add_session(
            user_id=username,
            metadata=initial_metadata or {},
            title=title
        )
        return ChatSession.from_zep(session)