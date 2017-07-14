import whois
import sys

url = sys.argv[1]

url_file = open(url, 'r')
line = url_file.readline()

domain = whois.query(line)

print(domain.__dict__) 


result_file = open('log.txt', 'w')

result_file.write(str(domain.__dict__))


url_file.close()
result_file.close()
