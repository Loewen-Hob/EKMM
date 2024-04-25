#### EKMM: Enhancing Multimodal Named Entity Recognition with External Knowledge

**Introduction**

The EKMM project (External Knowledge Multimodal Named Entity Recognition) is an innovative multimodal entity recognition system focused on integrating large language models as dynamic external knowledge sources to enhance the performance of entity recognition across text and image data. The aim is to achieve more accurate and efficient entity recognition in various multimodal scenarios.

**Background**

Multimodal Named Entity Recognition plays a key role in understanding complex data sources, especially in areas like social media and news reporting. Traditional methods typically rely on limited modalities to recognize entities, overlooking the potential of external large knowledge bases. Previous projects have successfully leveraged external knowledge (e.g., Wikipedia) to outperform traditional methods. Building on this experience, we introduce the EKMM project, which significantly improves accuracy and robustness by integrating text and image data with deep insights generated from external models.

**Methodology**

The EKMM project optimizes multimodal named entity recognition through the following steps:
1. **Data Fusion**: Combines text and image data to extract relevant features.
2. **Knowledge Generation**: Utilizes large models like InternLM to dynamically generate external knowledge relevant to the current data.

**Implementation**
- **Data Collection**: Gather multimodal datasets containing text and images.
- **Data Preprocessing**: Cleanse and standardize the multimodal datasets.
- **Model Training**: Train the multimodal named entity recognition model within a framework that includes external knowledge integration.
- **Evaluation and Optimization**: Assess model performance on standard datasets and optimize based on results.

### Quick Start
- Please refer to [Quick Start](docs/quick_start.md) for more information.

### 🎇Recent Updates
- [April 25, 2024] Project initiation
