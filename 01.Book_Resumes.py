import openai
import os

# Set up OpenAI API credentials
openai.api_key = "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"

# Define book title and chapter names
book_title = "Thinking, Fast and Slow"
chapter_names = [f"Chapter {i}" for i in range(1, 40)]


# Loop through each chapter and summarize using OpenAI API
for chapter_name in chapter_names:
    # Build prompt string
    prompt = f"Summarize {chapter_name} of {book_title} by Daniel Kahneman in 400-600 tokens, highlighting the most important points. Start with the name of the chapter, don't mention the book. Speak as you are the author, but do not use first person. Tell it as story."

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
    filename = f"../output/{chapter_name}.txt"
    with open(filename, "w") as f:
        f.write(summary)
