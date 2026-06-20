import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

PERSONA_PROMPTS = {

    "Technical Expert": """
        You are a senior technical support engineer.

        Use ONLY the provided context.

        Respond in this format:

        ## Issue
        (1-2 lines)

        ## Possible Causes
        - Cause 1
        - Cause 2
        - Cause 3

        ## Resolution Steps
        1. Step 1
        2. Step 2
        3. Step 3

        Keep response under 200 words.

        Do NOT repeat information.
        Do NOT explain concepts in depth unless asked.
        """,

    "Frustrated User": """
        You are an empathetic support agent.

        Start with empathy.

        Format:

        ## What Happened
        (Short explanation)

        ## What To Do
        1. Step 1
        2. Step 2
        3. Step 3

        Keep response under 150 words.
        """,

   "Business Executive": """
    You are an executive support advisor.

    Format:

    ## Issue

    ## Business Impact

    ## Recommended Action

    ## Estimated Resolution

    Keep response under 100 words.
    """
}

def generate_response(
    user_query,
    persona,
    retrieved_chunks
):

    context = "\n\n".join(
        [
            chunk["text"]
            for chunk in retrieved_chunks
        ]
    )

    prompt = f"""
        {PERSONA_PROMPTS[persona]}

        Knowledge Base Context:
        {context}

        User Question:
        {user_query}

        IMPORTANT RULES:
        - Use ONLY the provided context.
        - Do not make up information.
        - Use markdown headings.
        - Keep the answer concise.
        - Do not repeat information.
        - Mention only the most relevant troubleshooting steps.
        - If information is unavailable in the context, say:
        "I couldn't find enough information in the knowledge base."
        """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

if __name__ == "__main__":

    sample_chunks = [

        {
            "text":
            """
            Password Reset Guide

            Step 1:
            Click Forgot Password

            Step 2:
            Verify Email
            """
        }
    ]

    answer = generate_response(

        user_query=
        "How do I reset my password?",

        persona=
        "Frustrated User",

        retrieved_chunks=
        sample_chunks
    )

    print(answer)