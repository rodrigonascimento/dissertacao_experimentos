#!/usr/bin/env python3

import os

from experiment_tools import create_file_pwrite
from pathlib import Path

def main():
    file_name = Path('./output_experiment_01.bdata')    
    file_size_bytes = 10_485_760
    chunk_size_bytes = 1_048_576

    if not file_name.exists():
        create_file_pwrite(file_name=file_name, file_size_bytes=file_size_bytes, chunk_size_bytes=chunk_size_bytes)

    fd = os.open(file_name, os.O_RDWR)
    print(f'Reading file..........offset 0')
    os.pread(fd, chunk_size_bytes, 0)
    print(f'Reading file..........offset {int(file_size_bytes/2)}')
    os.pread(fd, chunk_size_bytes, int(file_size_bytes/2))
    print(f'Reading file..........offset {file_size_bytes-chunk_size_bytes}')
    os.pread(fd, chunk_size_bytes, file_size_bytes-chunk_size_bytes)
    print(f'Reading file..........offset {int(file_size_bytes/4)}')
    os.pread(fd, chunk_size_bytes, int(file_size_bytes/4))
    print(f'Reading file..........offset {int(file_size_bytes/2)+chunk_size_bytes}')
    os.pread(fd, chunk_size_bytes, int(file_size_bytes/2)+chunk_size_bytes)
    os.close(fd)

if __name__ == '__main__':
    main()
