from main import finite_automaton_search

with open("input_text.txt", "r", encoding="utf-8") as file:
    haystack = file.read()

phrases = ["ви отримаєте максимум", "та буде найкраще"]

for phrase in phrases:
    matches = finite_automaton_search(haystack, phrase)
    print(f"Фраза: \"{phrase}\" — Кількість входжень: {len(matches)}")
