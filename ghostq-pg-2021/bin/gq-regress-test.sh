if [ `./ghostq $1 -allow-free | ./fmla "-e eq(include(stdin), include($2))" -bdd-simp` = 'true()' ]
then echo "ok"
else echo "fail"
fi
