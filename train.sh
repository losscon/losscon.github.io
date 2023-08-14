#!/bin/bash
#CUDA_VISIBLE_DEVICES=1 
python run_classifier.py --task_name=mydata --do_train=true --do_eval=true --data_dir=/home/sll/bert_classify/shujvji/ --vocab_file=/home/sll/bert_classify/mode/vocab.txt --bert_config_file=/home/sll/bert_classify/mode/bert_config.json --init_checkpoint=/home/sll/bert_classify/mode/bert_model.ckpt --max_seq_length=128 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=30 --output_dir=/home/sll/bert_classify/output/