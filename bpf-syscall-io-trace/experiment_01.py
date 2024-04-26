#!/usr/bin/env python3

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

def main():
    file_name = Path('./output_experiment_01.bdata')    
    file_size_bytes = 10_485_760
    chunk_size_bytes = 1_024

    create_file_pwrite(file_name=file_name, file_size_bytes=file_size_bytes, chunk_size_bytes=chunk_size_bytes)

if __name__ == '__main__':
    main()
