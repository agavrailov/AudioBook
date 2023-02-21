import openai
import os
import random
import string

# Set up OpenAI API credentials
openai.api_key = "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"

# Define book title and chapter names
book_title = "Thinking, Fast and Slow"
chapter_names = ["The Characters of the Story", "Attention and Effort", "The Lazy Controller", "The Associative Machine",
                 "Cognitive Ease", "Norms, Surprises, and Causes", "A Machine for Jumping to Conclusions",
                 "How Judgments Happen", "Answering an Easier Question", "The Law of Small Numbers", "Anchors",
                 "The Science of Availability", "Availability, Emotion, and Risk", "Tom W’s Specialty", "Linda: Less is More",
                 "Causes Trump Statistics", "Regression to the Mean", "Taming Intuitive Predictions", "The Illusion of Understanding",
                 "The Illusion of Validity", "Intuitions Vs. Formulas", "Expert Intuition: When Can We Trust It?", "The Outside View",
                 "The Engine of Capitalism", "Bernoulli’s Errors", "Prospect Theory", "The Endowment Effect", "Bad Events",
                 "The Fourfold Pattern", "Rare Events", "Risk Policies", "Keeping Score", "Reversals", "Frames and Reality",
                 "Two Selves", "Life as a Story", "Experienced Well-Being", "Thinking About Life"]

# Loop through each chapter and summarize using OpenAI API
for i, chapter_name in enumerate(chapter_names):
    # Build prompt string
    # prompt = f"Summarize Chapter {chapter_name} of {book_title} by Daniel Kahneman in 400-600 tokens, highlighting the most important points. Don't mention the book name. Tell it as a story. Put chapter name as a title of the completion.  Don't make an overview or conclusion. Give stories and examples from the book every time when possible."

    # Generate a random string of 5 characters
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))

    # Build prompt string with random string appended
    prompt = f"I am telling a story spread in several chapters to audio book listeners. They listened to other parts already and have context. Explain Chapter {chapter_name} of book {book_title} by Daniel Kahneman in 400-600 tokens, highlighting the most important points. Don't mention the book name. Tell it as a story. Put chapter name as the title of the completion.  Don't make an overview or conclusion. Give stories and examples from the book each paragraph.  {random_string}"

    # Query OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.3,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3
    )
    # Extract summary text from API response
    summary = response.choices[0].text.strip()
    # Save summary to a text file
    filename = f"output/Chapter {i+1} - {chapter_name}.txt"
    with open(filename, "w") as f:
        f.write(summary)
