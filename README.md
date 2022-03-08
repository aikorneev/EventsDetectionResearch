# EventsDetectionResearch

Nowadays social networks are of vital importance for a lot of people. Over half of the world’s population uses social networks to express emotions, share their thoughts and support social relationships. Regular users publish information about their daily life, organizers of mass events broadcast public content via official pages. This trend makes social networks a useful data source for a variety of tasks dedicated to the analysis of urban processes. Such data allows creating, for example, recommendation or crime monitoring systems based on detecting multi scale events. Moreover, previous studies have revealed that information about remarkable events, such as hurricanes, earthquakes and floods, appears in social networks faster than in traditional media.

Among the diversity of social networks, Instagram and Twitter are the most suitable for event detecting task. Both of them are extremely wide-spread and continue to increase in popularity. Publications may contain not only text data, images or videos, some of them are pinned to particular locations and time stamps, which simplifies the identification of events. However, data from these social media contains a large amount of noise: publications with food, clothes, spam or advertisements do not reflect information about any event and lead to poor results.

In order to detect new events authors of the most advanced solutions usually use historical data and predict the number of new publications for specific locations. Algorithms based on this scheme recognize candidates if the predicted value is lower than the real one. This idea allows obtaining admissible results for detecting large scale events, but such approaches oftentimes are not sensible enough to cover private or local events. However, semantic analysis of content might help to solve not only the challenging task of low scale events detecting, but also to filter publications that contain noise information and complicate events detection in general.

This repository contains different scripts\notebooks\data related to the research of Event Detection Problem. 

+ **models_test** - small scripts for testing LDA and BERT models in the scope of event detection problem (not described well enough, mainly raw code).
+ + **notebooks** - jupyter notebooks with different solutions related to Instagram and KudaGo data (described with own readme).
+ + **scripts** - scripts for KudaGo data crawling, preprocessing and preparation for future analysis.
