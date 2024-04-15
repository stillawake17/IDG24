function calculateRisk() {
    const investmentGoals = parseInt(document.getElementById('investmentGoals').value);
    const investmentTime = parseInt(document.getElementById('investmentTime').value);
    const riskTolerance = parseInt(document.getElementById('riskTolerance').value);
    
    // Calculate total score
    const totalScore = investmentGoals + investmentTime + riskTolerance;
    
    // Determine risk level
    let riskLevel;
    if (totalScore <= 5) {
        riskLevel = "Very Risk Averse";
    } else if (totalScore <= 8) {
        riskLevel = "Risk Averse";
    } else if (totalScore <= 11) {
        riskLevel = "Moderate Risk";
    } else if (totalScore <= 14) {
        riskLevel = "Risk Tolerant";
    } else {
        riskLevel = "Very Risk Tolerant";
    }

    // Display result
    document.getElementById('result').innerHTML = `Your total risk score is: ${totalScore}<br>Risk Level: ${riskLevel}`;
}
