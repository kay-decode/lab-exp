import random

# List of emoji puzzles
puzzles = [
    ("🍕", "pizza"),
    ("☕", "coffee"),
    ("🐱", "cat"),
    ("🐶", "dog"),
    ("🌙", "moon"),
    ("☀️", "sun"),
    ("🌧️", "rain"),
    ("🎂", "cake"),
    ("🚗", "car"),
    ("📱", "phone"),
    ("💕", "sweet heart"),
    ("🐭", "sakshaat")
]

# Welcome message
print("\n=== EMOJI GAME ===")
print("Guess the word from the emoji!\n")

# Choose 5 random puzzles
selected = random.sample(puzzles, 5)

score = 0

# Play each round
for i in range(5):
    emoji, answer = selected[i]
    
    print(f"Round {i+1}: {emoji}")
    guess = input("Your guess: ").lower()
    
    if guess == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! It was: {answer}\n")

# Show final score
print(f"=== GAME OVER ===")
print(f"Your score: {score}/5")

if score == 5:
    print("Perfect! 🌟")
elif score >= 3:
    print("Good job! 👍")
else:
    print("Keep trying! 💪")