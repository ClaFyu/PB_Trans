import tensorflow as tf
from tensorflow.python.framework import graph_util
import sys


def freeze_graph(input_checkpoint, output_graph, output_node_names):
    saver = tf.train.import_meta_graph(input_checkpoint + '.meta', clear_devices=True)
    graph = tf.get_default_graph()  # 获得默认的图
    input_graph_def = graph.as_graph_def()  # 返回一个序列化的图代表当前的图

    with tf.Session() as sess:
        saver.restore(sess, input_checkpoint)  # 恢复图并得到数据
        output_graph_def = graph_util.convert_variables_to_constants(  # 模型持久化，将变量值固定
            sess=sess,
            input_graph_def=input_graph_def,  # 等于:sess.graph_def
            output_node_names=output_node_names.split(","))  # 如果有多个输出节点，以逗号隔开

        with tf.gfile.GFile(output_graph, "wb") as f:  # 保存模型
            f.write(output_graph_def.SerializeToString())  # 序列化输出
        print("%d ops in the final graph." % len(output_graph_def.node))  # 得到当前图有几个操作节点


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("需要输入三个参数：checkpoint路径（data、index和meta前面的部分）、pb模型输出路径（不同于h5转换，需要完整路径）和输出的节点名称（通过ckpt_node_names.py获取）")
        exit()

    checkpoint_path = sys.argv[1]
    out_graph = sys.argv[2]
    freeze_graph(checkpoint_path, out_graph, sys.argv[3])
