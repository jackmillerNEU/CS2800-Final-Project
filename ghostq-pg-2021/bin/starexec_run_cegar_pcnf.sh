#!/bin/bash
# USAGE: ./solver.sh INPUTFILE

infile=$1
python qcir-conv.py $infile --quiet -write-gq | ./ghostq - -s-cnf -q2 -cegar 1 > /dev/null
ex=$?
echo $ex
exit $ex
