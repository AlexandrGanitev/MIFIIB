my_file = open('file_to_write_to.txt', 'w')
my_file.write('tttt')
print('zzzz', file=my_file)
my_file.close()
