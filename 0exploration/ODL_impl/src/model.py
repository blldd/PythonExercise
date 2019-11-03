# from __future__ import absolute_import
# from __future__ import absolute_divide
# from __future__ import print_function

import tensorflow as tf
import numpy as np
import pandas as pd
import six

NUM_LAYERS = 19
OUTPUT_CLASS = 2
batch_size = 1
train_step = 1000000
num_feature = 28
layer_dimension = [28, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
beta = 0.99
smoothing = 0.3

HIGGS_DIR = '../data/HIGGS.csv'

def get_data(path):
	x = pd.read_csv(path, header=None)
	x = x[:1000000]
	global dataset_size
	dataset_size = x.shape[0]
	y = x[0].astype('int')
	x = x.astype('float')
	x.drop([0], axis=1, inplace=True)
	return x,y

def build_graph2():
	in_size = layer_dimension[0]
	thetaloss = list()
	alpha = tf.get_variable("alpha",[1,NUM_LAYERS],initializer = tf.constant_initializer(0.05))
	x = tf.placeholder(tf.float32,[batch_size, layer_dimension[0]], name = "x-input")
	y_t = tf.placeholder(tf.int32,[batch_size,], name = "y-input")

	inputs = x
	with tf.variable_scope("layer0"):
		theta = tf.get_variable("theta",[in_size,OUTPUT_CLASS],initializer = tf.truncated_normal_initializer(stddev=0.1))
		tf.add_to_collection('theta',theta)
		logits = tf.matmul(inputs,theta)
		thetaloss.append(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y_t))

	for i in range (1, NUM_LAYERS):
		out_size = layer_dimension[i]
		with tf.variable_scope("layer"+str(i)):
			w = tf.get_variable("weight",[in_size,out_size], initializer= tf.truncated_normal_initializer(stddev=0.1))
			tf.add_to_collection("w",w)
			b = tf.get_variable("biases",[out_size], initializer= tf.constant_initializer(0.0))
			tf.add_to_collection('b', b)
			theta = tf.get_variable("theta",[out_size,OUTPUT_CLASS],initializer= tf.truncated_normal_initializer(stddev=0.1))
			tf.add_to_collection('theta',theta)

			inputs = tf.nn.relu(tf.matmul(inputs,w)+b )
			logits = tf.matmul(inputs,theta)
			thetaloss.append(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y_t))
			in_size = layer_dimension[i]

	total_loss = tf.reduce_sum(tf.multiply(tf.transpose(thetaloss),alpha))
	tf.summary.scalar('total_loss',total_loss)

	train_op = tf.train.GradientDescentOptimizer(0.01).minimize(total_loss, var_list=[tf.get_collection('w'), tf.get_collection('b'), tf.get_collection('theta')])

	smooth = tf.get_variable('smooth',[1],initializer = tf.constant_initializer(0.01))

	min_loss = tf.reduce_min(thetaloss)
	max_loss = tf.reduce_max(thetaloss)
	range_loss = max_loss - min_loss
	losses = (thetaloss - min_loss)/range_loss

	gg = tf.math.maximum(tf.multiply(alpha ,tf.transpose(tf.pow(beta, losses))), smooth)
	sumgg = tf.reduce_sum(gg)
	update = tf.assign(alpha, gg/sumgg)

	merged = tf.summary.merge_all()


	X, Y = get_data(HIGGS_DIR)
	init = tf.global_variables_initializer()
	with tf.Session() as sess:
		sess.run(init)
		writer=tf.summary.FileWriter('./logs2',tf.get_default_graph())  
		show_loss = [0.0] * 500
		show_loss = np.array(show_loss)
		shadow_loss = 0
		for i in range(train_step):
			start = (i * batch_size) % dataset_size
			end = min(start+batch_size,dataset_size)
			show_loss[i % 500] = sess.run(total_loss, feed_dict={x:X[start:end], y_t:Y[start:end]})
			if i == 500:
				print i
				shadow_loss = np.average(show_loss)
				print shadow_loss
			elif i % 500 == 0:
				print i
				shadow_loss = shadow_loss*0.99 + np.average(show_loss)*0.01
				print shadow_loss
			summary, _, _ = sess.run([merged, update, train_op],feed_dict={x:X[start:end], y_t:Y[start:end]})
			writer.add_summary(summary, i)

	writer.close()

def build_graph():
	in_size = layer_dimension[0]
	x = tf.placeholder(tf.float32,[batch_size, layer_dimension[0]], name = "x-input")
	y_t = tf.placeholder(tf.int32,[batch_size,], name = "y-input")

	inputs = x

	for i in range (1, NUM_LAYERS):
		out_size = layer_dimension[i]
		with tf.variable_scope("layer"+str(i)):
			w = tf.get_variable("weight",[in_size,out_size], initializer= tf.truncated_normal_initializer(stddev=0.1))
			b = tf.get_variable("biases",[out_size], initializer= tf.constant_initializer(0.0))
			inputs = tf.nn.relu(tf.matmul(inputs,w)+b )
			in_size = layer_dimension[i]

	theta = tf.get_variable("theta",[out_size,OUTPUT_CLASS],initializer= tf.truncated_normal_initializer(stddev=0.1))
	logits = tf.matmul(inputs,theta)

	total_loss = tf.reduce_sum(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y_t))/batch_size
	tf.summary.scalar('total_loss',total_loss)

	train_op = tf.train.GradientDescentOptimizer(0.01).minimize(total_loss)
	merged = tf.summary.merge_all()

	X, Y = get_data(HIGGS_DIR)
	init = tf.global_variables_initializer()
	with tf.Session() as sess:
		sess.run(init)
		writer=tf.summary.FileWriter('./logs1',tf.get_default_graph())  
		for i in range(train_step):
			start = (i * batch_size) % dataset_size
			end = min(start+batch_size,dataset_size)
			print i
			print "total_loss"
			print sess.run(total_loss, feed_dict={x:X[start:end], y_t:Y[start:end]})
			summary, _ = sess.run([merged, train_op],feed_dict={x:X[start:end], y_t:Y[start:end]})
			writer.add_summary(summary, i)

	writer.close()

if __name__ == "__main__":
	build_graph()

