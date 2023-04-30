_base_ = './raw_default.py'

expname = 'rawnerf_candlefiat_tm_exp'

data = dict(
    datadir='./data/rawnerf/scenes/candlefiat',
    factor=2,
)

fine_train = dict(
    N_iters=50000,
)

