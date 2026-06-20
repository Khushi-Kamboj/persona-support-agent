SENSITIVE_TOPICS = [
    "legal",
    "lawsuit",
    "delete account",
    "account modification",
    "billing dispute"
]

def should_escalate(query):

    query = query.lower()

    for keyword in SENSITIVE_TOPICS:

        if keyword in query:

            return True

    return False

def generate_handoff(
    query,
    persona
):

    return {

        "escalate": True,

        "persona": persona,

        "issue_summary": query,

        "recommended_action":
        "Human Support Review Required"
    }

if __name__ == "__main__":

    query = (
        "I want a refund "
        "for my payment"
    )

    print(
        should_escalate(query)
    )

    print(
        generate_handoff(
            query,
            "Frustrated User"
        )
    )