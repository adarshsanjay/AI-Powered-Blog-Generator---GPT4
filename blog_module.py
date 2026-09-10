from utils import generate_response


def generate_blog(topic, style, tone, word_count):

    prompt = f"""
Write a complete and well-structured blog.

Blog Topic: {topic}
Writing Style: {style}
Tone: {tone}
Approximate Word Count: {word_count}

Instructions:
1. Give the blog an attractive title.
2. Write a clear introduction.
3. Use suitable headings and subheadings.
4. Explain the topic clearly.
5. Include relevant examples where appropriate.
6. Maintain the requested writing style.
7. Maintain the requested tone.
8. Write a proper conclusion.
9. Keep the blog close to {word_count} words.

Generate only the blog content.
"""

    blog = generate_response(prompt)

    return blog

def save_blog(blog):

    with open("outputs/generated_blog.txt", "w", encoding="utf-8") as file:
        file.write(blog)

    print("\nBlog saved successfully in outputs/generated_blog.txt")