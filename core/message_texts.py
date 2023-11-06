HELLO_TEXT = (
    "Hello, {user_name}!\n\nI am your Telegram bot. To check a request, send me a UUID "
    "(Universally Unique Identifier), and I will verify it for you. Make sure the UUID "
    "is correctly formatted."
)

HELP_TEXT = (
    "UUID (Universally Unique Identifier) is a 128-bit identifier that is globally "
    "unique and standardized, commonly used in computer systems to uniquely identify "
    "resources without a centralized authority. UUIDs are typically represented as a "
    "sequence of 32 hexadecimal digits separated by hyphens, resulting in a format like"
    ' "8-4-4-12." They are designed to be unique across time and space, making them '
    "suitable for various purposes, including database record keys, distributed "
    "systems, and more.\n\nExample of a UUID:\n"
    "<i><b>550e8400-e29b-41d4-a716-446655440000</b></i>"
)

WRONG_USER_TEXT = (
    "Access to the Telegram bot is currently unavailable. Please request access."
)

WRONG_FORMAT_TEXT = (
    "The text that was sent is not UUID format.\n\nExample of a UUID:\n"
    "<i><b>550e8400-e29b-41d4-a716-446655440000</b></i>"
)
