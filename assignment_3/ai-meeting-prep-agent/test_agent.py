from agent import MeetingPrepAgent


agent = MeetingPrepAgent()


response = agent.prepare_meeting(
    client_name="Acme Corp"
)


print("\n========== MEETING BRIEF ==========\n")

print(response)