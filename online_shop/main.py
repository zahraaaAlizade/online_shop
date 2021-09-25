def validate_phone(phone_number):
    if len(phone_number)==10:
        return phone_number
    else:
        raise Exception("Error! Invalid National number ")