#!/bin/sh

javac Main.java
java -classpath "sqlite-jdbc-3.34.0.jar:." Main
