# import function
from main import email_validator

# Test for email_validator funtion
def test_email_validator():
    assert email_validator("juno@email.com") == True
    assert email_validator("juno@email@.com") == False
