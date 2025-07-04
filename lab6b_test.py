#!/usr/bin/env python3

def test_lab6b():
    
    import subprocess
    p = subprocess.Popen(['python3', 'lab6b.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Provide the input
    p.stdin.write(b'5\n')
    p.stdin.flush()

    output = p.stdout.read().decode()
    assert "Please enter a number: " in output
    assert "1" in output
    assert "3" in output

test_lab6b()