def get_user_input():

    print("\nEnter Blog Details")
    print("-" * 30)

    topic = input("Enter Blog Topic: ")
    style = input("Enter Writing Style: ")
    tone = input("Enter Tone: ")

    while True:
        try:
            word_count = int(input("Enter Approximate Word Count: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    return topic, style, tone, word_count


def display_user_input(topic, style, tone, word_count):

    print("\n" + "-" * 35)
    print("Collected Information")
    print("-" * 35)

    print("Blog Topic :", topic)
    print("Style      :", style)
    print("Tone       :", tone)
    print("Words      :", word_count)

    print("-" * 35)