_base_ = './raw_default.py'

expname = 'rawnerf_gardenlights'

data = dict(
    datadir='./data/rawnerf/scenes/gardenlights',
    factor=8,
)

fine_train = dict(
    N_iters=50000,
)

