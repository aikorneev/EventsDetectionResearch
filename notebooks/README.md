# EventsDetectionResearch/notebooks/
Random notebooks for solving different tasks dedicated to the Event Detection probplem.

+ **InstARL** - Association rules obtaining for Instagram posts hastags. Rules distribution analysis. Completed for St.Petersburg dataset. An interesting observation: this analysis can be possibly used in oder to obtaing post clusters (also potentially useful for advertisment detection).
+ **KudaGo2EventData** - Connecting two datasets: first one is obtained via KidaGo API, second one is Instagram posts. To connect rows of both table one uses location (lat, lon) and timestamps with tunable shifts.
+ **KudagoCategories** - Analysis of categories and hashtags interconnections in KudaGo dataset. SuperVenn visualisation applying. ARL analysis.
+ **dataFilterSBERT** - Testing of dataset filtering approach based on semantic classification. This unsupervised approach allos distinguishing events and noise\advertisement posts with predefined classes (independent from dataset, but might be adjusted). Using of 
[paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) model to obtain embeddings.
+ **getEngPosts** - Notebook to obtain English posts for particular time period (manually tuned period). Based on [
xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection) model.