#!/bin/bash
# USAGE: ./solver.sh INPUTFILE

infile=$1
bash ./qcir-to-gq.sh $infile | ./ghostq - -s-cnf -q2 -cegar 0 > /dev/null
ex=$?
echo $ex
exit $ex
