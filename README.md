🤖 AI-Powered Blog Content Generator

An AI-powered Blog Content Generator developed using **Python, Ollama, and Qwen3:4b**.

This application uses a Large Language Model (LLM) to automatically generate high-quality blog content based on user requirements such as the **topic, writing style, tone, and approximate word count**.

The system is designed using a modular architecture where different components handle blog generation, title generation, SEO keyword generation, summarization, meta description generation, and intelligent intent detection.

---

📌 Project Overview

Writing high-quality blog content requires time and effort. This project automates the content generation process using Artificial Intelligence.

The user provides information about the desired blog, and the application communicates with the **Qwen3:4b Large Language Model through Ollama** to generate the requested content.

The application can generate:

- Complete blogs
- Attractive blog titles
- SEO-friendly keywords
- Blog summaries
- SEO meta descriptions
- Intelligent responses based on detected user intent

The application also saves generated blogs to a text file.

---

✨ Features

 📝 Complete Blog Generation

Users can generate a complete blog by providing:

- Blog Topic
- Writing Style
- Tone
- Approximate Word Count

The AI generates a structured blog containing:

- A suitable title
- Introduction
- Headings and subheadings
- Main content
- Relevant explanations
- Conclusion

---

 📰 Blog Title Generator

The application generates **five attractive and engaging titles** based on the selected blog topic.

---

 🔍 SEO Keyword Generator

The generated blog is analyzed by the AI to produce relevant **SEO-friendly keywords**.

These keywords can help improve the discoverability of blog content in search engines.

---

 📄 Blog Summary Generator

The application generates a concise summary of approximately **100 words** containing the important ideas from the generated blog.

---

 🌐 SEO Meta Description Generator

The system generates an SEO-friendly meta description with a maximum length of approximately **160 characters**.

---

 🧠 Intelligent Intent Detection

The application uses the LLM to identify the user's requested operation.

Supported intents include:

- `BLOG_GENERATION`
- `SUMMARY`
- `KEYWORD_GENERATION`
- `META_DESCRIPTION`

For example:

User: Summarize this blog
Detected Intent: SUMMARY

Technologies Used

- Python

- Ollama

- Qwen3:4b

Installation

Clone the repository:

git clone <repository-url>

Create a virtual environment:

python3 -m venv venv

Activate the virtual environment:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the Application

Make sure Ollama is running:

ollama serve

Then run:

python main.py
