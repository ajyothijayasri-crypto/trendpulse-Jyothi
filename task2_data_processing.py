import pandas as pd
import json

# STEP 1: Load JSON file
file_path = "data.json" # <-- make sure this file is in Desktop

with open(file_path, "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)

print("Loaded rows:", len(df))


# STEP 2: Remove duplicates
df = df.drop_duplicates(subset="post_id")
print("After removing duplicates:", len(df))


# STEP 3: Remove missing values
df = df.dropna(subset=["post_id", "title", "score", "num_comments"])
print("After removing nulls:", len(df))


# STEP 4: Convert safely (VERY IMPORTANT)
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

# Remove invalid values after conversion
df = df[df["score"].notna()]
df = df[df["num_comments"].notna()]

# Convert to integer
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# STEP 5: Remove low score (<5)
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))


# STEP 6: Remove extra spaces in title
df["title"] = df["title"].str.strip()


# STEP 7: Save as CSV
output_file = "trends_clean.csv"
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} rows to {output_file}")


# STEP 8: Summary (stories per category)
print("\nStories per category:")
print(df["category"].value_counts())

