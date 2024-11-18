counter=0
max=20

while [[ $counter -le $max ]]
do
    echo $counter
    ((counter++))
done 