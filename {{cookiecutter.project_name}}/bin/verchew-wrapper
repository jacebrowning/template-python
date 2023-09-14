#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# See `verchew` for licensing and documentation links.

set -e
set -o pipefail

BIN=$(dirname $(realpath $0))

if [ -e "${BIN}/verchew" ]; then
    python3 "${BIN}/verchew" "$@"
elif  [ -e "${BIN}/script.py" ]; then
    python3 "${BIN}/script.py" "$@"
else
    echo "ERROR: 'verchew' script is missing, run 'verchew --vendor' again"
    exit 1
fi
