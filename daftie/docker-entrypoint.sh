#!/bin/bash

set -xe

scrapy crawl rent -O "/data/daftie-$(date +%F-%H-%M).csv" -t csv
