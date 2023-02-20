import openai
import os

# Set up OpenAI API credentials
openai.api_key = "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"

# Define book title and chapter names
book_title = "Thinking, Fast and Slow"
chapter_names = ["Chapter 2", "Chapter 3", "Chapter 4"]

# Loop through each chapter and summarize using OpenAI API
for chapter_name in [1:39]
    # Build prompt string
    prompt = f"Summarize Chapter {chapter_name} of {book_title} by Daniel Kahneman 'Thinking, Fast and Slow', using bullet points.\nPlease, refrain from expressing any personal opinion\nAt the end, provide conclusion of the chapter.\n\n"

    # Query OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.7,
        max_tokens=1056,
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
