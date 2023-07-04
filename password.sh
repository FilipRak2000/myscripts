#!/bin/bash

echo "Podaj dlugosc hasla"
read LENGTH

password=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c "$LENGTH")

echo "Wygenerowane hasło: $password"
