"""ChatUser model for Agent C Session Manager.

Provides an abstraction over the Zep user object with additional metadata management.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
import zep_cloud.types as zep_types

class ChatUser(BaseModel):
    """Represents a chat user in the Agent C system.
    
    Acts as an abstraction over the Zep user object, providing methods for
    managing user data and associated sessions.
    
    Attributes:
        user_id: Unique identifier for the user
        email: User's email address
        first_name: User's first name
        last_name: User's last name
        metadata: General user metadata
        managed_metadata: Structured metadata with controlled access
    """
    
    user_id: str = Field(..., description="Unique identifier for the user")
    email: Optional[str] = Field(None, description="User's email address")
    first_name: Optional[str] = Field(None, description="User's first name")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="General user metadata")
    last_name: Optional[str] = Field(None, description="User's last name")
    zep_user: Optional[zep_types.User] = Field(None, description="Zep user object")

    @classmethod
    def from_zep(cls, zep_user: zep_types.User) -> "ChatUser":
        """Create a ChatUser instance from a Zep user object.

        Args:
            zep_user: Zep user object

        Returns:
            ChatUser instance
        """
        return cls(
            user_id=zep_user.user_id,
            email=zep_user.email,
            first_name=zep_user.first_name,
            last_name=zep_user.last_name,
            metadata=zep_user.metadata or {},
            zep_user=zep_user
        )
    
    def get_sessions(self, limit: int = 10, offset: int = 0) -> List["ChatSession"]:
        """Return a list of chat sessions for this user.
        
        Args:
            limit: Maximum number of sessions to return
            offset: Number of sessions to skip for pagination
            
        Returns:
            List of ChatSession objects belonging to this user
        """
        """Centric India Dev"""
        if not self.zep_user:
            raise ValueError("Zep user object is not loaded")
        sessions = self.zep_user.sessions[offset:offset + limit]
        from src.agent_c_session.models.chat_session import ChatSession
        return [ChatSession.from_zep(session) for session in sessions]
    
    def search_sessions(self, query: str, limit: int = 10) -> List["ChatSession"]:
        """Search for chat sessions using the Zep search API.
        
        Args:
            query: Search query string
            limit: Maximum number of sessions to return
            
        Returns:
            List of ChatSession objects matching the search criteria
        """
        """Centric India Dev"""
        if not self.zep_user or not self.zep_user.sessions:
            raise ValueError("Zep user sessions are not loaded")

        filtered_sessions = [session for session in self.zep_user.sessions if
                             query.lower() in (session.metadata.get("title", "").lower())]

        from src.agent_c_session.models.chat_session import ChatSession
        return [ChatSession.from_zep(session) for session in filtered_sessions[:limit]]
    
    def get_meta(self, key: str, default: Any = None) -> Any:
        """Get a value from the user metadata.
        
        Args:
            key: Metadata key
            default: Default value if key doesn't exist
            
        Returns:
            Value associated with the key or default
        """
        return self.metadata.get(key, default)
    
    def set_meta(self, key: str, value: Any) -> None:
        """Set a value in the user metadata.
        
        Args:
            key: Metadata key
            value: Value to store
        """
        self.metadata[key] = value
    
    def get_managed_meta(self, namespace: str, key: str, default: Any = None) -> Any:
        """Get a value from the managed metadata under a namespace.
        
        Args:
            namespace: Metadata namespace (e.g., 'tool', 'application')
            key: Metadata key within the namespace
            default: Default value if key doesn't exist
            
        Returns:
            Value associated with the namespace and key, or default
        """
        managed = self.metadata.get("managed", {})
        namespace_data = managed.get(namespace, {})
        return namespace_data.get(key, default)
    
    def set_managed_meta(self, namespace: str, key: str, value: Any) -> None:
        """Set a value in the managed metadata under a namespace.
        
        Args:
            namespace: Metadata namespace (e.g., 'tool', 'application')
            key: Metadata key within the namespace
            value: Value to store
        """
        if "managed" not in self.metadata:
            self.metadata["managed"] = {}

        if namespace not in self.metadata["managed"]:
            self.metadata["managed"][namespace] = {}

        self.metadata["managed"][namespace][key] = value
    
    def get_tool_metadata(self, tool_name: str, key: str, default: Any = None) -> Any:
        """Helper method to get tool-specific metadata.
        
        Args:
            tool_name: Name of the tool
            key: Metadata key
            default: Default value if key doesn't exist
            
        Returns:
            Tool-specific metadata value
        """
        return self.get_managed_meta("tool", f"{tool_name}.{key}", default)
    
    def get_application_metadata(self, key: str, default: Any = None) -> Any:
        """Helper method to get application-specific metadata.
        
        Args:
            key: Metadata key
            default: Default value if key doesn't exist
            
        Returns:
            Application-specific metadata value
        """
        return self.get_managed_meta("application", key, default)