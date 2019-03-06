from tensorflow.python import pywrap_tensorflow
import os
import sys


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("需要输入一个参数：checkpoint路径（data、index和meta前面的部分）")
		exit()

	checkpoint_path = os.path.join(sys.argv[1])
	reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
	var_to_shape_map = reader.get_variable_to_shape_map()
	for key in var_to_shape_map:
		print('tensor_name: ', key)
