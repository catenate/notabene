p=$1
pat=$2
p=$(echo $p | tr : ' ' | fmt -w 1 | grep -v $pat)
echo $(echo $p | tr ' ' :)
