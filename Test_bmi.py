import Lab2.bmi as bmi
print("Test.bmi.py")
def test_bmi_normal_weight():

    result = bmi.calculate_bmi(1.78,78)
    assert (result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.78,78)
    assert (result == 1)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.78,78)
    assert (result == -1)