#!/usr/bin/env bash
virtualenv -p /usr/bin/python3.7 menv
source venv/bin/activate
pip install -r requirements.txt
deactivate
