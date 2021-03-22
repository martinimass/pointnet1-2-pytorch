# Pytorch Implementation of PointNet and PointNet++   
This repo is an implementation for [PointNet](http://openaccess.thecvf.com/content_cvpr_2017/papers/Qi_PointNet_Deep_Learning_CVPR_2017_paper.pdf) and [PointNet++](http://papers.nips.cc/paper/7095-pointnet-deep-hierarchical-feature-learning-on-point-sets-in-a-metric-space.pdf) in pytorch.  

The following code is based on the implementation of [yanx27](https://github.com/yanx27/Pointnet_Pointnet2_pytorch ), appropriately modified to use generic datasets. The original version was customised to use only the S3DIS dataset.

  
## Update  
**2021/03/22:**  
  
(1) Generalised the code for the Semantic Segmentation task.

(2) Added the choice to use the ArCH dataset.

(3) Added preprocessing code to use any type of dataset.
  
  
## Semantic Segmentation  - S3DIS
### Data Preparation  
Download 3D indoor parsing dataset (**S3DIS**) [here](http://buildingparser.stanford.edu/dataset.html)  and save in `data/Stanford3dDataset_v1.2_Aligned_Version/`.  
```  
cd data_utils  
python collect_indoor3d_data.py  
```  
Processed data will save in `data/stanford_indoor3d/`.  
### Run  
```  
## Check model in ./models ## E.g. pointnet2_ssg  
python train_semseg.py --model pointnet2_sem_seg --test_area 5 --log_dir pointnet2_sem_seg  
python test_semseg.py --log_dir pointnet2_sem_seg --test_area 5 --visual  
```  
Visualization results will save in `log/sem_seg/pointnet2_sem_seg/visual/` and you can visualize these .obj file by [MeshLab](http://www.meshlab.net/).  

## Semantic Segmentation  - ArCH
### Data Preparation  
Download Cultural Heritage dataset (**ArCH**) [here](http://archdataset.polito.it/)  and save it in `data/arch-original/`.  

### Data Preprocessing  
```  
cd data_utils  
python prepare_arch.py  
```  
Processed data will be saved in `data/arch-conv/`.  This script allowed the dataset to be converted into the same structure as the S3DIS daset.
Within this script it is possible to define only one of the two scenes to be used for the test (SceneA or SceneB). You cannot use both at the same time as the code has been designed to use only one scene at a time.

```  
python collect_indoor3d_data_arch.py  
```  
Processed data will be saved in `data/arch-npy/`.  
This is the data that will be used for the training and testing phases.

### Training/Test phase
```  
python train_semseg.py --model pointnet2_sem_seg --test_area 16 --log_dir pointnet2_sem_seg --dataset ArCH 
python test_semseg.py --log_dir pointnet2_sem_seg --test_area 16 --visual --dataset ArCH  
```  
Compared to the original code, I have added the *--dataset* parameter in order to be able to choose the dataset to be used.

##  How to use a Custom Dataset
To add a new dataset, you can follow the same steps as I did:

 - the dataset must be composed of point clouds saved in .txt files,
   with this structure: `x y z r g b label`
 - the dataset should be saved in a folder, which will then be used by the *prepare_arch.py* script;
 - you have to create your own version of the following scripts: 
	 - *prepare_arch*
	 - *collect_indoor3d_data_arch*
	 - *indoor3d_util_arch*
	 - *ArCHDataloader*
 - you have to adapt the scripts *train_semseg.py* and *test_semseg.py* to use this new dataset.

  
## Reference By  
[yanx27/Pointnet_Pointnet2_pytorch](https://github.com/yanx27/Pointnet_Pointnet2_pytorch) <br>  
[charlesq34/PointNet](https://github.com/charlesq34/pointnet) <br>  
[charlesq34/PointNet++](https://github.com/charlesq34/pointnet2)  
  
## Environments  
Ubuntu 16.04 <br>  
Python 3.6.7 <br>  
Pytorch 1.1.0
