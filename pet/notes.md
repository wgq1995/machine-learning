# 0.431 kernel Q:
## sentiment
* sentiment only sum
* entities.type 未区分
* entities.mentions.type未区分
## sentiment notes
* categories, tokens都为空
* documentSentiment里只有２个元素，如{'magnitude': 3.1, 'score': 0.3}
* sentences每条记录类似于：{'text': {'content': 'Hi.', 'beginOffset': -1}, 'sentiment': {'magnitude': 0.2, 'score': 0.2}}
* entities每条记录类似于：{'name': 'someone', 'type': 'PERSON', 'metadata': {}, 'salience': 0.36503658, 'mentions': [{'text': {'content': 'someone', 'beginOffset': -1}, 'type': 'COMMON'}, {'text': {'content': 'someone', 'beginOffset': -1}, 'type': 'COMMON'}]}
## metadata
* metadata only mean
# drop 
    NMF_labelAnnotations_description_2
    PhotoAmt
    Type
    cropHintsAnnotation_cropHints_confidence_VAR
    cropHintsAnnotation_cropHints_confidence_SUM
    cropHintsAnnotation_cropHints_confidence_MEAN
    Name
    VideoAmt
    labelAnnotations_topicality_max_SUM
    cropHintsAnnotation_cropHints_importanceFraction_SUM
    labelAnnotations_topicality_mean_SUM
    labelAnnotations_topicality_min_SUM
    labelAnnotations_topicality_std_SUM
    documentSentiment_score
    labelAnnotations_topicality_min_VAR
    
