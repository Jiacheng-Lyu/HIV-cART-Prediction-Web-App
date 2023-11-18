# HIV-cART-Prediction-Web-App
This is a Medical Prediction App which can be used to predict the follow up cART response state of the patients affected by HIV in the future.

**Serum proteome profiling reveals novel clinical and biology insights after HIV combination antiretroviral therapy**

Fang Liu, Jiacheng Lyu, Jianhua Yu, Tao Ji, Yuanyuan Wang, Zeya Xu, Jianfeng Bao, Lin Bai, Lizhi Xue, Lingli Zhu, Jiamin Li, Kai Li, Miaochan Wang, Huaguo Shao, Ling Li, Xiaoxiao Huang, Jinsong Huang, Chen Ding

## Predict Task Description
> This app is used to predict the follow up response state of the cART for the patients affected by the HIV. The follow up predicted window include:
* 3 to 6 months
* 6 to 9 months
* 9 to 12 months
* more than 12 months

> With three different input features:

|Input feature type|Features|
|:---|:---|
|Clinical features|the age when first receiving cART<br />the current age<br />the count of CD4+ T cell when first receiving cART<br />the current count of CD4+ T cell|
|Proteome features|APOL1, ACACA, SERPIND1, MYH14, PKM, SYNE1|
|Combined clinical & proteome features|Clinical features and Proteome features|


## Environment Requirement
The following package / library versions were used in this study:
* python (version 3.9.18)
* streamlit (version 1.28.2)
* numpy (version 1.26.0)
* scikit-learn (version 1.2.1)

## Folders Structure
* *models*: which contains all the models for each of input features and each of predicted windows.

## Link To The Web Application
Predict the follow-up response (https://hiv-cart-followup-prediction-web-app.streamlit.app/)
