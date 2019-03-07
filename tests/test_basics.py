from pathlib import Path
import pytest
import subprocess


@pytest.mark.skip(reason="read file")
def read_file(path):
    file  = open(path, 'r')
    content = file.read()
    file.close()
    return content

def test_basic_case1():

    path = "../tests_files/basic/case1/t/1"
    path_compare = "../tests_files/basic/case1/tcompare/1"

    res = subprocess.run("python ../gsed.py lol mdr " + path,
                         shell=True, capture_output=True)

    assert res.returncode == 0

    content = read_file(path)
    content_compare = read_file(path_compare)

    assert content_compare == content
