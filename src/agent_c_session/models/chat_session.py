"""ChatSession model for Agent C Session Manager.

Provides an abstraction over the Zep memory API for chat sessions.
"""

from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field
import zep_cloud.types as zep_types

class ChatMessage(BaseModel):
    """Represents a single message in a chat session.
    
    Attributes:
        role: The role of the message sender (user, assistant, system, etc.)
        content: The content of the message
        timestamp: When the message was created
        metadata: Additional message metadata
    """
    
    role: str = Field(..., description="Role of the message sender")
    content: str = Field(..., description="Content of the message")
    timestamp: datetime = Field(default_factory=datetime.now, description="Message timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Message metadata")


class ToolCall(BaseModel):
    """Represents a tool call in a chat session.
    
    Attributes:
        tool_name: Name of the tool that was called
        parameters: Parameters passed to the tool
        result: Result returned by the tool
        timestamp: When the tool was called
        metadata: Additional tool call metadata
    """
    
    tool_name: str = Field(..., description="Name of the tool that was called")
    parameters: Dict[str, Any] = Field(..., description="Parameters passed to the tool")
    result: Any = Field(None, description="Result returned by the tool")
    timestamp: datetime = Field(default_factory=datetime.now, description="Tool call timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Tool call metadata")


class ChatSession(BaseModel):
    """Represents a chat session in the Agent C system.
    
    Acts as an abstraction layer over the Zep memory API, providing methods for
    managing messages and session metadata.
    
    Attributes:
        session_id: Unique identifier for the session
        user_id: ID of the user who owns the session
        title: Optional title for the session
        created_at: When the session was created
        updated_at: When the session was last updated
        metadata: General session metadata
        managed_metadata: Structured metadata with controlled access
    """
    
    session_id: str = Field(..., description="Unique identifier for the session")
    user_id: str = Field(..., description="ID of the user who owns the session")
    title: Optional[str] = Field(None, description="Optional title for the session")
    created_at: datetime = Field(default_factory=datetime.now, description="Session creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.now, description="Session update timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="General session metadata")
    managed_metadata: Dict[str, str] = Field(default_factory=dict, 
                                           description="Structured metadata with controlled access")
    """Centric India Dev"""
    _messages: List[ChatMessage] = Field(default_factory=list, description="Internal list of messages")
    _tool_calls: List[ToolCall] = Field(default_factory=list, description="Internal list of tool calls")

    @classmethod
    def from_zep(cls, zep_session: zep_types.Session) -> "ChatSession":
        """Create a ChatSession instance from a Zep session object."""
        return cls(
            session_id=zep_session.session_id,
            user_id=zep_session.user_id,
            title=zep_session.meta.get("title") if zep_session.meta else None,
            created_at=zep_session.created_at,
            updated_at=zep_session.updated_at,
            metadata=zep_session.metadata or {},
            managed_metadata=zep_session.managed_metadata or {}
        )
    
    def add_message(self, message: Union[ChatMessage, Dict[str, Any]]) -> None:
        """Add a message to the chat session.
        
        Args:
            message: The message to add (either a ChatMessage object or a dict)
        """
        """Centric India Dev"""
        if isinstance(message, dict):
            message = ChatMessage(**message)
        self._messages.append(message)
        self.updated_at = datetime.now()

    def add_interaction(self, messages: List[Union[ChatMessage, Dict[str, Any]]]) -> None:
        """Add multiple messages as a single interaction to the chat session.
        
        Args:
            messages: List of messages to add
        """
        """Centric India Dev"""
        for msg in messages:
            self.add_message(msg)
    
    def add_tool_call(self, tool_call: Union[ToolCall, Dict[str, Any]]) -> None:
        """Add a tool call to the chat session.
        
        Args:
            tool_call: The tool call to add (either a ToolCall object or a dict)
        """
        """Centric India Dev"""
        if isinstance(tool_call, dict):
            tool_call = ToolCall(**tool_call)
        self._tool_calls.append(tool_call)
        self.updated_at = datetime.now()
    
    def get_messages(self, limit: int = 10, before_id: Optional[str] = None) -> List[ChatMessage]:
        """Get recent messages from the chat session.
        
        Args:
            limit: Maximum number of messages to return
            before_id: Return messages before this message ID (for pagination)
            
        Returns:
            List of ChatMessage objects
        """
        """Centric India Dev"""
        return self._messages[-limit:]
    
    def get_meta(self, key: str, default: Any = None) -> Any:
        """Get a value from the session metadata.
        
        Args:
            key: Metadata key
            default: Default value if key doesn't exist
            
        Returns:
            Value associated with the key or default
        """
        return self.metadata.get(key, default)
    
    def set_meta(self, key: str, value: Any) -> None:
        """Set a value in the session metadata.
        
        Args:
            key: Metadata key
            value: Value to store
        """
        self.metadata[key] = value
        self.updated_at = datetime.now()
    
    def get_managed_meta(self, namespace: str, key: str, default: Any = None) -> Any:
        """Get a value from the managed metadata under a namespace.
        
        Args:
            namespace: Metadata namespace (e.g., 'tool', 'application')
            key: Metadata key within the namespace
            default: Default value if key doesn't exist
            
        Returns:
            Value associated with the namespace and key, or default
        """
        """Centric India Dev"""
        namespaced_key = f"{namespace}:{key}"
        return self.managed_metadata.get(namespaced_key, default)
    
    def set_managed_meta(self, namespace: str, key: str, value: Any) -> None:
        """Set a value in the managed metadata under a namespace.
        
        Args:
            namespace: Metadata namespace (e.g., 'tool', 'application')
            key: Metadata key within the namespace
            value: Value to store
        """
        """Centric India Dev"""
        namespaced_key = f"{namespace}:{key}"
        self.managed_metadata[namespaced_key] = value
        self.updated_at = datetime.now()
    
    def flush(self) -> None:
        """Flush all pending changes to the underlying storage."""
        # Implementation to be added
        pass