from src.classifier import classify_persona
from src.generator import generate_response
from src.rag_pipeline import retrieve_context
from src.escalator import (
    should_escalate,
    generate_handoff
)


def chat(query):

    # Step 1: Persona Classification
    persona_result = classify_persona(query)

    persona = persona_result["persona"]

    # Step 2: Escalation Check
    if should_escalate(query):

        return generate_handoff(
            query,
            persona
        )

    # Step 3: Retrieve Context
    retrieved_chunks = retrieve_context(
        query
    )

    # Step 4: Generate Response
    response = generate_response(
        user_query=query,
        persona=persona,
        retrieved_chunks=retrieved_chunks
    )

    return {
        "persona": persona,
        "response": response
    }

if __name__ == "__main__":

    query = input("User: ")

    result = chat(query)

    print("\nResult:\n")

    print(result)