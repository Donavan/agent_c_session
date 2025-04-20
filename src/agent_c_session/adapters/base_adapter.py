"""Base adapter for the Agent C Session Manager.

Provides a base class for adapters that translate between different message formats.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseAdapter(ABC):
    """Base class for message format adapters.
    
    Provides methods for translating between application message formats and
    external storage formats (like Zep).
    """
    
    @abstractmethod
    def to_external_format(self, messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Convert application messages to the external storage format.
        
        Args:
            messages: List of messages in the application format
            
        Returns:
            List of messages in the external storage format
        """
        pass
    
    @abstractmethod
    def to_application_format(self, messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Convert external storage messages to the application format.
        
        Args:
            messages: List of messages in the external storage format
            
        Returns:
            List of messages in the application format
        """
        pass