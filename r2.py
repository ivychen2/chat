
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines		


def convert(lines):
	person = None
	ivy_word_count = 0
	iris_word_count = 0
	ivy_sticker_count = 0
	iris_sticker_count = 0
	ivy_image_count = 0
	iris_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'ivy':
			if s[2] == '貼圖':
				ivy_sticker_count += 1
			elif s[2] == '圖片':
				ivy_image_count += 1
			else: #不是貼圖
				for msg in s[2:]:
					ivy_word_count += len(msg)
		elif name == 'Iris':
			if s[2] == '貼圖':
				iris_sticker_count += 1
			elif s[2] == '圖片':
				iris_image_count += 1
			else:
				for msg in s[2:]:
					iris_word_count += len(msg)			

	print('ivy說了', ivy_word_count, '個字')
	print('ivy傳了', ivy_sticker_count, '個貼圖')
	print('ivy傳了', ivy_image_count, '張圖片')
	print('iris說了', iris_word_count, '個字')
	print('iris傳了', iris_sticker_count, '個貼圖')
	print('iris傳了', iris_image_count, '張圖片')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') # \n為換行符號


def main():
	lines = read_file('[LINE]Iris.txt')
	lines = convert(lines)


main()