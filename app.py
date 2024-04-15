import json
from flask import Flask, request, render_template
from google.cloud import logging, storage

# Initialize Google Cloud Logging
logging_client = logging.Client()
logger = logging_client.logger("my-custom-log")

def load_scores():
    """Load scores from a cloud storage bucket."""
    bucket_name = 'staging.userrisk-123.appspot.com'  # Replace with your actual bucket name
    file_name = 'scores.json'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    if blob.exists():
        return json.loads(blob.download_as_string(client=None))
    else:
        return []

def save_scores(data):
    """Save scores to a cloud storage bucket."""
    bucket_name = 'staging.userrisk-123.appspot.com'  
    file_name = 'scores.json'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_string(json.dumps(data, indent=4), content_type='application/json')

app = Flask(__name__)

questions = {
    "InvestmentGoals": "What is the primary/main purpose of your investment?",
    "InvestmentTime": "When do you plan on using the funds you have invested?",
    "RiskTolerance": "How would you react to a significant drop in the value of your investment portfolio over a short period?",
    "InvestmentExperience": "How would you describe your experience with investing?",
    "AssetAllocation": "Which portfolio allocation would you be most comfortable with?",
    "LiquidityPreference": "How important is it for you to have immediate access to your investments without facing significant penalties or losses?",
    "IncomeStability": "How stable is your current source of income?",
    "FinancialSafetyNet": "Do you have an emergency fund or savings set aside outside of your investments?",
    "InvestmentPurpose": "Besides the primary goal, are there other purposes for your investment?",
    "MarketVolatilityReaction": "In times of market volatility, how likely are you to make significant changes to your investment portfolio?",
    "FinancialGoals": "Which of the following financial goals is most important to you right now?",
    "LearningandGuidance": "How much do you value educational resources and guidance in making investment decisions?",
}

def determine_risk_level(score):
    if score <= 12:
        return "Very Risk Averse"
    elif score <= 24:
        return "Risk Averse"
    elif score <= 36:
        return "Moderate Risk"
    elif score <= 40:
        return "Risk Tolerant"
    else:
        return "Very Risk Tolerant"

@app.route('/')
def questionnaire():
    return render_template('questionnaire.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    total_score = 0
    for question in questions.keys():
        answer_value = request.form.get(question)
        if answer_value:
            total_score += int(answer_value)
    risk_level = determine_risk_level(total_score)
    
    # Get username from the form
    username = request.form.get('username')
    
    # Load existing scores from cloud storage
    scores_data = load_scores()
    
    # Append new score
    scores_data.append({
        'username': username,
        'score': total_score,
        'risk_level': risk_level
    })
    
    # Save updated scores back to cloud storage
    save_scores(scores_data)
    
    return render_template('result.html', score=total_score, risk_level=risk_level)

if __name__ == '__main__':
    app.run(debug=True)
