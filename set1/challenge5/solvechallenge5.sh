#!/bin/bash
echo "The challenge is to encrypt a text with a repeating XOR key:"
echo "https://cryptopals.com/static/challenge-data/5.txt"
echo "################################################################################################"
./challenge5.py -f plaintext -k ICE
echo "################################################################################################"