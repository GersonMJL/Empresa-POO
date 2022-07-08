import re


def validate_phone(phone: str):
    """Validate brazilian phone number.

    Valid phone formats accepted:
     - (XX) XXXX-XXXX
     - (XX) XXXXX-XXXX
     - XX XXXX-XXXX
     - XX XXXXX-XXXX
     - XXXX-XXXX
     - XXXXX-XXXX

    Args:
        phone (str): String with phone number to be validated.

    Raises:
        TypeError: If phone is not a string.
        Exception: If phone is not a valid phone number.

    Returns:
        True: If phone is a valid phone number.
    """
    if type(phone) is not str:
        raise TypeError("Phone must be a string.")
    if not re.match(r"(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})", phone):
        raise Exception("Phone is not valid.")
    return True
