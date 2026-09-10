from utils import generate_response


def generate_titles(topic):

    prompt = f"""
Generate exactly 5 attractive and engaging blog titles for the following topic:

{topic}

Requirements:
- Make the titles interesting and professional.
- Keep them relevant to the topic.
- Return only a numbered list of 5 titles.
"""

    titles = generate_response(prompt)

    return titles