from app.seed.seed import generate_topic_content


class DummyResponse:
    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


def test_generate_topic_content_uses_google_api_key(monkeypatch):
    captured = {}

    def fake_post(url, json=None, timeout=15.0):
        captured["url"] = url
        captured["json"] = json
        return DummyResponse({
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": "# Variables\n\n## Overview\n\nVariables store values for later use."}
                        ]
                    }
                }
            ]
        })

    monkeypatch.setattr("app.seed.seed.httpx.post", fake_post)

    result = generate_topic_content(
        "Variables",
        "variables",
        "Store and reuse values in JavaScript",
        api_key="test-key",
        fallback_content="# Fallback",
    )

    assert "# Variables" in result
    assert "## Overview" in result
    assert captured["url"].startswith("https://generativelanguage.googleapis.com")
    assert captured["json"]["contents"][0]["parts"][0]["text"].startswith("Create a detailed Markdown lesson")
