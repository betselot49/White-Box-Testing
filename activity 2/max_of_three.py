def assess_risk(age, smoker, has_preexisting_condition):
    if age < 18:
        return "Underage - Not applicable"
    
    if smoker and has_preexisting_condition:
        return "High Risk"
    elif smoker or has_preexisting_condition:
        return "Moderate Risk"
    else:
        return "Low Risk"


















