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

def test_basic_case2():

    dir_path = "../tests_files/basic/case2/t/"
    path =         [
        "../tests_files/basic/case2/t/1",
        "../tests_files/basic/case2/t/2"
    ]
    path_compare = [
        "../tests_files/basic/case2/tcompare/1",
        "../tests_files/basic/case2/tcompare/2"
    ]
    res = subprocess.run("python ../gsed.py lol mdr " + dir_path,
                         shell=True, capture_output=True)
    assert res.returncode == 0

    i = 0
    while i < len(path):
        content = read_file(path[i])
        content_compare = read_file(path_compare[i])
        assert content_compare == content
        i += 1

