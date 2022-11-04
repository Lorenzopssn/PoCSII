start=open('rosalind_subs.txt').readlines()
string=start[0].replace('\n', '')
substring=start[1].replace('\n', '')
#.find() da -1 se la substringa non viene individuata
my_output=[]
end_point=0
while end_point<len(string):
    end_point=string.find(substring, end_point)
    if end_point != -1:
        my_output.append(end_point+1)
        end_point += 1
    else:
        print(*my_output)
        break

