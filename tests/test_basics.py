from pathlib import Path
import pytest
import subprocess


@pytest.mark.skip(reason="read file")
def read_file(path):
    file  = open(path, 'r')
    content = file.read()
    file.close()
    return content

# simple file in arg no opt
def test_basic_case1():
    path = "../tests_files/basic/case1/t/1"
    path_compare = "../tests_files/basic/case1/tcompare/1"
    res = subprocess.run("python ../gsed.py lol mdr " + path,
                         shell=True, capture_output=True)
    assert res.returncode == 0
    content = read_file(path)
    content_compare = read_file(path_compare)
    assert content_compare == content

# simple path in arg no opt
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
    print(res)
    assert res.returncode == 0
    i = 0
    while i < len(paths):
        content = read_file(paths[i])
        content_compare = read_file(paths_compare[i])
        assert content_compare == content
        i += 1

# hidded file in arg opt all
def test_basic_case3():
    dir_path = "../tests_files/basic/case3/t"
    dir_path_compare = "../tests_files/basic/case3/tcompare"
    path = dir_path + "/.1"
    path_compare = dir_path_compare + "/.1"
    res = subprocess.run("python ../gsed.py -a lol mdr " + dir_path,
                         shell=True, capture_output=True)
    assert res.returncode == 0
    content = read_file(path)
    content_compare = read_file(path_compare)
    assert content_compare == content

# hidded file in arg no opt
def test_basic_case4():
    dir_path = "../tests_files/basic/case4/t"
    dir_path_compare = "../tests_files/basic/case4/tcompare"
    path = dir_path + "/.1"
    path_compare = dir_path_compare + "/.1"
    res = subprocess.run("python ../gsed.py lol mdr " + dir_path,
                         shell=True, capture_output=True)
    assert res.returncode == 0
    content = read_file(path)
    content_compare = read_file(path_compare)
    assert content_compare == content

