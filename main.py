from keras_bert import load_trained_model_from_checkpoint
from bert import get_bert_finetuning_model, inherit_Tokenizer
from eval import eval_ratio
from extract import extract_data
from db import *
import codecs

SEQ_LEN = 128
BATCH_SIZE = 16
EPOCHS=2
LR=1e-5

config_path = 'model/bert/bert_config.json'
checkpoint_path = 'model/bert/bert_model.ckpt'
vocab_path = 'model/bert/vocab.txt'

DATA_COLUMN = "document"
LABEL_COLUMN = "label"

token_dict = {}
with codecs.open(vocab_path, 'r', 'utf8') as reader:
    for line in reader:
        token = line.strip()
        if "_" in token:
            token = token.replace("_","")
            token = "##" + token
        token_dict[token] = len(token_dict)

tokenizer = inherit_Tokenizer(token_dict)

layer_num = 12
model = load_trained_model_from_checkpoint(
    config_path,
    checkpoint_path,
    training=True,
    trainable=True,
    seq_len=SEQ_LEN,)

bert_model = get_bert_finetuning_model(model)
bert_model.load_weights('model/bert.h5')

contents = call_content()

for content in contents:
    df = extract_data(content[1])
    ratio = eval_ratio(content[1], bert_model, tokenizer)
    delete_org_content(content[0])

    for idx, data in df.iterrows():
        print(data['단축코드'], data['한글 종목약명'], data['업종'])
        insert_company(data['단축코드'], data['한글 종목약명'])
        insert_positivity(ratio, content[1], data['단축코드'])
        insert_industry(data['업종'])
        insert_company_industry_id(data['단축코드'], data['업종'])
