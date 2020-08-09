# Pytorch-CycleGAN
Hello老铁们好！这是一个可读性很高的`CycleGAN`(https://arxiv.org/abs/1703.10593)的`Pytorch`实现

Fork 自：https://github.com/aitorzip/PyTorch-CycleGAN

## 环境要求
代码运行在`Python 3.6.x`，还没有测试之前的`Python`版本

### [PyTorch & torchvision](http://pytorch.org/)
参考网站[pytorch.org](http://pytorch.org) 安装`Pytorch`环境

### [Visdom](https://github.com/facebookresearch/visdom)
为了在nice的Web浏览器中绘制loss图并绘制生成图像，我们需要安装`visdom`
```
pip3 install visdom
```

### wget
为了下载数据集需要安装 `wget` 库，国内下载极慢，推荐手动下载

```
pip3 install wget
```

## Training
### 1. 数据集下载

首先，我们需要搞定数据集。最简单的方式使用 UC Berkeley's repository 的数据集仓库：

```
./download_dataset <数据集名字>
```
可以用的 <数据集名字> 有: apple2orange, summer2winter_yosemite, horse2zebra, monet2photo, cezanne2photo, ukiyoe2photo, vangogh2photo, maps, cityscapes, facades, iphone2dslr_flower, ae_photos

另外，您可以根据以下目录结构来构建自己的数据集：

    .
    ├── datasets                   
    |   ├── <dataset_name>         # i.e. brucewayne2batman
    |   |   ├── train              # Training
    |   |   |   ├── A              # Contains domain A images (i.e. Bruce Wayne)
    |   |   |   └── B              # Contains domain B images (i.e. Batman)
    |   |   └── test               # Testing
    |   |   |   ├── A              # Contains domain A images (i.e. Bruce Wayne)
    |   |   |   └── B              # Contains domain B images (i.e. Batman)

### 2. Train!
```
./train --dataroot datasets/<dataset_name>/ --cuda
```
此命令将使用 *dataroot/train* 目录下的图像以及原作者提供超参数开始训练.

我们可以随意设置超参数，可以使用 `./train --help` 查看超参数描述.

生成器和判别器的权重都将保存在目录`output `下。

如果您没有GPU，请删除`--cuda`选项，尽管建议用GPU!

您还可以通过在另一个终端中运行`python3 -m visdom`并打开[http://localhost:8097/](http://localhost:8097/)来查看训练进度以及实时输出图像。



在这可以看到 **train loss** 进度，如下所示 (默认参数，使用horse2zebra数据集):

![Generator loss](https://github.com/ai-tor/PyTorch-CycleGAN/raw/master/output/loss_G.png)
![Discriminator loss](https://github.com/ai-tor/PyTorch-CycleGAN/raw/master/output/loss_D.png)
![Generator GAN loss](https://github.com/ai-tor/PyTorch-CycleGAN/raw/master/output/loss_G_GAN.png)
![Generator identity loss](https://github.com/ai-tor/PyTorch-CycleGAN/raw/master/output/loss_G_identity.png)
![Generator cycle loss](https://github.com/ai-tor/PyTorch-CycleGAN/raw/master/output/loss_G_cycle.png)

## Testing
```
./test --dataroot datasets/<dataset_name>/ --cuda
```
测试将使用 *dataroot/test*  目录下的图片, 通过生成器运行，并将输出保存在*output/A* 和 *output/B* 目录下. 就像训练一样，测试时，也可以更改参数，从 `./test --help`查看更多信息.

生成图片的例子(默认的参数，数据集为 `horse2zebra` ):



![Real horse](https://github.com/ai-tor/PyTorch-CycleGAN/raw/master/output/real_A.jpg)
![Fake zebra](https://github.com/ai-tor/PyTorch-CycleGAN/raw/master/output/fake_B.png)
![Real zebra](https://github.com/ai-tor/PyTorch-CycleGAN/raw/master/output/real_B.jpg)
![Fake horse](https://github.com/ai-tor/PyTorch-CycleGAN/raw/master/output/fake_A.png)

## 开源协议
本项目使用GPL v3协议，可以从 [LICENSE.md](LICENSE.md) 查看细节.

## 致谢
Code is basically a cleaner and less obscured implementation of [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). 

All credit goes to the authors of [CycleGAN](https://arxiv.org/abs/1703.10593), Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A.