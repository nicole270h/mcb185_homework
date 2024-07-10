#this took me freaking forever
cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep -E "^[zoncair]*r[zoncair]*$" | grep -E ".{4,}"
gunzip -c dictionary.gz | grep -E "^[zoncair]*r[zoncair]*$" | grep -Ec ".{4,}"