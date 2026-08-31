from google import genai

from config import GEMINI_API_KEY

from tools.document_search import search_client_documents
from tools.meeting_notes import search_meeting_notes

from tools.memory_tool import (
    retrieve_client_memory,
    save_client_memory
)


class MeetingPrepAgent:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )


    # -----------------------------------------
    # AUTOMATIC LONG-TERM MEMORY DETECTION
    # -----------------------------------------

    def save_important_information(
        self,
        client_name,
        user_message
    ):

        prompt = f"""
You are managing long-term memory for an AI client meeting preparation system.

CLIENT:
{client_name}

USER MESSAGE:
{user_message}

Determine whether the user message contains NEW and IMPORTANT factual
information about the client that should be remembered for future meetings.

Important information includes:

- Client preferences
- New requirements
- Deadlines
- Concerns
- Decisions
- Risks
- Communication preferences
- Project changes
- Important stakeholder information

Do NOT save:

- General questions
- Greetings
- Requests for information
- Opinions without factual client information

If the message contains important information, respond EXACTLY in this format:

YES: <short factual memory>

Example:

YES: Acme Corp prefers weekly project status updates.

If the message does NOT contain important information, respond EXACTLY:

NO
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        result = response.text.strip()

        # Check if important information was detected
        if result.startswith("YES:"):

            memory = result.replace(
                "YES:",
                "",
                1
            ).strip()

            # Save information to SQLite long-term memory
            save_client_memory(
                client_name,
                memory
            )

            return memory

        return None


    # -----------------------------------------
    # PREPARE MEETING BRIEF
    # -----------------------------------------

    def prepare_meeting(
        self,
        client_name,
        conversation_context=""
    ):

        # Tool 1: Search client documents
        client_information = search_client_documents(
            f"""
            Important information, current project status,
            priorities, issues, risks and stakeholders
            for {client_name}
            """
        )

        # Tool 2: Search previous meeting notes
        meeting_information = search_meeting_notes(
            f"""
            Previous meetings, open action items,
            concerns, decisions and follow-ups
            for {client_name}
            """
        )

        # Tool 3: Retrieve long-term memory
        memory_information = retrieve_client_memory(
            client_name
        )

        prompt = f"""
You are an AI Meeting Preparation Agent.

Your task is to prepare a concise and useful meeting brief.

CLIENT:
{client_name}

CURRENT CONVERSATION CONTEXT:
{conversation_context}

CLIENT DOCUMENTS:
{client_information}

PREVIOUS MEETING NOTES:
{meeting_information}

LONG-TERM MEMORY:
{memory_information}

Based ONLY on the information provided above, create a professional
meeting brief.

Use exactly these sections:

## 1. CLIENT OVERVIEW

## 2. CURRENT PROJECT STATUS

## 3. KEY TALKING POINTS

## 4. OPEN ACTION ITEMS

## 5. CLIENT CONCERNS

## 6. RISKS TO DISCUSS

## 7. RECOMMENDED NEXT STEPS

Keep the response concise, practical, and useful for someone
entering a client meeting in 10 minutes.
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text


    # -----------------------------------------
    # ANSWER FOLLOW-UP QUESTIONS
    # -----------------------------------------

    def answer_follow_up(
        self,
        client_name,
        question,
        conversation_context=""
    ):

        # -------------------------------------
        # STEP 1: CHECK FOR IMPORTANT MEMORY
        # -------------------------------------

        saved_memory = self.save_important_information(
            client_name,
            question
        )


        # -------------------------------------
        # STEP 2: TOOL 1 - DOCUMENT SEARCH
        # -------------------------------------

        client_information = search_client_documents(
            f"{client_name}: {question}"
        )


        # -------------------------------------
        # STEP 3: TOOL 2 - MEETING NOTES
        # -------------------------------------

        meeting_information = search_meeting_notes(
            f"{client_name}: {question}"
        )


        # -------------------------------------
        # STEP 4: TOOL 3 - LONG-TERM MEMORY
        # -------------------------------------

        memory_information = retrieve_client_memory(
            client_name
        )


        # -------------------------------------
        # STEP 5: GENERATE RESPONSE
        # -------------------------------------

        prompt = f"""
You are an AI Client Meeting Preparation Agent.

CLIENT:
{client_name}

CURRENT CONVERSATION:
{conversation_context}

USER QUESTION OR MESSAGE:
{question}

RELEVANT CLIENT DOCUMENTS:
{client_information}

RELEVANT MEETING NOTES:
{meeting_information}

LONG-TERM MEMORY:
{memory_information}

Answer the user's question clearly and concisely.

IMPORTANT RULES:

1. Use the conversation context to understand references such as:
   - they
   - their
   - them
   - that issue
   - the project

2. Use the retrieved information to provide accurate answers.

3. If the user provided NEW client information, acknowledge it naturally
   and use it when relevant.

4. Only use the information provided above.

5. If the required information is unavailable, clearly say that you
   do not have enough information.

Do not invent information.
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text