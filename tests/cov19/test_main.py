import pytest
import subprocess

import cov19.main

def capture(command):
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out,err = proc.communicate()
    return out, err, proc.returncode

def test_main(capsys):
    with capsys.disabled():
        command = ['python3', 'src/cov19/main.py', 'processDirectURL', '--url', '"https://www.rts.rs/page/stories/sr/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/story/3134/koronavirus-u-srbiji/4295816/koronavirus-kovid-19-vakcine-srbija-epidemija.html"']
        out, err, exitcode = capture(command)
        assert exitcode == 0
