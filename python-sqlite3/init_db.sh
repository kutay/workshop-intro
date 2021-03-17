#!/bin/bash

sqlite3 sqlite.db '.read create.sql'

sqlite3 sqlite.db '.databases'

sqlite3 sqlite.db '.tables'
