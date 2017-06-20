#!/bin/bash
echo "The challenge is to decrypt an encrypted file with AES-128-ECB using key \"YELLOW SUBMARINE\""
echo "https://cryptopals.com/static/challenge-data/6.txt"
echo "################################################################################################"
./challenge7.py -f 7.txt -k "YELLOW SUBMARINE"
echo "################################################################################################"