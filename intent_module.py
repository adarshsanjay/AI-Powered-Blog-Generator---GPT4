from utils import generate_response


def detect_intent(user_request):

    prompt = f"""
You are an intent detection system.

Classify the user's request into exactly ONE of these categories:

BLOG_GENERATION
SUMMARY
KEYWORD_GENERATION
META_DESCRIPTION
UNKNOWN

User Request:
{user_request}

Return ONLY the category name.
Do not provide an explanation.
"""

    intent = generate_response(prompt)

    return intent.strip().upper()