_base_ = './raw_default.py'

expname = 'rawnerf_stove_tm_exp_noshutter'

data = dict(
    datadir='./data/rawnerf/scenes/stove',
)

fine_train = dict(
    N_iters=50000,
)
