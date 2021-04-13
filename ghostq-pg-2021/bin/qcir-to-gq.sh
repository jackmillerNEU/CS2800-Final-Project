ulimit -S -s 250000
./fmla $1 -read-qcir -write-gq | python ./qcir-conv.py - -write-gq -quiet -reclim 25000
