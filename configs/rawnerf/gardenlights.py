_base_ = './raw_default.py'

expname = 'rawnerf_gardenlights3'

data = dict(
    datadir='./data/rawnerf/scenes/gardenlights',
    factor=8,
)

fine_train = dict(
    N_iters=5000,
)

exposure = None
activation_bias = -0.5

