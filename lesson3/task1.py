'''Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: ' x'

Expected Result: Empty String'''

print('helloworld'[0:2] + 'helloworld'[-2:])  # print('helloworld'[0:3]+'d')
print('my'[0:2] + 'my'[-2:])
print(' x'[:-1])             # print(' x'[:0])