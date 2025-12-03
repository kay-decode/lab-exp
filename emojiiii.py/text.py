import random

# List of word and emoji pairs
puzzles = [
    ("pizza", "🍕"),
    ("coffee", "☕"),
    ("cat", "🐱"),
    ("dog", "🐶"),
    ("moon", "🌙"),
    ("sun", "☀️"),
    ("rain", "🌧️"),
    ("cake", "🎂"),
    ("car", "🚗"),
    ("phone", "📱"),
    ("book", "📚"),
    ("heart", "❤️"),
    ("fire", "🔥"),
    ("tree", "🌲"),
    ("flower", "🌸"),
    ("sakshaat", "🐭")
]

# Welcome message
print("\n=== TEXT TO EMOJI GAME ===")
print("Type the emoji for each word!")
print("Example: For 'pizza' type 🍕\n")

# Choose 5 random puzzles
selected = random.sample(puzzles, 5)

score = 0

# Play each round
for i in range(5):
    word, emoji = selected[i]
    
    print(f"Round {i+1}: {word}")
    guess = input("Your emoji: ")
    
    if guess == emoji:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! It was: {emoji}\n")

# Show final score
print(f"=== GAME OVER ===")
print(f"Your score: {score}/5")

if score == 5:
    print("Perfect! 🌟")
elif score >= 3:
    print("Good job! 👍")
else:
    print("Keep trying! 💪")