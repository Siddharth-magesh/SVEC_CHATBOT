'''from random import randint

# Assuming matrix_prices is already defined
matrix_prices = [[randint(1, 100) for _ in range(30)] for _ in range(5)]

for i in matrix_prices:
    print((i))'''
    
def parse_budget_input(user_input):
    # Define the keywords and their corresponding quantities
    keywords = ["seeds", "farming", "equipment", "fertilizers", "labours", "trackors"]
    quantities = [0] * len(keywords)
    total_budget = 0
    
    # Split the input string into words
    words = user_input.split()
    
    # Iterate over the words to find the quantities
    for i, word in enumerate(words):
        # Check if the word is a number
        if word.isdigit():
            # Check if the next word is one of the keywords
            if i < len(words) - 1 and words[i + 1] in keywords:
                # Get the index of the keyword
                keyword_index = keywords.index(words[i + 1])
                # Set the quantity at the corresponding index
                quantities[keyword_index] = int(word)
                # Increment the total budget
                total_budget += int(word)
    
    return total_budget, quantities

# Test the function with the given input string
user_input = "I have a budget of 5000 ruppess and I want 2 sack of seeds, 3 farming equipment, 5 bags of fertilizers, 15 labours, and 2 trackors"
total_budget, quantities = parse_budget_input(user_input)
print("Total Budget:", total_budget)
print("Quantities:", quantities)


