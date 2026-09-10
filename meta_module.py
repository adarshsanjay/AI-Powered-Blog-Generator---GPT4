from utils import generate_response


def generate_meta_description(blog):

    prompt = f"""
Generate an SEO-friendly meta description for the following blog.

Requirements:
- Maximum 160 characters.
- Clear and attractive.
- Relevant to the blog.
- SEO-friendly.
- Return only the meta description.

Blog:
{blog}
"""

    meta_description = generate_response(prompt)

    return meta_description