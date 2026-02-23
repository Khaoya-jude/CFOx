# app/agents/llm.py
from typing import Dict
import json
import openai  # or any other LLM SDK

class LLMPlanner:
    """
    Structured LLM planner for CFOx.
    Returns deterministic JSON with 'tool' + 'args'.
    """

    def __init__(self, model="gpt-4"):
        self.model = model

    def plan(self, prompt: str) -> Dict:
        """
        Ask the LLM to return a JSON plan:
        {
            "tool": "optimize_payables",
            "args": {...}
        }
        """

        # Example OpenAI usage
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0  # deterministic
        )

        text = response.choices[0].message.content

        try:
            plan = json.loads(text)
        except json.JSONDecodeError:
            plan = {"tool": None, "args": {}, "error": "Invalid JSON"}

        return plan
