#!/bin/bash
echo "The challenge is to decrypt a AES-128-CBC encrypted message with key \"YELLOW SUBMARINE\"."
echo "https://cryptopals.com/static/challenge-data/10.txt"
echo "################################################################################################"
./challenge10.py -f 10.txt -k "YELLOW SUBMARINE"
echo "################################################################################################"