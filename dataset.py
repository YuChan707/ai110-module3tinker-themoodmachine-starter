"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Lowkey stressed but kinda proud of what I shipped",
    "No cap, this party was the worst 😂",
    "Highkey could do without this 5am meeting",
    "I absolutely love getting stuck in traffic 😒",
    "I’m chill, but also a bit anxious about tomorrow",
    "Went to the gym, felt weak but also strong 💪",
    "Can’t tell if I’m mad or just tired 🥲",
    "This is the best worst date I’ve ever been on 💀",
    "I’m so happy and also sorta sad at the same time",
    "No emoji needed, the vibes are immaculate :)",
    "Ugh, I hate being sick but the cozy blankets are nice :(",
    "Feeling neutral about everything rn",
    "I’m actually crying from laughing too hard 😂",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "mixed",     # "Lowkey stressed but kinda proud of what I shipped"
    "negative",  # "No cap, this party was the worst 😂"
    "negative",  # "Highkey could do without this 5am meeting"
    "negative",  # "I absolutely love getting stuck in traffic 😒"
    "mixed",     # "I’m chill, but also a bit anxious about tomorrow"
    "mixed",     # "Went to the gym, felt weak but also strong 💪"
    "mixed",     # "Can’t tell if I’m mad or just tired 🥲"
    "mixed",     # "This is the best worst date I’ve ever been on 💀"
    "mixed",     # "I’m so happy and also sorta sad at the same time"
    "positive",  # "No emoji needed, the vibes are immaculate :)"
    "mixed",     # "Ugh, I hate being sick but the cozy blankets are nice :("
    "neutral",   # "Feeling neutral about everything rn"
    "positive",  # "I’m actually crying from laughing too hard 😂"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
