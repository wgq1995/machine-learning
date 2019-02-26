import pandas as pd
import numpy as np
import json
import os
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import SparsePCA, TruncatedSVD, LatentDirichletAllocation, NMF


def get_rescuer_feature(df):
    rg = df['RescuerID'].value_counts()
    df['RescuerID'] = df['RescuerID'].apply(lambda x: rg[x])
    return df

feature_list = [
    'pet_id',
    'documentSentiment_magnitude',
    'documentSentiment_score',
]
statistics_features = [
    'Sentences_text_sentiment_magnitude_',
    'Sentences_text_sentiment_score_',
    'Entities_other_salience_'
]
statistics_functions = [
    ['max', np.max],
    ['min', np.min],
    ['mean', np.mean],
    ['std', np.std]
]
feature_list = feature_list + [statistics_feature + statistics_function[0] for statistics_feature in statistics_features for statistics_function in statistics_functions]
# feature_list.append('Entities_location_salience')
feature_list.append('Entities_name')
print(feature_list)

def get_agg_result(data, functions_list):
    res = []
    if len(data) == 0:
        return [None] * 4
    else:
        for i, f in enumerate(functions_list):
            res.append(f(data))
        return res
    
def get_sentiment_feature(sentiment_path):
    pet_id = sentiment_path.split('/')[-1][:-5]
    with open(sentiment_path) as f:
        sentiment_dic = json.load(f)
    feature_list = [pet_id]
    # get documentSentiment feature
    feature_list.extend([sentiment_dic['documentSentiment']['magnitude'], sentiment_dic['documentSentiment']['score']])
    
    # get sentences feature
    sentences_function = [np.max, np.min, np.mean, np.std]
    sentences_magnitude_list = []
    sentences_score_list = []
    for sentences_dic in sentiment_dic['sentences']:
        sentences_magnitude_list.append(sentences_dic['sentiment']['magnitude'])
        sentences_score_list.append(sentences_dic['sentiment']['score'])
    feature_list.extend(get_agg_result(sentences_magnitude_list, sentences_function))
    feature_list.extend(get_agg_result(sentences_score_list, sentences_function))
    
    # get entities feature
    entities_function = [np.max, np.min, np.mean, np.std]
    entities_list = []
    entities_name_str = []
    for entities_dic in sentiment_dic['entities']:
        entities_list.append(entities_dic['salience'])
        entities_name_str.append(entities_dic['name'])
    entities_name_str = ' '.join(entities_name_str)
    feature_list.extend(get_agg_result(entities_list, entities_function))
    feature_list.append(entities_name_str)
    return feature_list

def getFileDir(path):
    list_name=[]
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            getFileDir(file_path, list_name)
        else:
            if file != '.DS_Store' :# .DS_Store这个文件是系统默认文件
                list_name.append(file_path)
    return list_name
sentiment_data_root = './data/train_sentiment/'
meta_data_root = './data/train_metadata/'
sentiment_data_paths = getFileDir(sentiment_data_root)
meta_data_paths = getFileDir(meta_data_root)

data = []
time1 = time.clock()
for path in sentiment_data_paths:
    data.append(get_sentiment_feature(path))
data = np.asarray(data)
sentiment_df = pd.DataFrame(data, columns=feature_list)
print(time.clock() - time1)

meta_feature_list = [
    'pet_id',
    'imagePropertiesAnnotation_colors_color_score_max',
    'imagePropertiesAnnotation_colors_color_score_min',
    'imagePropertiesAnnotation_colors_color_score_mean',
    'imagePropertiesAnnotation_colors_color_score_std',
    'imagePropertiesAnnotation_colors_color_pixelFraction_max',
    'imagePropertiesAnnotation_colors_color_pixelFraction_min',
    'imagePropertiesAnnotation_colors_color_pixelFraction_mean',
    'imagePropertiesAnnotation_colors_color_pixelFraction_std',
    'cropHintsAnnotation_cropHints_confidence',
    'cropHintsAnnotation_cropHints_importanceFraction',
    'labelAnnotations_score_max',
    'labelAnnotations_score_min',
    'labelAnnotations_score_mean',
    'labelAnnotations_score_std',
    'labelAnnotations_topicality_max',
    'labelAnnotations_topicality_min',
    'labelAnnotations_topicality_mean',
    'labelAnnotations_topicality_std',
    'labelAnnotations_description'
]
len(meta_feature_list)

def get_meta_feature(meta_path):
    pet_id = meta_path.split('/')[-1][:-5]
    with open(meta_path) as f:
        meta_dic = json.load(f)
    feature_list = [pet_id]
    # get imagePropertiesAnnotation feature:
    imagePropertiesAnnotation_function = [np.max, np.min, np.mean, np.std]
    imagePropertiesAnnotation_score_list = []
    imagePropertiesAnnotation_pixelFraction_list = []
    for color_dic in meta_dic['imagePropertiesAnnotation']['dominantColors']['colors']:
        imagePropertiesAnnotation_score_list.append(color_dic['score'])
        imagePropertiesAnnotation_pixelFraction_list.append(color_dic['pixelFraction'])
    imagePropertiesAnnotation_function = [np.max, np.min, np.mean, np.std]
    feature_list.extend(get_agg_result(imagePropertiesAnnotation_score_list, imagePropertiesAnnotation_function))
    feature_list.extend(get_agg_result(imagePropertiesAnnotation_pixelFraction_list, imagePropertiesAnnotation_function))
    
    # get cropHintsAnnotation feature
    feature_list.append(meta_dic['cropHintsAnnotation']['cropHints'][0].get('confidence'))
    feature_list.append(meta_dic['cropHintsAnnotation']['cropHints'][0].get('importanceFraction'))
    
    # get labelAnnotations feature
    label_function = [np.max, np.min, np.mean, np.std]
    label_score_list = []
    label_topicality_list = []
    label_description_list= []
    try:
        for label_dic in meta_dic['labelAnnotations']:
            label_score_list.append(label_dic['score'])
            label_topicality_list.append(label_dic['topicality'])
            label_description_list.append(label_dic['description'])
        feature_list.extend(get_agg_result(label_score_list, label_function))
        feature_list.extend(get_agg_result(label_topicality_list, label_function))
        feature_list.append(' '.join(label_description_list))
    except KeyError:
        feature_list.extend([None]*(2*len(label_function)))
        feature_list.append(' ')
    return feature_list

meta_data = []
time1 = time.clock()
for path in meta_data_paths:
    meta_data.append(get_meta_feature(path))
meta_data = np.asarray(meta_data)
meta_df = pd.DataFrame(meta_data, columns=meta_feature_list)
print('use time {}'.format(time.clock() - time1))

def get_svd_nmf_feature(text_df, n_components = 5):
    text_df_features = []
    for i in text_df.columns:
        svd_ = TruncatedSVD(n_components=n_components, random_state=1337)
        nmf_ = NMF(n_components=n_components, random_state=1337)

        tfidf_col = TfidfVectorizer().fit_transform(text_df.loc[:, i].values)
        svd_col = svd_.fit_transform(tfidf_col)
        svd_col = pd.DataFrame(svd_col)
        svd_col = svd_col.add_prefix('SVD_{}_'.format(i))

        nmf_col = nmf_.fit_transform(tfidf_col)
        nmf_col = pd.DataFrame(nmf_col)
        nmf_col = nmf_col.add_prefix('NMF_{}_'.format(i))
        text_df_features.append(svd_col)
        text_df_features.append(nmf_col)
    text_df_features = pd.concat(text_df_features, axis=1)
    return text_df_features
len(get_svd_nmf_feature(meta_df[['labelAnnotations_description', 'pet_id']]))
