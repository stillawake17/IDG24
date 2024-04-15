# Example questionnaire
questions = {
    "Investment Goals": {
        "Saving for retirement": 1,
        "Buying a property/car in the next 5-10 years": 2,
        "Generating short-term income": 3,
        "Speculative gains": 4,
    },
    "Investment Time": {
        "Less than 1 year": 4,
        "1-3 years": 3,
        "3-5 years": 2,
        "More than 5 years": 1,
    },
    "Risk Tolerance": {
        "Sell all investments to avoid further losses": 1,
        "Sell some investments to minimize losses": 2,
        "Keep all investments and wait for the market to recover": 3,
        "Invest more to lower the average cost": 4,
    },
}

# Function to collect responses and calculate the risk score
def collect_responses_and_calculate_score(questions):
    total_score = 0
    for question, options in questions.items():
        print(f"\n{question}:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        response = int(input("Your choice (number): "))
        chosen_option = list(options.keys())[response-1]
        total_score += options[chosen_option]
    return total_score

# Calculate the risk score
risk_score = collect_responses_and_calculate_score(questions)

# Determine risk level based on the score
if risk_score <= 5:
    risk_level = "Very Risk Averse"
elif risk_score <= 8:
    risk_level = "Risk Averse"
elif risk_score <= 11:
    risk_level = "Moderate Risk"
elif risk_score <= 14:
    risk_level = "Risk Tolerant"
else:
    risk_level = "Very Risk Tolerant"

print(f"\nYour total risk score is: {risk_score}")
print(f"Risk Level: {risk_level}")

