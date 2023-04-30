_base_ = './llff_default.py'

expname = 'candle_ldr'

data = dict(
    datadir='./data/rawnerf/scenes/candle',
)

fine_train = dict(
    N_iters=50000,
)

exposure = None
activation_bias = 0.0