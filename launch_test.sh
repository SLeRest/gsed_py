#!/bin/bash

# make test
cd tests/
pytest test_basics.py

# reset file
cd ..
rm -rf tests_files
cp -r tests_files.backup tests_files
