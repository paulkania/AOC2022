import os

with open('6r.txt','r') as file:
    file=file.read()

# file = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' #7
# file = 'bvwbjplbgvbhsrlpgdmjqwftvncz' #5, vwbj
# file = 'nppdvjthqldpwncqszvftbrmjlhg' #6 
# file = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' #10
# file = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' #11

string = file
signal = ''
count = 0
score = 0

while string:
    signal += string[count]
    if len(set(signal)) == len(signal):
        count += 1
    else:
        signal = ''
        string = string[1:]
        count=0
        score+=1
        continue
    if count == 4: # change 4 to 14 to answer part 2
        print(score + 4) # change 4 to 14 to answer part 2
        print(signal)
        break

