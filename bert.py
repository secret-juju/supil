import keras as keras
from keras_radam import RAdam
from keras_bert import Tokenizer

def get_bert_finetuning_model(model):
    inputs = model.inputs[:2]
    dense = model.layers[-3].output


    outputs = keras.layers.Dense(1, activation='sigmoid',kernel_initializer=keras.initializers.TruncatedNormal(stddev=0.02),
                                 name = 'real_output')(dense)



    bert_model = keras.models.Model(inputs, outputs)
    bert_model.compile(
        optimizer=RAdam(learning_rate=0.00001, weight_decay=0.0025),
        loss='binary_crossentropy',
        metrics=['accuracy'])

    return bert_model

class inherit_Tokenizer(Tokenizer):
    def _tokenize(self, text):
        if not self._cased:
            text = text

            text = text.lower()
        spaced = ''
        for ch in text:
            if self._is_punctuation(ch) or self._is_cjk_character(ch):
                spaced += ' ' + ch + ' '
            elif self._is_space(ch):
                spaced += ' '
            elif ord(ch) == 0 or ord(ch) == 0xfffd or self._is_control(ch):
                continue
            else:
                spaced += ch
        tokens = []
        for word in spaced.strip().split():
            tokens += self._word_piece_tokenize(word)
        return tokens

