import json
import os
from transformers import pipeline

def summarize_description(text, char_limit=250):
    """
    Summarizes text to fit within a character limit while retaining coherence.

    Args:
    - text (str): The original description.
    - char_limit (int): Maximum character length of the output.

    Returns:
    - str: A summarized description that fits within the character limit.
    """
    summarizer = pipeline("summarization", model="t5-small")
    
    # Generate a more detailed summary by increasing max_length
    summary = summarizer(text, max_length=min(char_limit // 4, 80), min_length=30, do_sample=False)
    summarized_text = summary[0]['summary_text']
    
    # Ensure it fits the character limit and is coherent
    if len(summarized_text) > char_limit:
        summarized_text = summarized_text[:char_limit]
        if ' ' in summarized_text:
            summarized_text = summarized_text.rsplit(' ', 1)[0]
    
    # Remove any spaces before periods
    summarized_text = summarized_text.replace(" .", ".")
    
    return summarized_text

def process_json_files(input_folder, output_folder, char_limit=250):
    """
    Processes each JSON file in the input folder, summarizes descriptions, and saves them to a .txt file in the output folder.

    Args:
    - input_folder (str): Folder path containing JSON files with original descriptions.
    - output_folder (str): Folder path where processed .txt files will be saved.
    - char_limit (int): Character limit for each description.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate over each JSON file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_summarized.txt")
            
            # Load descriptions from the JSON file
            with open(input_path, 'r') as f:
                descriptions = json.load(f)
            
            # Summarize each description and write to output file
            with open(output_path, 'w') as f:
                for image, description in descriptions.items():
                    summarized_description = summarize_description(description, char_limit=char_limit)
                    f.write(f"{image}: {summarized_description}\n")
            
            print(f"Processed descriptions saved to {output_path}")

# Example usage
if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"
    process_json_files(input_folder, output_folder, char_limit=250)
