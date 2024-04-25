
<div align="center"> 

## EKMM: 利用外部知识增强的多模态命名实体识别

</div>
<div align="center">
      简体中文| <a href="README_EN.md" >English</a>
  </div>

**介绍**

EKMM项目（外部知识多模态命名实体识别）专注于通过整合大型语言模型作为动态外部知识源，目标是在各种多模态场景中实现更准确和高效的实体识别。

**背景**

多模态命名实体识别在理解复杂数据源中扮演着关键角色，特别是在社交媒体、新闻报道等领域。传统方法通常只依赖于有限的模态来识别实体，而忽视了外部大型知识库的潜力。此前也有项目尝试通过外部知识（wiki）增强实现任务，也很有效的打败了传统方法。基于前人的经验，我们提出了EKMM项目，EKMM通过融合文本和图像的数据，并结合外部模型生成的深层次知识，极大地提高了识别的准确性和鲁棒性。


## 快速体验
- 请阅读[快速体验](docs/quick_start.md)查阅


## 🎇最近更新
- 【2024.4.25】项目立项

## 🎛项目结构




## 📌实现

### Requirements

```
python==3.7.10

```

### Data
- Twitter15_Twitter17数据集
    - text部分：`/data/twitter2015` and `/data/twitter2017`
    - image部分：[下载链接](https://pan.baidu.com/s/15JN6BK9RBXyeLKZMV2vkCw?pwd=mner)

### OCR part
- 在此我们使用OCR文本检测与识别模型得到图片中更多的信息，包括文字、位置等信息。
- 在此使用通用领域中英都可以识别的的[读光-文字识别-行识别模型](https://www.modelscope.cn/models/iic/cv_convnextTiny_ocr-recognition-general_damo/summary)与[读光-文字检测-行检测模型](https://www.modelscope.cn/models/iic/cv_resnet18_ocr-detection-db-line-level_damo/summary)，具体请阅读[OCR部分](https://modelscope.cn/headlines/article/42)查阅。
- 代码实现于`/code/ocr_module.py`

