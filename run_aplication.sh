#!/bin/bash

cd $(pwd)

source .venv/bin/activate
python3 src/api/main.py

deactivate
