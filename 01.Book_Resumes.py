import openai
import os

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

# Load prompt.txt from external file
with open("prompt.txt", "r") as f:
    prompt = f.read()

# Loop through each chapter and summarize using OpenAI API
for i, chapter_name in enumerate(chapter_names):
    prompt = prompt.format(chapter_name=chapter_name, book_title=book_title)

    # Query OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.3,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Extract summary text from API response
    summary = response.choices[0].text.strip()
    # Save summary to a text file
    filename = f"output/Chapter {i+1} - {chapter_name}.txt"
    with open(filename, "w") as f:
        f.write(summary)
