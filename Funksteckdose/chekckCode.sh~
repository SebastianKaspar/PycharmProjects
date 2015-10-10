#!/bin/bash
date
s=0
u=0

for  s in {1..31}
do
     for  u in {1..31}
     do
      sudo pilight-send -p  mumbi -s $s -u $u -f
      sudo pilight-send -p  mumbi -s $s -u $u -t
      echo "s=" $s  "u=" $u
      done
done
