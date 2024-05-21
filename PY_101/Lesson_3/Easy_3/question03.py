# What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# this will print 'hello there' because string are an immutable data type.
# the only way to change str1 is to reassigned it to a new value.
# in Line 4, although str2 initally point to str1 in memory, when we reassign str2 in line 5
# str2 now point to a new address which has a value of 'goodbye'
