#!/bin/bash

python3 /app/app.py > /python_app_logs.txt &

varnishncsa -F '%{Varnish:handling}x %U%q %{Varnish:hitmiss}x' > /logs.txt &
