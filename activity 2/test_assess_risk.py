def assess_risk(age, smoker, has_preexisting_condition):
    if age < 18:
        return "Underage - Not applicable"
    
    if smoker and has_preexisting_condition:
        return "High Risk"
    elif smoker or has_preexisting_condition:
        return "Moderate Risk"
    else:
        return "Low Risk"


def test_underage():
    assert assess_risk(16, True, True) == "Underage - Not applicable"

def test_high_risk():
    assert assess_risk(30, True, True) == "High Risk"

def test_moderate_risk_smoker():
    assert assess_risk(40, True, False) == "Moderate Risk"

def test_moderate_risk_condition():
    assert assess_risk(45, False, True) == "Moderate Risk"

def test_low_risk():
    assert assess_risk(50, False, False) == "Low Risk"





