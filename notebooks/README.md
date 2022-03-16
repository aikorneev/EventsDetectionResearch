# EventsDetectionResearch/notebooks/
Random notebooks for solving different tasks dedicated to the Event Detection problem.

+ **Anomalies2Events** - Obtaining connected posts for each determined event from anomalies data (obtained from [convolutional quadtrees algorithm](https://dl.acm.org/doi/abs/10.1145/3282866.3282867 )). Using of CUML library: UMAP + clustering methods. For now in progress.
+ **InstARL** - Association rules obtaining for Instagram posts hashtags. Rules distribution analysis. Completed for St.Petersburg dataset. An interesting observation: this analysis can be possibly used in order to obtain post clusters (also potentially useful for advertisement detection).
+ **KudaGo2EventData** - Connecting two datasets: first one is obtained via KidaGo API, second one is Instagram posts. To connect rows of both tables one uses location (lat, lon) and timestamps with tunable shifts.
+ **KudagoCategories** - Analysis of categories and hashtags interconnections in KudaGo dataset. SuperVenn visualization applying. ARL analysis.
+ **dataFilterSBERT** - Testing of dataset filtering approach based on semantic classification. This unsupervised approach allows distinguishing events and noise\advertisement posts with predefined classes (regardless of dataset, but might be adjusted). Using of 
[paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) model to obtain embeddings.
+ **getEngPosts** - Notebook to obtain English posts for particular time period (manually tuned period). Based on [
xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection) model.
