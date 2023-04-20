_base_ = '../default.py'

basedir = './logs/rawnerf'

data = dict(
    dataset_type='raw',
    ndc=True,
    factor=4,
)

coarse_train = dict(
    N_iters=0,
)

fine_train = dict(
    N_iters=30000,
    # N_iters=5000,
    N_rand=4096,
    weight_distortion=0.01,
    pg_scale=[2000,4000,6000,8000],
    ray_sampler='flatten',
    tv_before=1e9,
    tv_dense_before=10000,
    weight_tv_density=1e-5,
    weight_tv_k0=1e-6,
)

fine_model_and_render = dict(
    num_voxels=256**3,
    mpi_depth=256,
    rgbnet_dim=12,
    rgbnet_width=128,
    world_bound_scale=1,
    fast_color_thres=1e-3,
)

exposure = None
activation_bias = 0.0

