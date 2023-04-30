_base_ = './raw_default.py'

expname = 'rawnerf_windowlegovary_tm_exp'

data = dict(
    datadir='./data/rawnerf/scenes/windowlegovary',
)

fine_train = dict(
    N_iters=50000,
)

activation_bias = 0