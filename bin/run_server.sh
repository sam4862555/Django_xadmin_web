#!/bin/bash

BASE_DIR=$(dirname $(readlink -f $0))/../
DATE=$(date +'%Y%m%d')

source /etc/profile
# 进入python virtualenv 环境
source ${BASE_DIR}/venv/bin/activate

nohup ${BASE_DIR}/manage.py runserver 0.0.0.0:8001 >> ${BASE_DIR}/logs/${DATE}_run.log 2>&1 &



