#!/usr/bin/env bash
set -e;

./scripts/install_python.sh
./scripts/install_gphoto2.sh
./scripts/install_ykush.sh

apt-get update && apt-get install -y virtualenv python3.7-dev

virtualenv .venv -p python3.7 \
&&  source .venv/bin/activate \
&&  pip install -r requirements.txt \
&&  pip install -e ./src/