# import libraries
import pytest
import re

def phone_validator(phone_number):
    """Function checks is given phone number is a valid 10 digit phone number .

    phone_number (string) - phone number (XXX-XXX-XXXXX)
    """

    # regex for validating a phone number
    regex = '\w{3}-\w{3}-\w{5}'

    # validate phone number
    if(re.search(regex, phone_number)):
        return True
    else:
        return False