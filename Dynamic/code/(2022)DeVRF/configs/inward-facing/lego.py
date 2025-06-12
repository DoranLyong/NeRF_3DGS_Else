_base_ = './default.py'

expname = 'lego_test'
basedir = './logs'

data = dict(
    datadir='/home/cvipl-ubuntu/Workspace/Active/3DGS/DeVRF/dataset/inward-facing/lego/dynamic_4views',
    dataset_type='blender',
    white_bkgd=True,
)

fine_train = dict(
    static_model_path = "/home/cvipl-ubuntu/Workspace/Active/3DGS/DeVRF/static_DirectVoxGO/logs/lego_test/fine_last.tar",
)
