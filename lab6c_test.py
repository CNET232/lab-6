#!/usr/bin/env python3
import subprocess

def test_lab6c():
    
    p = subprocess.Popen(['python3', 'lab6c.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Provide the input
    p.stdin.write(b'5\n')
    p.stdin.flush()
    
    output = p.stdout.read().decode()
    assert "Please enter a number: " in output
    assert "0" in output
    assert "2" in output
    assert "4" in output

test_lab6c()