import tensorflow as tf
from tensorflow.keras.regularizers import L1L2, l1
from tensorflow.keras.losses import hinge
from libs.io.flags import FlagIO

_LOSS_TYPE = ['sse', 'l2', 'smooth', 'sparse', 'l1', 'softmax']


def loss(self, net_out):
    m = self.meta
    loss_type = m['type'].strip('[]')
    out_size = m['out_size']
    H, W, _ = m['inp_size']
    HW = H * W
    loss = float()
    try:
        assert loss_type in _LOSS_TYPE, \
            'Loss type {} not implemented'.format(loss_type)
    except AssertionError as e:
        self.flags.error = str(e)
        self.logger.error(str(e))
        FlagIO.send_flags(self)
        raise

    self.logger.info('{} loss hyper-parameters:'.format(m['model']))
    self.logger.info('Input Grid Size   = {}'.format(HW))
    self.logger.info('Number of Outputs = {}'.format(out_size))

    out = net_out
    out_shape = out.get_shape()
    out_dtype = out.dtype.base_dtype
    _truth = tf.compat.v1.placeholder(out_dtype, out_shape)

    self.placeholders = dict({
        'truth': _truth
    })

    diff = _truth - out
    if loss_type in ['sse', '12']:
        loss = tf.nn.l2_loss(diff)

    elif loss_type == ['smooth']:
        small = tf.cast(diff < 1, tf.float32)
        large = 1. - small
        loss = L1L2(tf.multiply(diff, large), tf.multiply(diff, small))

    elif loss_type in ['sparse', 'l1']:
        loss = l1(diff)

    elif loss_type == 'softmax':
        loss = tf.nn.softmax_cross_entropy_with_logits(logits=net_out)
        loss = tf.reduce_mean(loss)

    self.loss = loss

    # elif loss_type == 'svm':
    #     assert 'train_size' in m, \
    #         'Must specify'
    #     size = m['train_size']
    #     self.nu = tf.Variable(tf.ones([self.flags.size, self.num_classes]))
    #     self.loss(hinge(self.nu))