#!/bin/bash

cd tests/

pytest test_basics.py


cp -r test_files.backup test_files
