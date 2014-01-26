#!/bin/bash

echo "Status: 200 OK"
echo "Content-Type: text/html; charset=UTF-8"
echo 
echo 
echo "<html>"
echo "<head>"
echo "<title>Mostrar IP</title>"
echo "</head>"
echo "<body>"
echo "<h1>Mostrar IP</h1>"
echo "<p>Tu IP es: $REMOTE_ADDR</p>"
echo "</body>"
echo "<html>"
