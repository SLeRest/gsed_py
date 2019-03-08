from pathlib import Path
import pytest
import subprocess


@pytest.mark.skip(reason="read file")
def read_file(path):
    file  = open(path, 'r')
    content = file.read()
    file.close()
    return content

def test_recursive_case1():
    dir_path = "../tests_files/recursive/case1/t"
    dir_path_compare = "../tests_files/recursive/case1/tcompare"
    paths = [
        dir_path + "/1",
        dir_path + "/d/2",
    ]
    paths_compare = [
        dir_path_compare + "/1",
        dir_path_compare + "/d/2",
    ]

    res = subprocess.run("python ../gsed.py -R lol mdr " + dir_path,
                         shell=True, capture_output=True)

    assert res.returncode == 0

    i = 0
    while i < len(paths):
        content = read_file(paths[i])
        content_compare = read_file(paths_compare[i])
        assert content_compare == content
        i += 1

def test_recursive_case2():
    dir_path = "../tests_files/recursive/case2/t"
    dir_path_compare = "../tests_files/recursive/case2/tcompare"
    paths = [
        dir_path + "/1",
        dir_path + "/d/2",
        dir_path + "/d//dd/3",
    ]
    paths_compare = [
        dir_path_compare + "/1",
        dir_path_compare + "/d/2",
        dir_path_compare + "/d/dd/3",
    ]

    res = subprocess.run("python ../gsed.py -R lol mdr " + dir_path,
                         shell=True, capture_output=True)

    assert res.returncode == 0

    i = 0
    while i < len(paths):
        content = read_file(paths[i])
        content_compare = read_file(paths_compare[i])
        assert content_compare == content
        i += 1
