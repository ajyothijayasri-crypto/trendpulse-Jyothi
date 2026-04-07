# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load analysed CSV
print("Loading analysed data...")
df = pd.read_csv("trends_analysed.csv")

# Create outputs folder if not exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -------------------------------
# Chart 1: Top 10 Stories by Score
# -------------------------------
print("Creating Top 10 stories chart...")

top10 = df.sort_values(by="score", ascending=False).head(10)

# shorten long titles
top10["title"] = top10["title"].apply(lambda x: x[:50])

plt.figure(figsize=(12, 7))
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# -------------------------------
# Chart 2: Stories per Category
# -------------------------------
print("Creating category chart...")

category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()


# -------------------------------
# Chart 3: Score vs Comments
# -------------------------------
print("Creating scatter plot...")

plt.figure(figsize=(8, 6))

# separate popular and non-popular
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.legend()

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()


# -------------------------------
# Bonus: Dashboard
# -------------------------------
print("Creating dashboard...")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Chart 1
axes[0, 0].barh(top10["title"], top10["score"])
axes[0, 0].set_title("Top 10 stories")
axes[0,0].invert_yaxis()

# Chart 2
axes[0, 1].bar(category_counts.index, category_counts.values)
axes[0, 1].set_title("Categories")

# Chart 3
axes[1, 0].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[1, 0].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[1, 0].set_title("Score vs Comments")
axes[1, 0].legend()

# empty box (looks natural)
axes[1, 1].axis("off")

plt.suptitle("TrendPulse Dashboard")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()


print("All charts created and saved successfully!")
