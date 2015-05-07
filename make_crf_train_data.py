#!/usr/bin/python
# -*- coding: utf-8 -*-
#make_crf_train_data.py
#得到CRF++要求的格式的训练文件
#用法：命令行--python dataprocess.py input_file output_file


import sys
import codecs

#4 tags for character tagging: B(Begin), E(End), M(Middle), S(Single)
def character_4tagging(input_file, output_file):
	input_data = codecs.open(input_file, 'r', 'utf-8')
	output_data = codecs.open(output_file, 'w', 'utf-8')
	for line in input_data.readlines():
		word_list = line.strip().split()
		for word in word_list:
			if len(word) == 1:
				output_data.write(word + "\tS\n")
			else:
				output_data.write(word[0] + "\tB\n")
				for w in word[1:len(word)-1]:
					output_data.write(w + "\tM\n")
				output_data.write(word[len(word)-1] + "\tE\n")
		output_data.write("\n")
	input_data.close()
	output_data.close()

#6 tags for character tagging: B(Begin), E(End), M(Middle), S(Single), M1, M2
def character_6tagging(input_file, output_file):
	input_data = codecs.open(input_file, 'r', 'utf-8')
	output_data = codecs.open(output_file, 'w', 'utf-8')
	for line in input_data.readlines():
		word_list = line.strip().split()
		for word in word_list:
			if len(word) == 1:
				output_data.write(word + "\tS\n")
			elif len(word) == 2:
				output_data.write(word[0] + "\tB\n")
				output_data.write(word[1] + "\tE\n")
			elif len(word) == 3:
				output_data.write(word[0] + "\tB\n")
				output_data.write(word[1] + "\tM\n")
				output_data.write(word[2] + "\tE\n")
			elif len(word) == 4:
				output_data.write(word[0] + "\tB\n")
				output_data.write(word[1] + "\tM1\n")
				output_data.write(word[2] + "\tM\n")
				output_data.write(word[3] + "\tE\n")
			elif len(word) == 5:
				output_data.write(word[0] + "\tB\n")
				output_data.write(word[1] + "\tM1\n")
				output_data.write(word[2] + "\tM2\n")
				output_data.write(word[3] + "\tM\n")
				output_data.write(word[4] + "\tE\n")
			elif len(word) > 5:
				output_data.write(word[0] + "\tB\n")
				output_data.write(word[1] + "\tM1\n")
				output_data.write(word[2] + "\tM2\n")
				for w in word[3:len(word)-1]:
					output_data.write(w + "\tM\n")
				output_data.write(word[len(word)-1] + "\tE\n")
		output_data.write("\n")
	input_data.close()
	output_data.close()

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Usage: python dataprocess.py inputfile outputfile"
		sys.exit()
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	character_4tagging(input_file, output_file)
