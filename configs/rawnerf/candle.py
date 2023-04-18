_base_ = './raw_default.py'

expname = 'rawnerf_candle'

data = dict(
    datadir='./data/rawnerf/scenes/candle',
    # datadir='./data/nerf_llff_data/room',
)

fine_train = dict(
    N_iters=50000,
)
