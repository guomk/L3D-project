_base_ = './raw_default.py'

expname = 'rawnerf_bikes'

data = dict(
    datadir='./data/rawnerf/scenes/bikes',
    factor=4,
)

fine_train = dict(
    N_iters=10000,
)

