from input_module import get_user_input, display_user_input
from blog_module import generate_blog, save_blog
from title_module import generate_titles
from keyword_module import generate_keywords
from summary_module import generate_summary
from meta_module import generate_meta_description
from intent_module import detect_intent


current_blog = ""
current_topic = ""


def generate_complete_blog():

    global current_blog
    global current_topic

    topic, style, tone, word_count = get_user_input()

    display_user_input(
        topic,
        style,
        tone,
        word_count
    )

    print("\nGenerating Blog...")

    current_blog = generate_blog(
        topic,
        style,
        tone,
        word_count
    )

    current_topic = topic

    print("\n" + "=" * 60)
    print("GENERATED BLOG")
    print("=" * 60)

    print(current_blog)

    print("=" * 60)

    save_blog(current_blog)


def show_titles():

    global current_topic

    if current_topic == "":
        topic = input("\nEnter Blog Topic: ")
    else:
        topic = current_topic

    print("\nGenerating Suggested Titles...")

    titles = generate_titles(topic)

    print("\n" + "=" * 60)
    print("SUGGESTED TITLES")
    print("=" * 60)

    print(titles)

    print("=" * 60)


def show_summary():

    global current_blog

    if current_blog == "":
        print("\nPlease generate a blog first.")
        return

    print("\nGenerating Summary...")

    summary = generate_summary(current_blog)

    print("\n" + "=" * 60)
    print("BLOG SUMMARY")
    print("=" * 60)

    print(summary)

    print("=" * 60)


def show_keywords():

    global current_blog

    if current_blog == "":
        print("\nPlease generate a blog first.")
        return

    print("\nGenerating SEO Keywords...")

    keywords = generate_keywords(current_blog)

    print("\n" + "=" * 60)
    print("SEO KEYWORDS")
    print("=" * 60)

    print(keywords)

    print("=" * 60)


def show_meta_description():

    global current_blog

    if current_blog == "":
        print("\nPlease generate a blog first.")
        return

    print("\nGenerating Meta Description...")

    meta = generate_meta_description(current_blog)

    print("\n" + "=" * 60)
    print("META DESCRIPTION")
    print("=" * 60)

    print(meta)

    print("=" * 60)


def intelligent_request():

    global current_blog

    request = input("\nEnter your request: ")

    print("\nDetecting Intent...")

    intent = detect_intent(request)

    print("Detected Intent:", intent)

    if intent == "SUMMARY":

        if current_blog == "":
            print("\nPlease generate a blog first.")
        else:
            show_summary()

    elif intent == "KEYWORD_GENERATION":

        if current_blog == "":
            print("\nPlease generate a blog first.")
        else:
            show_keywords()

    elif intent == "META_DESCRIPTION":

        if current_blog == "":
            print("\nPlease generate a blog first.")
        else:
            show_meta_description()

    elif intent == "BLOG_GENERATION":

        generate_complete_blog()

    else:

        print("\nSorry, I could not understand the request.")


def main():

    print("=" * 60)
    print("AI-POWERED BLOG CONTENT GENERATOR")
    print("Using Ollama + Qwen3:4b")
    print("=" * 60)

    while True:

        print("\nMENU")
        print("1. Generate Complete Blog")
        print("2. Generate Blog Titles")
        print("3. Generate Blog Summary")
        print("4. Generate SEO Keywords")
        print("5. Generate Meta Description")
        print("6. Intelligent Intent Detection")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            generate_complete_blog()

        elif choice == "2":

            show_titles()

        elif choice == "3":

            show_summary()

        elif choice == "4":

            show_keywords()

        elif choice == "5":

            show_meta_description()

        elif choice == "6":

            intelligent_request()

        elif choice == "7":

            print("\nThank you for using the AI Blog Content Generator!")
            print("Exiting the application...")
            break

        else:

            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()