from kovi import KoviClient

# Initialize client with their branch API key
client = KoviClient(api_key="te_live_your_actual_key_here")

try:
    result = client.schedule_interview(
        job_id="JD-AI-7284",
        candidate_name="Alex Mercer",
        candidate_email="alex.mercer@example.com",
        mobile_number="+91-9876543210",
        role="AI Engineer",
        interview_type="System Design",
        evaluation_level="Mid-Level to Senior",
        tech_stack=["Python", "FastAPI", "GCP", "LangChain"],
        duration=15,
        pass_score=6.5,
        deadline_hours=72
    )
    print("✅ Success! Interview Link:", result.get("interviewUrl"))
except Exception as e:
    print("❌ Failed:", e)
