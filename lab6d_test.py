#!/usr/bin/env python3

import subprocess

def test_lab6d():
    
    # Run the script and capture the output
    p = subprocess.Popen(['python3', 'lab6d.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Provide the input
    p.stdin.write('1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'.encode())
    p.stdin.flush()

    # Write a unit test to check the output of lab6d.py
    output = p.stdout.read().decode()

    # Assert the output begins with Guess a number between 1 and 10: or contains "You guessed the correct number!"
    assert output.startswith('Please guess a number between 1 and 10:') or "You guessed the correct number!" in output

test_lab6d()