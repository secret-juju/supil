import numpy as np
SEQ_LEN = 128

def sentence_convert_data(data, tokenizer):
    indices = []
    ids, segments = tokenizer.encode(data, max_len = SEQ_LEN)
    indices.append(ids)

    items = indices
    indices = np.array(indices)
    return [indices, np.zeros_like(indices)]

def evaluation_predict(sentence, bert_model, tokenizer):
    data_x = sentence_convert_data(sentence, tokenizer)
    predict = bert_model.predict(data_x)
    predict_answer = np.round(np.ravel(predict), 0).item()

    return predict_answer

def eval_ratio(contents, bert_model, tokenizer):
    p = 0
    n = 0
    for content in contents.split('\n'):
        eval = evaluation_predict(content, bert_model, tokenizer)
        if eval == 1:
            p+=1
        elif eval == 0:
            n+=1

    return int(p/(p+n)*100)