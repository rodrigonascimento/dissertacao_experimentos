import os
import random
import string

from io import BytesIO
from pathlib import Path

def generate_random_bdata(chunk_size_bytes: int) -> BytesIO:
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=chunk_size_bytes))
    bdata = BytesIO(random_string.encode('utf-8'))
    return bdata

def create_file_pwrite(file_name: Path, file_size_bytes: int, chunk_size_bytes: int):
    num_chunks = int(file_size_bytes / chunk_size_bytes)

    if not file_name.exists():
        file_name.touch()
    else:
        os.remove(path=file_name)
        file_name.touch()

    offset = 0
    fd = os.open(file_name, os.O_RDWR)
    for i in range(num_chunks):
        bytes_written = os.pwrite(fd, generate_random_bdata(chunk_size_bytes=chunk_size_bytes).read(), offset)
        offset += chunk_size_bytes
    os.close(fd)


class Task:
    def __init__(self, file_name: Path, offset_range: dict, file_size_bytes: int, chunk_size_bytes: int) -> None:
        self.file_name = file_name
        self.offset_range = offset_range
        self.chunk_size_bytes = chunk_size_bytes
        self.file_size_bytes = file_size_bytes

    def read(self):
        num_chunks = int(self.offset_range['end'] / self.chunk_size_bytes)
        offset = int(self.offset_range['start'])
        
        fd = os.open(self.file_name, os.O_RDONLY)
        for i in range(num_chunks):
            if offset > self.file_size_bytes:
                os.close(fd)
                return
            os.pread(fd, self.chunk_size_bytes, offset)
            offset += self.chunk_size_bytes
        os.close(fd)
