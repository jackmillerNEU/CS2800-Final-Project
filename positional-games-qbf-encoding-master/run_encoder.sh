output_folder=${2:-qbf}
enc=5 

rm -fr $output_folder
mkdir $output_folder

go build encode.go
go build ground.go

for x in {maps,hex-hein}
do 
        mkdir $output_folder/$x 
        for instance in $x/*.pg;
        do
         	a=$(mktemp)
        	./encode $instance --enc=$enc > $a
        	./ground $a -dimacs | grep -v '^c ' > $output_folder/$x/$(basename $instance .pg).qdimacs
        done 
done

for instance in $output_folder/maps/*.qdimacs;
do
    cp $instance /mnt/c/Users/mille/OneDrive/Desktop/depqbf
done 