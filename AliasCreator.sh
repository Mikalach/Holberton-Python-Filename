#!/bin/bash
echo "template(){" >> ~/.bashrc
echo "    vi $PWD/SourceCod ; python3 $PWD/main.py \$PWD $PWD ; chmod u+x *" >> ~/.bashrc
echo "}" >> ~/.bashrc
echo "Alias Made: use \"template\" in new Holberton folder"
exec bash
