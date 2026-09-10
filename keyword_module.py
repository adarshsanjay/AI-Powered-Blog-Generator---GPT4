from utils import generate_response


def generate_keywords(blog):

    prompt = f"""
Generate SEO-friendly keywords for the following blog.

Requirements:
- Generate 7 to 10 relevant keywords.
- Make them suitable for SEO.
- Return only the keywords.
- Display one keyword per line.

Blog:
{blog}
"""

    keywords = generate_response(prompt)

    return keywords