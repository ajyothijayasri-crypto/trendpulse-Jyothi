import pandas as pd
import numpy as np

# STEP 1: Load CSV file
df = pd.read_csv("trends_clean.csv")

print("Loaded data:", df.shape)

# STEP 2: First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# STEP 3: Basic averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", int(avg_score))
print("Average comments:", int(avg_comments))

# STEP 4: NumPy statistics
scores = df["score"].values

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

print("\n--- NumPy Stats ---")
print("Mean score:", int(mean_score))
print("Median score:", int(median_score))
print("Std deviation:", int(std_score))
print("Max score:", int(max_score))
print("Min score:", int(min_score))

# STEP 5: Category with most stories
top_category = df["category"].value_counts().idxmax()
top_count = df["category"].value_counts().max()

print("\nMost stories in:", top_category, f"({top_count} stories)")

# STEP 6: Most commented story
max_comments_row = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:")
print(f'"{max_comments_row["title"]}" - {max_comments_row["num_comments"]} comments')

# STEP 7: Add new columns

# engagement = num_comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = True if score > average score
df["is_popular"] = df["score"] > avg_score

# STEP 8: Save file
df.to_csv("trends_analysed.csv", index=False)

print("\nSaved to trends_analysed.csv")
