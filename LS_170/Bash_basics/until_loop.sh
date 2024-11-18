counter=0
max=20

until [[ $counter -gt $max ]]
do
    echo $counter
    ((counter++))
done