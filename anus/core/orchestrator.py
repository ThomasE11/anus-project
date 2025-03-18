"""
Orchestrator module for the ANUS framework.

This module contains the agent orchestration system that manages agent 
lifecycle and coordinates task execution across multiple agents.

Behind every successful ANUS is a well-designed Orchestrator.
"""

from typing import Dict, List, Any, Optional
import yaml
import os

from anus.core.agent.tool_agent import ToolAgent

class AgentOrchestrator:
    """
    Coordinates agents and manages their lifecycle.
    
    This is a simplified implementation for the demo.
    """
    
    def __init__(self, config_path: str = "config.yaml"):
        """
        Initialize an AgentOrchestrator instance.
        
        Args:
            config_path: Path to the configuration file.
        """
        self.config = self._load_config(config_path)
        self.primary_agent = self._create_primary_agent()
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """
        Load configuration from a file.
        
        Args:
            config_path: Path to the configuration file.
            
        Returns:
            A dictionary containing the configuration.
        """
        try:
            with open(config_path, "r") as f:
                config = yaml.safe_load(f)
            return config
        except Exception as e:
            print(f"Warning: Failed to load config from {config_path}: {e}")
            print("Using default configuration.")
            return {
                "agent": {
                    "mode": "single",
                    "max_iterations": 10,
                    "verbose": True
                },
                "tools": {
                    "enabled": ["calculator"]
                }
            }
    
    def _create_primary_agent(self) -> ToolAgent:
        """
        Create the primary agent based on configuration.
        
        Returns:
            A ToolAgent instance.
        """
        # Get enabled tools from config
        tools = self.config.get("tools", {}).get("enabled", [])
        
        # Create the agent
        agent = ToolAgent(
            name="primary-agent",
            max_iterations=self.config.get("agent", {}).get("max_iterations", 10),
            tools=tools
        )
        
        return agent
    
    def execute_task(self, task: str, mode: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute a task using the appropriate agent(s).
        
        Args:
            task: The task to execute.
            mode: The execution mode (single or multi).
            
        Returns:
            A dictionary containing the execution result and metadata.
        """
        # Use the primary agent to execute the task
        return self.primary_agent.execute(task)
