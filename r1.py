
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines		

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue #跳到下一迴
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值，不是None的話才執行裡面這行
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') # \n為換行符號

def main():
	lines = read_file('input.txt')
	# print(lines)
	lines = convert(lines)
	write_file('output.txt', lines)

main()