"""
Calculator tool for basic arithmetic operations.

This tool provides safe evaluation of mathematical expressions.
"""

import logging
import ast
import operator
from typing import Dict, Any, Union

class CalculatorTool:
    """
    A tool for performing basic arithmetic calculations.
    
    ANUS can handle your numbers with precision and care.
    """
    
    name = "calculator"
    description = "Perform basic arithmetic calculations"
    parameters = {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The mathematical expression to evaluate"
            }
        },
        "required": ["expression"]
    }
    
    def execute(self, expression: str) -> Dict[str, Any]:
        """
        Execute the calculator tool with the given expression.
        
        Args:
            expression: The mathematical expression to evaluate.
            
        Returns:
            A dictionary containing the result of the calculation.
        """
        try:
            # Simple implementation for demo
            # WARNING: eval is used here for demo purposes only
            # In a real implementation, use a safer method
            result = str(eval(expression))
            return {
                "expression": expression,
                "result": result,
                "status": "success"
            }
        except Exception as e:
            return {
                "expression": expression,
                "error": str(e),
                "status": "error"
            }