# noinspection PyUnresolvedReferences
from beagles.backend.darknet.layer import Layer
from beagles.backend.darknet.convolution import *
from beagles.backend.darknet.connected import *
from beagles.backend.darknet.rnn import *


class avgpool_layer(Layer):
    def setup(self):
        """Not Implemented"""
        pass

    def finalize(self, *args):
        """Not Implemented"""
        pass


class crop_layer(Layer):
    def setup(self):
        """Not Implemented"""
        pass

    def finalize(self, *args):
        """Not Implemented"""
        pass


# noinspection PyAttributeOutsideInit
class upsample_layer(Layer):
    def setup(self, stride, h, w):
        self.stride = stride
        self.height = h
        self.width = w

    def finalize(self, *args):
        """Not Implemented"""
        pass


# noinspection PyAttributeOutsideInit
class shortcut_layer(Layer):
    def setup(self, from_layer):
        self.from_layer = from_layer

    def finalize(self, *args):
        """Not Implemented"""
        pass


# noinspection PyAttributeOutsideInit
class maxpool_layer(Layer):
    def setup(self, ksize, stride, pad):
        self.stride = stride
        self.ksize = ksize
        self.pad = pad

    def finalize(self, *args):
        """Not Implemented"""
        pass


# noinspection PyAttributeOutsideInit
class softmax_layer(Layer):
    def setup(self, groups):
        self.groups = groups

    def finalize(self, *args):
        """Not Implemented"""
        pass


class dropout_layer(Layer):
    def setup(self, p):
        self.h['pdrop'] = dict({
            'feed': p,  # for training
            'dfault': 1.0,  # for testing
            'shape': ()
        })

    def finalize(self, *args):
        """Not Implemented"""
        pass


# noinspection PyAttributeOutsideInit
class route_layer(Layer):
    def setup(self, routes):
        self.routes = routes

    def finalize(self, *args):
        """Not Implemented"""
        pass


# noinspection PyAttributeOutsideInit
class reorg_layer(Layer):
    def setup(self, stride):
        self.stride = stride

    def finalize(self, *args):
        """Not Implemented"""
        pass


darkops = {
    'dropout': dropout_layer,
    'connected': connected_layer,
    'maxpool': maxpool_layer,
    'shortcut': shortcut_layer,
    'upsample': upsample_layer,
    'convolutional': convolutional_layer,
    'avgpool': avgpool_layer,
    'softmax': softmax_layer,
    'crop': crop_layer,
    'local': local_layer,
    'select': select_layer,
    'route': route_layer,
    'reorg': reorg_layer,
    'conv-select': conv_select_layer,
    'conv-extract': conv_extract_layer,
    'extract': extract_layer,
    'lstm': lstm_layer,
    'rnn': rnn_layer,
    'gru': gru_layer
}


def create_darkop(ltype: str, num: int, *args):
    op_class = darkops.get(ltype, Layer)
    return op_class(ltype, num, *args)
