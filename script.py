import os
everyok = True
final = input("[-] Please Type The File You Wanna Write Into: ")
if os.path.exists(final) and os.path.isfile(final) and os.access(final, os.R_OK) and os.access(final, os.W_OK):
    pass
else:
    print("[-] Creating File")
    createfile = open(final, 'w')
    createfile.close()
wordlists = input("[-] Please Type All The Wordlists You Wanna Combine (One Space Seperated): ").split(' ')
if len(wordlists) >= 2:
    for s in wordlists:
        try:
            if s == wordlists[wordlists.index(s) - 1]: 
                print(f"[x] {s} This Is A Repeated Wordlist")
                everyok = False
                break
        except:
            if s == wordlists[wordlists.index(s) + 1]:
                print(f"[x] {s} This Is A Repeated Wordlist")
                everyok = False
                break
else:
    everyok = False 
    print("[x] Provide At Least 2 Wordlists")
if everyok:
    for i in wordlists:
        if os.path.exists(i) and os.path.isfile(i) and os.access(i, os.R_OK) and i != final:
            wordlist = open(i, 'r')
            finish = open(final, 'a')
            readfin = open(final, 'r')
            for line in wordlist.read():
                repeated = False
                for s in readfin.read():
                    if s == line:
                        repeated = True
                        break
                if repeated:
                    pass 
                else:
                    finish.write(line)
        else:
            everyok = False
            print(f"[x] {i} Does Not Exists, Is Not A File, Is The Same As Input File, Or You Do not Read/Write Permissions")
            break
if everyok == True:
    print(f"[-] Done Combining {wordlists} into {final}")
