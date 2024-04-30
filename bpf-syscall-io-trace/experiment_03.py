#!/usr/bin/env python3

import threading

from experiment_tools import Task, create_file_pwrite
from pathlib import Path


def main():
    file_name = Path('./output_experiment_01.bdata')    
    file_size_bytes = 10_485_760
    chunk_size_bytes = 1_048_576

    if not file_name.exists():
        create_file_pwrite(file_name=file_name, file_size_bytes=file_size_bytes, chunk_size_bytes=chunk_size_bytes)

    t1_offset_range = dict()
    t1_offset_range['start'] = 0 
    t1_offset_range['end'] = (file_size_bytes/2) - 1
    task1 = Task(file_name=file_name, offset_range=t1_offset_range, chunk_size_bytes=chunk_size_bytes, file_size_bytes=file_size_bytes)
    t1 = threading.Thread(target=task1.read, name='t1')

    t2_offset_range = dict()
    t2_offset_range['start'] = file_size_bytes/2
    t2_offset_range['end'] = file_size_bytes
    task2 = Task(file_name=file_name, offset_range=t2_offset_range, chunk_size_bytes=chunk_size_bytes, file_size_bytes=file_size_bytes)
    t2 = threading.Thread(target=task2.read, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
