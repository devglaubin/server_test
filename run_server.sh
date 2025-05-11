#!/bin/bash

cd $(pwd)

source .venv/bin/activate
python3 src/server/main.py

deactivate
