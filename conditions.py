import pandas as pd
import random

# Your 25 words
words = ['rop', 'poy', 'tib', 'zeg', 'tem', 'wis', 'arf', 'vow', 'ses', 'kal',
         'smeck', 'praith', 'stutch', 'tharge', 'blick', 'plyne', 'kreet', 
         'clet', 'flane', 'wug', 'fusk', 'phrup', 'trebe', 'tarb', 'crolt']

# Create empty list for trials
trials = []
trial_id = 1

for word in words:
    # First trial: with "a" article (correct = object)
    obj_num1 = random.randint(1, 25)
    sub_num1 = random.randint(1, 25)
    
    trials.append({
        'trial_id': trial_id,
        'word': word,
        'article': 'a',
        'correct_type': 'obj',
        'obj_image': f'o{obj_num1}.png',
        'sub_image': f's{sub_num1}.png'
    })
    trial_id += 1
    
    # Second trial: null article (correct = substance)
    # Use DIFFERENT random images!
    obj_num2 = random.randint(1, 25)
    sub_num2 = random.randint(1, 25)
    
    trials.append({
        'trial_id': trial_id,
        'word': word,
        'article': '',
        'correct_type': 'sub',
        'obj_image': f'o{obj_num2}.png',
        'sub_image': f's{sub_num2}.png'
    })
    trial_id += 1

# Randomize trial order
random.shuffle(trials)

# Reset trial_id after shuffle (optional)
for i, trial in enumerate(trials, 1):
    trial['trial_id'] = i

# Create DataFrame and save
df = pd.DataFrame(trials)
df.to_csv('conditions.csv', index=False)

# Print summary
print("conditions.csv generated!")
print(f"Total trials: {len(df)}")
print("\nFirst 5 trials:")
print(df.head())
print("\nExample: Same word appears with different images:")
print(df[df['word'] == 'rop'][['word', 'article', 'obj_image', 'sub_image']])
