#!/bin/sh

sleep 10

celery -A lfg_project worker -l info