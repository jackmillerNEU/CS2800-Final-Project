for x in  load_56.xml_UNSAT_5_1  load_21.xml_UNSAT_1_1  load_57.xml_SAT_2_2
do
    echo -n "Testing $x... "
    ./gq-regress-test.sh $x.cqbf $x.ans
done
