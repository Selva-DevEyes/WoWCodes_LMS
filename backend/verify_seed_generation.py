import sys
sys.path.append('.')
import app.seed.seed as seed

class R:
    def raise_for_status(self):
        return None
    def json(self):
        return {
            'candidates': [
                {'content': {'parts': [{'text': '# Variables\n\n## Overview\n\nVariables store values for later use.'}]}}
            ]
        }


def fake_post(url, json=None, timeout=15.0):
    print(url)
    return R()

seed.httpx.post = fake_post
result = seed.generate_topic_content('Variables', 'variables', 'Store and reuse values in JavaScript', api_key='test-key', fallback_content='# Fallback')
print(result)
