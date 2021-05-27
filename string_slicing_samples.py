#string slice
#Slice[start_at_index:stop_before_index:step_index]
s = "sample slice"

# number before ":" is from index and after ":" is (end index - 1)
# if negatvie sign is used before ":" then counts backwards from end index to till end
# if negative sing is used after ":" then counts from beginning till ( end index - number used)

#when you slice a string specify the index as shown below, end index is not inclusive here
print(s[1:3])
#outputs >>am

#prints from position 2 till end
print(s[2:])

#print from beginning till position 2
print(s[:2])

#print from -2 till end
print(s[-2:])

#print from start till -2
print(s[:-2])

print(s[::-1])
print(s[1::-1])
print(s[1:1:-1])
