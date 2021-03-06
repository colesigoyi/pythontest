#!/usr/bin/env python
# encoding: utf-8
"""
@author: taoxuefeng
@file: Minist_data_test.py
@time: 2019/1/27 18:14
@desc:

"""
from __future__ import print_function
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np

old_v = tf.logging.get_verbosity()
tf.logging.set_verbosity(tf.logging.ERROR)

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

def add_layer(inputs, int_size, out_size, activation_function=None):
        Weights = tf.Variable(tf.random_normal([int_size, out_size]),name='W')
        biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
        Wx_plus_b = tf.matmul(inputs, Weights) + biases

        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

def compute_accuarcy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

#搭建网络
xs = tf.placeholder(tf.float32, [None, 784])   #28*28
ys = tf.placeholder(tf.float32, [None, 10])

tf.logging.set_verbosity(old_v)

prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                              reduction_indices=[1])) #loss

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(10000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
    if i % 500 ==0:
        print(compute_accuarcy(
            mnist.test.images, mnist.test.labels))