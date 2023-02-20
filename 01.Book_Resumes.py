import openai
import os

# Set up OpenAI API credentials
openai.api_key = "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"

# Define book title and chapter names
book_title = "Thinking, Fast and Slow"
chapter_names = ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 39"]

# Loop through each chapter and summarize using OpenAI API
for chapter_name in chapter_names:
    # Build prompt string
    #prompt = f"Summarize {chapter_name} of {book_title} by Daniel Kahneman. Use bullets and nothing more. Don't express opinion, Don't provide a conclusion."
    prompt = f"Summarize {chapter_name} of {book_title} by Daniel Kahneman in a bullet-point format for optimal listening comprehension, without expressing an opinion or drawing conclusions?"
    # Query OpenAI API
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    )
    # Extract summary text from API response
    summary = response.choices[0].text.strip()
    # Save summary to a text file
    filename = f"../output/{chapter_name}.txt"
    with open(filename, "w") as f:
        f.write(summary)
