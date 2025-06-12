# Installation 
```
# -- We run on python==3.10 and PyTorch2 with CUDA 12.8  
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128 
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
* `fvcore` and `iopath` are needed for PyTorch3D. 
* `FORCE_CUDA="1"`: An environment variable that the CUDA kernel should be compiled.
* `CUDA_HOME=/usr/local/cuda-12.8`: The path of CUDA Toolkit
* `pip install .`: Install it in this directory.



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
