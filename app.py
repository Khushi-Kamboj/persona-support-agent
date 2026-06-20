# import streamlit as st

from src.main import chat

# st.set_page_config(
#     page_title="Persona Adaptive Support Agent",
#     page_icon="🤖"
# )

# st.title(
#     "🤖 Persona Adaptive Customer Support Agent"
# )

# query = st.text_area(
#     "Enter your support query:"
# )

# if st.button("Submit"):

#     if query:

#         result = chat(query)

#         # Escalation Case
#         if result.get("escalate"):

#             st.error(
#                 "🚨 Human Handoff Required"
#             )

#             st.json(result)

#         # Normal Response
#         else:

#             st.success(
#                 f"Detected Persona: {result['persona']}"
#             )

#             st.markdown(
#                 result["response"]
#             )

import streamlit as st
from src.main import chat

st.title("🤖 Persona Support Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input(
    "Ask your question..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("🤖 Analyzing query..."):
        result = chat(prompt)

    bot_response = result.get(
        "response",
        str(result)
    )

    with st.chat_message("assistant"):
        st.markdown(bot_response)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":bot_response
        }
    )