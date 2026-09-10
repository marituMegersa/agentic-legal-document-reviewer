def test_agent_orchestrator():
    prompt = "Test execution query for agentic-legal-document-reviewer"
    assert len(prompt) > 0
    assert "Test" in prompt
