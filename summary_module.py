from utils import generate_response


def generate_summary(blog):

    prompt = f"""
Generate a short summary of approximately 100 words for the following blog.

Requirements:
- Keep the summary clear and concise.
- Include the main ideas of the blog.
- Keep it close to 100 words.
- Return only the summary.

Blog:
{blog}
"""

    summary = generate_response(prompt)

    return summary