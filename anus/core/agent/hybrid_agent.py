"""
Hybrid Agent module that combines single and multi-agent capabilities.

This agent can dynamically switch between single and multi-agent modes based on task complexity.
"""

import logging
import re
from typing import Dict, Any, List, Tuple, Optional

from anus.core.agent.tool_agent import ToolAgent

class HybridAgent(ToolAgent):
    """
    A hybrid agent that can switch between single and multi-agent modes.
    
    This agent assesses task complexity and chooses the appropriate mode.
    """
    
    def __init__(
        self,
        name: Optional[str] = None,
        max_iterations: int = 10,
        tools: Optional[List[str]] = None,
        **kwargs
    ):
        """
        Initialize a HybridAgent instance.
        
        Args:
            name: Optional name for the agent.
            max_iterations: Maximum number of thought-action cycles to perform.
            tools: Optional list of tool names to load.
            **kwargs: Additional configuration options for the agent.
        """
        super().__init__(name=name, max_iterations=max_iterations, tools=tools, **kwargs)
        self.mode = "auto"
        
        # Specialized agents for multi-agent mode
        self.specialized_agents = {
            "researcher": ToolAgent(name="researcher", tools=tools),
            "planner": ToolAgent(name="planner", tools=tools),
            "executor": ToolAgent(name="executor", tools=tools),
            "critic": ToolAgent(name="critic", tools=tools)
        }
    
    def _assess_complexity(self, task: str) -> float:
        """
        Assess the complexity of a task.
        
        Args:
            task: The task to assess.
            
        Returns:
            A float between 0 and 1 representing task complexity.
        """
        # Simple heuristic for complexity assessment
        complexity_indicators = [
            "research", "analyze", "investigate", "compare", "evaluate",
            "generate", "create", "synthesize", "design", "develop",
            "multi-step", "complex", "in-depth", "comprehensive"
        ]
        
        # Count occurrences of complexity indicators
        count = sum(1 for indicator in complexity_indicators if indicator in task.lower())
        
        # Normalize to a value between 0 and 1
        complexity = min(1.0, count / 5)
        
        return complexity
    
    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a task using single or multi-agent mode based on complexity.
        
        Args:
            task: The task to execute.
            
        Returns:
            A dictionary containing the execution result and metadata.
        """
        # Assess task complexity
        complexity = self._assess_complexity(task)
        
        # Determine execution mode
        if self.mode == "auto":
            mode = "multi" if complexity > 0.5 else "single"
        else:
            mode = self.mode
        
        # Execute based on selected mode
        if mode == "single":
            return super().execute(task)
        else:
            return self._execute_multi_agent(task)
    
    def _execute_multi_agent(self, task: str) -> Dict[str, Any]:
        """
        Execute a task using multiple specialized agents.
        
        Args:
            task: The task to execute.
            
        Returns:
            A dictionary containing the execution result and metadata.
        """
        # Simple implementation of multi-agent execution
        results = {}
        
        # Have each agent process the task
        for role, agent in self.specialized_agents.items():
            agent_task = f"As a {role}, {task}"
            results[role] = agent.execute(agent_task)
        
        # Combine results
        return {
            "task": task,
            "answer": f"Multi-agent execution of: {task}",
            "mode": "multi",
            "agent_results": results
        }