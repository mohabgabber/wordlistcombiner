#!/usr/bin/env bash
echo "Welcome, This Project Is Meant To Combine Multiple Wordlists Together, With Checks To Delete Duplicates"
read -p "please type the name of the file you wanna write to: " wordlist
if [[ -e $wordlist && -s $wordlist && -w $wordlist && -f $wordlist && -r $wordlist ]]; then
    mv "$wordlist" "$wordlist".backup
    touch $wordlist
fi

read -p "Please Define All The Wordlists You Wanna Combine (Comma Seperated): " files 

readarray -d , -t Wordlists <<< $files

for i in "${Wordlists[@]}"; 
do

    if [[ -e "$i" ]]; then
        echo "$i Is Added To Targeted Wordlists"
    else
        echo "$i Doesn Not Exist, Is Not A File, Or Is Not A Writeable/Readable File"
        exit 0
    fi

done