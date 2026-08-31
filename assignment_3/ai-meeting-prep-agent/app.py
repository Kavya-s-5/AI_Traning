import streamlit as st

from agent import MeetingPrepAgent
from memory.short_term_memory import ShortTermMemory


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="AI Meeting Prep Agent",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------
# INITIALIZE SESSION STATE
# --------------------------------

if "short_term_memory" not in st.session_state:
    st.session_state.short_term_memory = ShortTermMemory()

if "agent" not in st.session_state:
    st.session_state.agent = MeetingPrepAgent()

if "active_client" not in st.session_state:
    st.session_state.active_client = ""

if "meeting_brief" not in st.session_state:
    st.session_state.meeting_brief = ""


# --------------------------------
# HEADER
# --------------------------------

st.title("🤖 AI Client Meeting Preparation Agent")

st.write(
    "Prepare for client meetings using RAG, memory, and AI-powered tools."
)

st.divider()


# --------------------------------
# SIDEBAR
# --------------------------------

with st.sidebar:

    st.header("📋 Meeting Details")

    client_name = st.text_input(
        "Client Name",
        placeholder="Example: Acme Corp"
    )

    if st.button("🗑️ Clear Conversation"):

        st.session_state.short_term_memory.clear_memory()

        st.session_state.meeting_brief = ""

        st.session_state.active_client = ""

        st.success("Conversation cleared!")

        st.rerun()


# --------------------------------
# PREPARE MEETING BRIEF
# --------------------------------

if client_name:

    if st.button("🚀 Prepare Meeting Brief"):

        with st.spinner(
            "🔎 Searching documents, meeting notes, and memory..."
        ):

            conversation_context = (
                st.session_state
                .short_term_memory
                .get_context()
            )

            response = (
                st.session_state.agent.prepare_meeting(
                    client_name=client_name,
                    conversation_context=conversation_context
                )
            )

            # Save client
            st.session_state.active_client = client_name

            # Save meeting brief
            st.session_state.meeting_brief = response

            # Save in short-term memory
            st.session_state.short_term_memory.add_message(
                "user",
                f"Prepare me for my meeting with {client_name}"
            )

            st.session_state.short_term_memory.add_message(
                "assistant",
                response
            )

        st.rerun()


# --------------------------------
# DISPLAY MEETING BRIEF
# --------------------------------

if st.session_state.meeting_brief:

    st.subheader("📋 Meeting Brief")

    st.markdown(
        st.session_state.meeting_brief
    )


# --------------------------------
# CHAT SECTION
# --------------------------------

if st.session_state.active_client:

    st.divider()

    st.subheader(
        f"💬 Ask Questions About {st.session_state.active_client}"
    )

    # Show conversation
    for message in (
        st.session_state
        .short_term_memory
        .get_conversation()
    ):

        if message["role"] == "user":

            with st.chat_message("user"):
                st.write(message["content"])

        else:

            with st.chat_message("assistant"):
                st.write(message["content"])


    # User follow-up question
    question = st.chat_input(
        f"Ask something about {st.session_state.active_client}..."
    )


    if question:

        # Display user question
        with st.chat_message("user"):
            st.write(question)


        # Save user question
        st.session_state.short_term_memory.add_message(
            "user",
            question
        )


        # Get updated conversation context
        conversation_context = (
            st.session_state
            .short_term_memory
            .get_context()
        )


        # Generate AI response
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = (
                    st.session_state.agent.answer_follow_up(
                        client_name=st.session_state.active_client,
                        question=question,
                        conversation_context=conversation_context
                    )
                )

                st.write(response)


        # Save AI response
        st.session_state.short_term_memory.add_message(
            "assistant",
            response
        )


# --------------------------------
# ARCHITECTURE INFO
# --------------------------------

with st.expander("🔍 How the AI Agent Works"):

    st.markdown("""
### Agentic Workflow

1. **User Request**
2. 🔎 Document Search Tool
3. 📝 Meeting Notes Tool
4. 🧠 Long-Term Memory Tool
5. 📚 RAG Retrieval using ChromaDB
6. 🤖 Gemini generates the response
7. 💬 Short-Term Memory maintains conversation context
""")