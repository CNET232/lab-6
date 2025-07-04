#!/usr/bin/env python3

import subprocess

def test_lab6a():
    # Run the script and capture the output   
    p = subprocess.Popen(['python3', 'lab6a.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    output = p.stdout.read().decode()

    # Check if the output is correct
    assert output == "Toyota\nHonda\nFord\nChevrolet\nNissan\n"

test_lab6a()