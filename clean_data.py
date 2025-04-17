import os
import pandas as pd

# Define paths
input_dir = 'data/original_data'
output_dir = 'data/cleaned_data'


os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try:
            df = pd.read_csv(input_path, low_memory=False)

            df.columns = [col.strip() for col in df.columns]  
            df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x) 
            df.drop_duplicates(inplace=True)  

            df.to_csv(output_path, index=False)
            print(f"Cleaned and saved: {output_path}")

        except Exception as e:
            print(f"Failed to process {filename}: {e}")
