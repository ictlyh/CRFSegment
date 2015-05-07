#! /bin/sh
python make_crf_train_data.py ./icwb2-data/training/msr_training.utf8 tmp.data && ./CRF/crf_learn -f 3 -c 4.0 ./CRF/example/seg/template tmp.data model && python crf_segmenter.py model ./icwb2-data/testing/msr_test.utf8 crf_4tag_result.utf8
