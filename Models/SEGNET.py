# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rFYxp7La0QKrxlpPEx4y3kCAZZ958kFv
"""

from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers import Input
from keras.models import Model
from keras.layers import Layer
class MaxPooling2DWithIndices(Layer):
    def __init__(self, pool_size, strides, padding='SAME', **kwargs):
        super(MaxPooling2DWithIndices, self).__init__(**kwargs)
        self.pool_size = pool_size
        self.strides = strides
        self.padding = padding
        return

    def call(self, x):
        pool_size = self.pool_size
        strides = self.strides
        if isinstance(pool_size, int): ps = [1, pool_size, pool_size, 1]
        else: ps = [1,pool_size[0],pool_size[1],1]
        if isinstance(strides,int): st = [1, strides, strides, 1]
        else: st = [1, strides[0], strides[1], 1]
        mpooled, indices = tf.nn.max_pool_with_argmax(x, ps, st, self.padding)
        return [mpooled, indices]

    def compute_output_shape(self, input_shape):
        if isinstance(self.pool_size,int):
            output_shape = (input_shape[0], input_shape[1]//self.pool_size, input_shape[2]//self.pool_size, input_shape[3])
        else: output_shape = (input_shape[0], input_shape[1]//self.pool_size[0], input_shape[2]//self.pool_size[1], input_shape[3])
        return [output_shape,output_shape]

class MaxUnpooling2DWithIndices(Layer):
    def __init__(self, **kwargs):
        super(MaxUnpooling2DWithIndices, self).__init__(**kwargs)
        return
        
    def call(self,x):
        argmax=K.cast(K.flatten(x[1]),'int32')
        max_value=K.flatten(x[0])
        with tf.variable_scope(self.name):
            input_shape=K.shape(x[0])
            batch_size=input_shape[0]
            image_size=input_shape[1]*input_shape[2]*input_shape[3]
            output_shape=[input_shape[0],input_shape[1]*2,input_shape[2]*2,input_shape[3]]
            indices_0=K.flatten(tf.matmul(K.reshape(tf.range(batch_size),(batch_size,1)),K.ones((1,image_size),dtype='int32')))
            indices_1=argmax%(image_size*4)//(output_shape[2]*output_shape[3])
            indices_2=argmax%(output_shape[2]*output_shape[3])//output_shape[3]
            indices_3=argmax%output_shape[3]
            indices=tf.stack([indices_0,indices_1,indices_2,indices_3])
            output=tf.scatter_nd(K.transpose(indices),max_value,output_shape)
            return output

    def compute_output_shape(self, input_shape):
        return input_shape[0][0],input_shape[0][1]*2,input_shape[0][2]*2,input_shape[0][3]

class SegNet:
    def __init__(self, depth = 64):
        self.depth = depth

    def CompositeConv2D(self, input_layer, num_convs, filters):
        output = input_layer
        for i in range(num_convs):
            output = Conv2D(filters, kernel_size=(3, 3), padding='same', activation="relu")(output)
            output = BatchNormalization(axis=3)(output)
        return output
        
    def encoder(self, input_layer):
        encoded_out = self.CompositeConv2D(input_layer, 2, self.depth)
        encoded_out, indices1 = MaxPooling2DWithIndices(pool_size=2,strides=2)(encoded_out)

        encoded_out = self.CompositeConv2D(encoded_out, 2, self.depth)
        encoded_out, indices2 = MaxPooling2DWithIndices(pool_size=2,strides=2)(encoded_out)

        encoded_out = self.CompositeConv2D(encoded_out, 3, self.depth)
        encoded_out, indices3 = MaxPooling2DWithIndices(pool_size=2,strides=2)(encoded_out)

        encoded_out = self.CompositeConv2D(encoded_out, 3, self.depth)
        encoded_out, indices4 = MaxPooling2DWithIndices(pool_size=2,strides=2)(encoded_out)

        encoded_out = self.CompositeConv2D(encoded_out, 3, self.depth)
        encoded_out, indices5 = MaxPooling2DWithIndices(pool_size=2,strides=2)(encoded_out)

        return [encoded_out, indices1, indices2, indices3, indices4, indices5]

    def decoder(self, encoded_out, indices1, indices2, indices3, indices4, indices5):
        decoded_out = MaxUnpooling2DWithIndices()([encoded_out, indices5])
        decoded_out = self.CompositeConv2D(decoded_out, 3, self.depth)

        decoded_out = MaxUnpooling2DWithIndices()([decoded_out, indices4])
        decoded_out = self.CompositeConv2D(decoded_out, 3, self.depth)

        decoded_out = MaxUnpooling2DWithIndices()([decoded_out, indices3])
        decoded_out = self.CompositeConv2D(decoded_out, 3, self.depth)

        decoded_out = MaxUnpooling2DWithIndices()([decoded_out, indices2])
        decoded_out = self.CompositeConv2D(decoded_out, 2, self.depth)

        decoded_out = MaxUnpooling2DWithIndices()([decoded_out, indices1])
        decoded_out = self.CompositeConv2D(decoded_out, 2, self.depth)
        
        return decoded_out

    def SegNet(self, input_shape):
        self.depth = 40;
        input_layer = Input(shape=input_shape)
        encoded_out, indices1, indices2, indices3, indices4, indices5 = self.encoder(input_layer)
        decoded_out = self.decoder(encoded_out, indices1, indices2, indices3, indices4, indices5)
        decoded_out = Conv2D(1, kernel_size=(3, 3), padding="same", activation="sigmoid")(decoded_out)
        model = Model(input_layer, decoded_out)
        return model