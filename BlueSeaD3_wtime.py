import pandas as pd
import ollama
import os
import re  # For filtering valid responses
import time  # For timing execution

# Start timing
start_time = time.time()


# Define input file paths
input_folder = "input"  # Folder where Atryout.csv is stored
persona_file = os.path.join(input_folder, "persona_prompts_onlynull.csv")
csv_file = os.path.join(input_folder, "Input_SSS_1.csv")

# Load the persona data
persona_df = pd.read_csv(persona_file, delimiter=";")  # Adjust delimiter if necessary

# Load the main CSV file with statements
df = pd.read_csv(csv_file, delimiter=";")  # Adjust delimiter if necessary


# Ensure 'persona' column exists
if "persona" not in persona_df.columns:
    raise ValueError("Missing required column: 'persona' in persona_prompts.csv")


# Ensure required columns exist
required_columns = ["context", "statement", "option_1", "option_2", "option_3"]
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col} in Atryout.csv")

# Prepare lists to store results and summary
results = []
summary_results = []

# Loop through each persona
for _, persona_row in persona_df.iterrows():
    persona = persona_row["persona"]  # Get the persona name from persona_prompts.csv
    print(f"Processing Persona: {persona}\n{'=' * 50}")

    # Initialize counters for this persona
    count_true = 0
    count_false = 0
    count_neither = 0

    # Loop through each row in Atryout.csv
    for index, row in df.iterrows():
        prompt = f"""{persona}, given the context: {row["context"]}, is the statement: {row["statement"]}, 
options: 
a) {row["option_1"]}  
b) {row["option_2"]}  
c) {row["option_3"]}

Choose only 'a', 'b', or 'c' given the context. Do not explain. Do not add extra words. Only output a single letter.
"""

        print(f"Processing Prompt {index+1} for {persona}:\n{prompt}\n")

        # Query the Ollama model
        messages = [
            {"role": "system", "content": "You must strictly answer with only 'a', 'b', or 'c'. No explanations."},
            {"role": "user", "content": prompt}
        ]
        response = ollama.chat(model="llama3.1:8b", messages=messages)

        # Extract answer and filter only valid responses
        raw_answer = response["message"]["content"].strip().lower()  # Normalize case
        match = re.search(r"\b(a|b|c)\b", raw_answer)  # Extract 'a', 'b', or 'c' from the response
        answer = match.group(0) if match else "Invalid response"

        # Map the selected option to its corresponding value
        selected_option_value = None
        if answer == "a":
            selected_option_value = row["option_1"]
        elif answer == "b":
            selected_option_value = row["option_2"]
        elif answer == "c":
            selected_option_value = row["option_3"]
        else:
            selected_option_value = "Invalid response"

        # Count occurrences of each category
        if selected_option_value == "Definitely true":
            count_true += 1
        elif selected_option_value == "Definitely false":
            count_false += 1
        elif selected_option_value == "Neither true nor false":
            count_neither += 1

        # Store individual results
        results.append({
            "persona": persona,  
            "context": row["context"],
            "statement": row["statement"],
            "option_1": row["option_1"],
            "option_2": row["option_2"],
            "option_3": row["option_3"],
            "selected_option": answer,
            "selected_option_value": selected_option_value  
        })

    # Store summary results for this persona
    summary_results.append({
        "context": row["context"],
        "statement": row["statement"],
        "persona": persona,
        "Definitely true": count_true,
        "Definitely false": count_false,
        "Neither true nor false": count_neither
    })

    # Print summary for persona
    print(f"\nSummary for {persona}:")
    print(f"Definitely true: {count_true}")
    print(f"Definitely false: {count_false}")
    print(f"Neither true nor false: {count_neither}")
    print("=" * 50)

# Convert results to DataFrames
output_df = pd.DataFrame(results)
summary_df = pd.DataFrame(summary_results)

# Define output file paths
output_folder = "output"
output_file = os.path.join(output_folder, "output_with_personas_WithNull_SSS.csv")
summary_file = os.path.join(output_folder, "persona_summary_WithNull_SSS.csv")

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Save detailed results to CSV
output_df.to_csv(output_file, index=False, sep=";")  
summary_df.to_csv(summary_file, index=False, sep=";")  

# Stop timing and print execution time
end_time = time.time()
execution_time = end_time - start_time
minutes = int(execution_time // 60)
seconds = int(execution_time % 60)

print(f"\nAll results saved to {output_file}")
print(f"Summary saved to {summary_file}")
print(f"\nTotal execution time: {minutes} minutes and {seconds} seconds ⏳")
