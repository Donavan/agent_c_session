"""ChatUser model for Agent C Session Manager.

Provides an abstraction over the Zep user object with additional metadata management.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class ChatUser(BaseModel):
    """Represents a chat user in the Agent C system.
    
    Acts as an abstraction over the Zep user object, providing methods for
    managing user data and associated sessions.
    
    Attributes:
        username: Unique identifier for the user
        email: User's email address
        first_name: User's first name
        last_name: User's last name
        metadata: General user metadata
        managed_metadata: Structured metadata with controlled access
    """
    
    username: str = Field(..., description="Unique identifier for the user")
    email: Optional[str] = Field(None, description="User's email address")
    first_name: Optional[str] = Field(None, description="User's first name")
    last_name: Optional[str] = Field(None, description="User's last name")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="General user metadata")
    managed_metadata: Dict[str, str] = Field(default_factory=dict, 
                                           description="Structured metadata with controlled access")
    
    def update_data(self) -> None:
        """Update the non-username parts of a user record in Zep."""
        # Implementation to be added
        pass
    
    def get_sessions(self, limit: int = 10, offset: int = 0) -> List["ChatSession"]:
        """Return a list of chat sessions for this user.
        
        Args:
            limit: Maximum number of sessions to return
            offset: Number of sessions to skip for pagination
            
        Returns:
            List of ChatSession objects belonging to this user
        """
        # Implementation to be added
        pass
    
    def search_sessions(self, query: str, limit: int = 10) -> List["ChatSession"]:
        """Search for chat sessions using the Zep search API.
        
        Args:
            query: Search query string
            limit: Maximum number of sessions to return
            
        Returns:
            List of ChatSession objects matching the search criteria
        """
        # Implementation to be added
        pass
    
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
        # Implementation to be added
        pass
    
    def set_managed_meta(self, namespace: str, key: str, value: Any) -> None:
        """Set a value in the managed metadata under a namespace.
        
        Args:
            namespace: Metadata namespace (e.g., 'tool', 'application')
            key: Metadata key within the namespace
            value: Value to store
        """
        # Implementation to be added
        pass
    
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