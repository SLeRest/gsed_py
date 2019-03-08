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
    dir_path = "../tests_files/basic/case2/t"
    dir_path_compare = "../tests_files/basic/case2/tcompare"
    paths =         [
        dir_path + "/1",
        dir_path + "/2"
    ]
    paths_compare = [
        dir_path_compare + "/1",
        dir_path_compare + "/2"
    ]
    res = subprocess.run("python ../gsed.py lol mdr " + dir_path,
                         shell=True, capture_output=True)
    assert res.returncode == 0
    i = 0
    while i < len(paths):
        content = read_file(paths[i])
        content_compare = read_file(paths_compare[i])
        assert content_compare == content
        i += 1
