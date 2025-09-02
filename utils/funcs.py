import re

words = ["test", "spam", "reklama"]


def contains_words(text: str, words: list[str] = words) -> bool:
    """
    Проверяет, содержит ли текст хоть одно слово из списка.
    """
    text_lower = text.lower()
    return any(word.lower() in text_lower for word in words)
