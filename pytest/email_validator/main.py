# import libraries
import pytest
import re

def email_validator(email):
    """Function validates given email address.

    email (string) - email address
    """

    # regex for validating an email
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    # validate email
    if(re.search(regex, email)):
        return True
    else:
        return False