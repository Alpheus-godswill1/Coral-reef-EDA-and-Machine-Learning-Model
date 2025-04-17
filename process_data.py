import os
import pandas as pd

input_dir = 'data/cleaned_data'
output_dir = 'data/processed_data'

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try:
            df = pd.read_csv(input_path)

            for col in df.columns:
                if 'date' in col.lower():
                    df[col] = pd.to_datetime(df[col], errors='coerce')

            for col in df.select_dtypes(include='object').columns:
                df[col] = pd.to_numeric(df[col], errors='ignore')

            df['row_index'] = range(len(df))

            df.to_csv(output_path, index=False)
            print(f"Processed and saved: {output_path}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
