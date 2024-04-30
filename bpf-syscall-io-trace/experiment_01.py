#!/usr/bin/env python3

import os

from pathlib import Path
from experiment_tools import generate_random_bdata, create_file_pwrite

def main():
    file_name = Path('./output_experiment_01.bdata')    
    file_size_bytes = 10_485_760
    chunk_size_bytes = 1_048_576

    print(f'Creating file..........: {file_name.name}')
    create_file_pwrite(file_name=file_name, file_size_bytes=file_size_bytes, chunk_size_bytes=chunk_size_bytes)

if __name__ == '__main__':
    main()
