# Installation 
```
# -- Tested Env.
python==3.10, torch==2.7.1+cu128
```

```bash
# -- C++ for miniconda 
conda install -c conda-forge libstdcxx-ng
```

Install `Pytorch3D` 
```bash
pip install fvcore iopath
git clone https://github.com/facebookresearch/pytorch3d.git
cd pytorch3d 

FORCE_CUDA="1" CUDA_HOME=/usr/local/cuda-12.8 pip install .
```

Install `mmcv` and `mmengine` for config system.
```bash
pip install -U openmim
mim install mmengine==0.10.7
mim install mmcv==2.2.0
```

Install remain packages using `pip`
```bash
torch_scatter
scipy
lpips
imageio
imageio-ffmpeg
einops
Ninja
opencv-python
tqdm
```
