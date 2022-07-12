def contamination(text: str, char: str) -> str:
    """
    An AI has infected a text with a character!!

    This text is now fully mutated to this character.

    If the text or the character are empty, return an empty string.
    There will never be a case when both are empty as nothing is going on!!

    Note: The character is a string of length 1 or an empty string.
    :param text: original text
    :param char: the mutated character
    :return:
    """
    result = char * len(text)
    return result
