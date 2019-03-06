from keras.models import load_model
import tensorflow as tf
import sys
from keras import backend as K
from tensorflow.python.framework import graph_util, graph_io


def h5_to_pb(model, model_name, out_prefix="output_"):

	out_nodes = []
	for i in range(len(model.outputs)):
		out_nodes.append(out_prefix + str(i + 1))
		tf.identity(model.output[i], out_prefix + str(i + 1))

	sess = K.get_session()

	init_graph = sess.graph.as_graph_def()
	main_graph = graph_util.convert_variables_to_constants(sess, init_graph, out_nodes)
	graph_io.write_graph(main_graph, logdir='result', name=model_name, as_text=False)


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("需要输入两个参数：h5模型输入路径、pb模型输出路径（存储在result文件夹下）")
		exit()

	weight_file_path = sys.argv[1]
	output_graph_name = sys.argv[2]

	h5_model = load_model(weight_file_path)
	h5_to_pb(h5_model, model_name=output_graph_name)
	print('model saved')
