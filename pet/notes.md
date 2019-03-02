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
## metadata notes
* {drop'faceAnnotations', 'labelAnnotations', 'textAnnotations', 'imagePropertiesAnnotation', 'cropHintsAnnotation'}5种
#  select
    Breed1
    RescuerID
    Age 
    Breed2
    State 
    SVD_Description_2
    Entities_other_salience_max
    SVD_labelAnnotations_description_2
    SVD_labelAnnotations_description_0
    labelAnnotations_score_max_MAX
    Entities_other_salience_min
    NMF_Description_2 
    Fee 
    Entities_other_salience_sum 
    Entities_other_salience_std 
    Sentences_text_sentiment_score_mean
    NMF_Description_4 
    labelAnnotations_score_min_MIN 
    Entities_other_salience_mean
    SVD_labelAnnotations_description_4
    Quantity
    imagePropertiesAnnotation_colors_color_score_min_VAR
    NMF_Entities_name_0 
    Sentences_text_sentiment_magnitude_mean
    Color2
    Sentences_text_sentiment_magnitude_std 
    imagePropertiesAnnotation_colors_color_score_min_MIN
    NMF_Entities_name_2 
    SVD_Description_3 
    SVD_Entities_name_3 
    SVD_Description_1
    NMF_Description_0 
    Sentences_text_sentiment_score_std 
    Color1 
    SVD_Entities_name_4 
    SVD_labelAnnotations_description_3 
    imagePropertiesAnnotation_colors_color_score_mean_VAR
    NMF_Entities_name_4
    imagePropertiesAnnotation_colors_color_score_max_MAX
    NMF_labelAnnotations_description_3 
    labelAnnotations_score_mean_MEAN 
    imagePropertiesAnnotation_colors_color_pixelFraction_min_VAR 
    Sterilized 
    imagePropertiesAnnotation_colors_color_pixelFraction_max_MIN 
    SVD_Description_4 
    imagePropertiesAnnotation_colors_color_pixelFraction_std_MIN 
    labelAnnotations_score_max_MIN 
    labelAnnotations_score_max_MEAN 
    imagePropertiesAnnotation_colors_color_score_std_VAR 
    imagePropertiesAnnotation_colors_color_pixelFraction_min_MIN 
    imagePropertiesAnnotation_colors_color_pixelFraction_mean_VAR 
    SVD_Description_0 
    imagePropertiesAnnotation_colors_color_pixelFraction_std_VAR 
    imagePropertiesAnnotation_colors_color_pixelFraction_mean_MIN 
    imagePropertiesAnnotation_colors_color_score_max_VAR 
    labelAnnotations_score_min_MEAN 
    imagePropertiesAnnotation_colors_color_score_max_MIN 
    NMF_labelAnnotations_description_4 
    SVD_Entities_name_1 
    imagePropertiesAnnotation_colors_color_score_std_MIN 
    labelAnnotations_score_mean_MIN 
    imagePropertiesAnnotation_colors_color_pixelFraction_min_MAX 
    imagePropertiesAnnotation_colors_color_score_min_MAX 
    SVD_Entities_name_0 
    labelAnnotations_score_sum_MEAN 
    imagePropertiesAnnotation_colors_color_pixelFraction_sum_VAR 
