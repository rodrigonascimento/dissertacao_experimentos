#!/usr/bin/env python3

import os

from pathlib import Path
from experiment_tools import generate_random_bdata

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
    chunk_size_bytes = 1_048_576

    print(f'Creating file..........: {file_name.name}')
    create_file_pwrite(file_name=file_name, file_size_bytes=file_size_bytes, chunk_size_bytes=chunk_size_bytes)

if __name__ == '__main__':
    main()
