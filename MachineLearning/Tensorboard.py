#!/usr/bin/env python
# encoding: utf-8
"""
@author: taoxuefeng
@file: Tensorboard.py
@time: 2019/1/22 22:40
@desc:可视化练习

"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def add_layer(inputs, int_size, out_size, activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([int_size, out_size]),name='W')
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data)-0.5+noise

with tf.name_scope('input'):
    xs = tf.placeholder(tf.float32,[None,1],name='x_input')
    ys = tf.placeholder(tf.float32,[None,1],name='y_input')

# 定义隐藏层
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# 输出层
prediction = add_layer(l1, 10, 1, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                                    reduction_indices=[1]))
with tf.name_scope('train_step'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

writer = tf.summary.FileWriter("pythontest/machineLearning/", sess.graph)
# 可视化
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50:
        # print(sess.run(loss, feed_dict={xs:x_data,ys:y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data, ys: y_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)

        plt.pause(0.2)