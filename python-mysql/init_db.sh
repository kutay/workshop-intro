#!/bin/bash

docker run --name mysql-server -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=employees -d mysql
