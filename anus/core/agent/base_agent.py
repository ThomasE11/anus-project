"""
Base Agent module that defines the core agent functionality.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class BaseAgent(ABC):
    """
    Abstract base class for all agent implementations.
    
    Defines the common interface that all agents must implement.
    """
    
    def __init__(
        self,
        name: Optional[str] = None,
        **kwargs
    ):
        """
        Initialize a BaseAgent instance.
        
        Args:
            name: Optional name for the agent.
            **kwargs: Additional configuration options for the agent.
        """
        self.name = name or "anus-agent"
        self.config = kwargs
    
    @abstractmethod
    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a task and return the result.
        
        Args:
            task: The task to execute.
            
        Returns:
            A dictionary containing the execution result and metadata.
        """
        pass
    
    def __str__(self) -> str:
        """Return a string representation of the agent."""
        return f"<{self.__class__.__name__} '{self.name}'>"