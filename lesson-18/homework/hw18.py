1. 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
df = pd.read_csv('C:\\Users\\Ziyada\\Desktop\\python\\tackoverflow_qa.csv')
df.head() 
print("\nExercise 1: Questions created before 2014")
print("=" * 50)
if 'creationdate' in df.columns:
    before_2014 = df[df['creationdate'] < '2014-01-01']
    print(f"Found {len(before_2014)} questions created before 2014")
    if len(before_2014) > 0:
        print(before_2014[['id', 'creationdate', 'title', 'score']].head())
else:
    print("No creationdate column found")

# Exercise 2: Find all questions with a score more than 50
print("\nExercise 2: Questions with score > 50")
print("=" * 50)
if 'score' in df.columns:
    high_score = df[df['score'] > 50]
    print(f"Found {len(high_score)} questions with score > 50")
    if len(high_score) > 0:
        print(high_score[['id', 'title', 'score']].head())
else:
    print("No score column found")

# Exercise 3: Find all questions with a score between 50 and 100
print("\nExercise 3: Questions with score between 50 and 100")
print("=" * 50)
if 'score' in df.columns:
    score_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]
    print(f"Found {len(score_50_100)} questions with score between 50 and 100")
    if len(score_50_100) > 0:
        print(score_50_100[['id', 'title', 'score']].head())
else:
    print("No score column found")

# Exercise 4: Find all questions answered by Scott Boston
print("\nExercise 4: Questions answered by Scott Boston")
print("=" * 50)
answer_columns = ['ans_name', 'answer_name', 'answered_by']
ans_col = None
for col in answer_columns:
    if col in df.columns:
        ans_col = col
        break

if ans_col:
    scott_boston_answers = df[df[ans_col] == 'Scott Boston']
    print(f"Found {len(scott_boston_answers)} questions answered by Scott Boston")
    if len(scott_boston_answers) > 0:
        print(scott_boston_answers[['id', 'title', ans_col, 'score']].head())
else:
    print("No answer name column found")

# Exercise 5: Find all questions answered by specific users
print("\nExercise 5: Questions answered by target users")
print("=" * 50)
if ans_col:
    target_users = ['Scott Boston', 'Unutbu', 'Mike Pennington', 'Demitri', 'doug']
    user_answers = df[df[ans_col].isin(target_users)]
    print(f"Found {len(user_answers)} questions answered by target users")
    if len(user_answers) > 0:
        print(f"Breakdown by user:")
        print(user_answers[ans_col].value_counts())
        print(f"\nSample questions:")
        print(user_answers[['id', 'title', ans_col, 'score']].head())
else:
    print("No answer name column found")

# Exercise 6: Complex filtering - Date range, specific answerer, and score
print("\nExercise 6: Complex filtering (Mar-Oct 2014, Unutbu, score < 5)")
print("=" * 50)
if all(col in df.columns for col in ['creationdate', ans_col, 'score']):
    complex_filter = df[
        (df['creationdate'] >= '2014-03-01') & 
        (df['creationdate'] <= '2014-10-31') & 
        (df[ans_col] == 'Unutbu') & 
        (df['score'] < 5)
    ]
    print(f"Found {len(complex_filter)} questions matching all criteria")
    if len(complex_filter) > 0:
        print(complex_filter[['id', 'creationdate', 'title', 'score', ans_col]])
else:
    print("Required columns not found for complex filtering")

# Exercise 7: OR condition filtering
print("\nExercise 7: Questions with score 5-10 OR view count > 10,000")
print("=" * 50)
if all(col in df.columns for col in ['score', 'viewcount']):
    score_or_views = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
    print(f"Found {len(score_or_views)} questions matching the criteria")
    if len(score_or_views) > 0:
        print(score_or_views[['id', 'title', 'score', 'viewcount']].head())
else:
    print("Required columns not found")

# Exercise 8: Negation filtering
print("\nExercise 8: Questions NOT answered by Scott Boston")
print("=" * 50)
if ans_col:
    not_scott_boston = df[df[ans_col] != 'Scott Boston']
    print(f"Found {len(not_scott_boston)} questions NOT answered by Scott Boston")
    if len(not_scott_boston) > 0:
        print(f"Top answerers (excluding Scott Boston):")
        print(not_scott_boston[ans_col].value_counts().head())
else:
    print("No answer name column found") 
  
