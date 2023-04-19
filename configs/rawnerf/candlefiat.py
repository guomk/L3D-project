_base_ = './raw_default.py'

expname = 'rawnerf_candlefiat'

data = dict(
    datadir='./data/rawnerf/scenes/candlefiat',
    factor=1,
)

fine_train = dict(
    N_iters=50000,
)

