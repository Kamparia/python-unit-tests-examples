# import function
from main import phone_validator

# Test for phone_validator funtion
def test_phone_validator():
    assert phone_validator("080-601-51398") == True
    assert phone_validator("+2348060151398") == False