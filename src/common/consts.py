CLASSES_COUNT = 120
INCEPTION_CLASSES_COUNT = 2048
INCEPTION_OUTPUT_FIELD = 'inception_output'
LABEL_ONE_HOT_FIELD = 'label_one_hot'
IMAGE_RAW_FIELD = 'image_raw'
INCEPTION_INPUT_TENSOR = 'DecodeJpeg/contents:0'
INCEPTION_OUTPUT_TENSOR = 'pool_3:0'
OUTPUT_NODE_NAME = 'output_node'
OUTPUT_TENSOR_NAME = OUTPUT_NODE_NAME + ':0'
HEAD_INPUT_NODE_NAME = 'x'
HEAD_INPUT_TENSOR_NAME = HEAD_INPUT_NODE_NAME + ':0'

DEV_SET_SIZE = 3000
TRAIN_SAMPLE_SIZE = 3000

# name of the model being referenced by all other scripts
# CURRENT_MODEL_NAME = 'test_v1.0'
CURRENT_MODEL_NAME = 'Pic-a-Breed_v1.0'
# sets up number of layers and number of units in each layer for
# the "head" dense neural network stacked on top of the Inception
# pre-trained model.

#INCEPTION_CLASSES_COUNT=2048
#CLASSES_COUNT=120
HEAD_MODEL_LAYERS = [INCEPTION_CLASSES_COUNT, 1024, CLASSES_COUNT]