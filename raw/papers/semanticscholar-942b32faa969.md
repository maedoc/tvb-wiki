# Developing a real-time water quality simulation toolbox using machine learning and application programming interface.

**Source**: semantic-scholar
**ID**: 942b32faa9696068ae2e7ebc587e610d5d24b15e
**DOI**: 10.1016/j.jenvman.2025.124719
**URL**: https://www.semanticscholar.org/paper/942b32faa9696068ae2e7ebc587e610d5d24b15e
**Date**: 2025-02-28
**Year**: 2025
**Authors**: Gi-Hun Bang, Na-Hyeon Gwon, Min-Jeong Cho, Ji-Ye Park, Sang-Soo Baek
**Venue**: Journal of Environmental Management
**Citations**: 5

## Abstract

Rivers are vital for sustaining human life as they foster social development, provide drinking water, maintain aquatic ecosystems, and offer recreational spaces. However, most rivers are being increasingly contaminated by pollutants from non-point sources, urbanization, and other sources. Consequently, real-time river water quality modeling is essential for managing and protecting rivers from contamination, and its significance is growing across various sectors, including public health, agriculture, and water treatment systems. Therefore, a real-time river water quality simulation toolbox was developed using machine learning (ML) and an application program interface (API). To create the toolbox, models that simulated water quality parameters such as chlorophyll a (Chl-a), dissolved oxygen (DO), total nitrogen (TN), total organic carbon (TOC), and total phosphorus (TP) at each point in the Nakdong River were constructed. The models were constructed using Artificial neural network (ANN), Random Forest (RF), support vector machines (SVM), and data from API. Subsequently, hyperparameter optimization was conducted to enhance the model's performance. During training, the models' performances were evaluated and compared based on the data sampling method and ML algorithms. Models trained with random sampling data outperformed those trained with time-series data. Among the algorithm models that used random sampling data, the RF exhibited the best performance. The average coefficient of determination (R2) values for each water quality simulation with randomly sampled data using RF for DO, TN, TP, Chl-a, and TOC were 0.79, 0.65, 0.74, 0.45, and 0.48, respectively. For ANN, they were 0.7, 0.51, 0.64, 0.35, and 0.35, respectively, and for SVM, they were 0.73, 0.51, 0.59, 0.21, and 0.3, respectively. The Chl-a and TOC models exhibited relatively poor performance, whereas the DO, TN, and TP models demonstrated superior performance. Diversifying the input data variables is necessary to improve the performance of the Chl-a and TOC models. Sensitivity and uncertainty analyses were conducted to evaluate and enhance the models' understanding. Furthermore, using a graphic user interface (GUI) toolbox, user convenience was maximized.
