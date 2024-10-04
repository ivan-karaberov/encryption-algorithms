import string
import random

def generate_random_string(str_size: int) -> str:
    return "".join(random.choice(string.ascii_lowercase) for i in range(str_size))