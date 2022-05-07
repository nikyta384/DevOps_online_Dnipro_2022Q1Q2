# Task 6

**A-script**

#!/bin/bash

trgt=$2

function all(){

nmap -sn $trgt | grep -E -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'

}

function target(){

nmap $trgt | grep 'open'

}

function nothing(){

echo "Please select parametrs --all or --target"

}

if [ $1 == "--all" ]

then

all

elif [ $1 == "--target" ]

then

  target

else

  nothing

fi

----------------------------------------------------------------------------------------------------------------------------------

**B-script**

#1 How many requests were there from each ip?

cat apache_logs.txt | grep -E -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort | uniq -c | sort -n

#2 What is the most requested page?

cat apache_logs.txt | grep -E -o 'GET.*HTTP' | awk '{ $1=""; print $0 }' |  awk '{ $2=""; print $0 }' | sort | uniq -c | sort -n

#3 How many requests were there from each ip?

cat apache_logs.txt | grep -E -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort | uniq -c | sort -n

#4 What non-existent pages were clients referred to?

cat apache_logs.txt | grep 404

#5 What time did site get the most requests?

cat apache_logs.txt | cut -d[ -f2 | cut -d] -f1 | awk -F: '{print $2":00"}' | sort -n | uniq -c

#5 What search bots have accessed the site? (UA + IP)

cat apache_logs.txt | grep bot | grep -E -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'\|'\"\s\"(.*)\s'

-----------------------------------------------------------------------------------------------------------------------

**C-script**

#!/bin/bash 

backup_files=$1

dest="$2"

day=$(date +%A:%H:%M)

hostname=$(hostname)

archive_file="$hostname-$day.tgz"

echo "Backing up $backup_files to $dest/$archive_file"

date

echo

tar -cvzf $dest/$archive_file $backup_files

echo

echo "Backup finished"

date

ls -lh $dest

tee "$day.log"


crontab

* * * * * /home/pavlovskyi/bash_scripts/c-script.sh ~/bash_scripts/bc ~/bash_scripts | tee ~/bash_scripts/backuplog.txt
