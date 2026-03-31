"""
AI & External API Integrations (ai_service.py)
==============================================
Abstracts third-party boundaries (like OpenAI, Google Vertex, Pinecone, or Stripe).
If an LLM changes its endpoints, or if you swap embedding engines, you only rewrite logic
here, ensuring your API Controllers (`users.py`, etc.) are completely shielded from vendor churn.
"""

def generate_embedding(text: str) -> list[float]:
    """Mock generating an embedding for text data."""
    return [0.1, 0.2, -0.3, 0.5]


def call_llm(prompt: str) -> str:
    """Mock calling a Large Language Model."""
    return f"AI Response to: {prompt}"
