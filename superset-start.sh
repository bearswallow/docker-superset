#!/bin/bash

# wait to superset-init complete.
python3 /superset/check_init.py

# run superset service
superset runserver