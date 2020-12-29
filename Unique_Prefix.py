n = 3
# word = ['pretend','present','previous','prefix']
# word = ['find', 'the', 'shortest', 'unique', 'prefix']
word = ['A', 'AA', 'AAA']

for i in range(n):
    # count = 0
    for j in range(1, len(word[i]) + 1):
        count = 0
        for grp in word:
            if word[i] == grp:
                continue
            elif len(word[i]) == len(word[i][:j]):
                break
            elif word[i][:j] == grp[:j]:
                count += 1
                # break
        if count == 0:
            print(word[i][:j])    
            break