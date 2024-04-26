import random
import string

from io import BytesIO

def generate_random_bdata(chunk_size_bytes: int) -> BytesIO:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=chunk_size_bytes))
        bdata = BytesIO(random_string.encode('utf-8'))
        return bdata
