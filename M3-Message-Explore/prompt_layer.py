SYSTEM_PROMPT = """
You are an AI academic assistant.
Provide structured and concise answers.
Avoid hallucinations.
"""


def build_prompt(user_input):
    return f"""
{SYSTEM_PROMPT}

Answer the question clearly.

Question:
{user_input}

Provide:
- Clear explanation
- Example
- Key insights
"""
