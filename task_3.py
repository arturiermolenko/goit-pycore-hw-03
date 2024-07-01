import re


def normalize_phone(phone_number: str) -> str:
    """
    Function normalizes phone numbers to a standard format,
    leaving only numbers and the '+' symbol at the beginning
    :param phone_number: unchecked phone number
    :return: phone number in standard format
    """
    phone_number = phone_number.strip()

    if phone_number.startswith("+380"):
        pass
    elif phone_number.startswith("380"):
        phone_number = "+" + phone_number
    elif not phone_number.startswith("+"):
        phone_number = "+38" + phone_number

    pattern = r"[^0-9+]"
    phone_number = re.sub(pattern=pattern, repl="", string=phone_number)
    return phone_number


def normalize_phone_short(phone_number: str) -> str | None:
    pattern = r"[^0-9]"
    phone_number = re.sub(pattern=pattern, repl="", string=phone_number)
    if len(phone_number) < 7:
        return
    return "+380" + phone_number[-7:]


if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Normalized numbers:", sanitized_numbers)
