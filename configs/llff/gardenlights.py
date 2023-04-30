_base_ = './llff_default.py'

expname = 'gardenlights_ldr'

data = dict(
    datadir='./data/rawnerf/scenes/gardenlights',
)

fine_train = dict(
    N_iters=50000,
)

exposure = None
activation_bias = 0.0