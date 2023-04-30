_base_ = './raw_default.py'

expname = 'rawnerf_bikes_tm_exp'

data = dict(
    datadir='./data/rawnerf/scenes/bikes',
    factor=4,
)

fine_train = dict(
    N_iters=50000,
)

