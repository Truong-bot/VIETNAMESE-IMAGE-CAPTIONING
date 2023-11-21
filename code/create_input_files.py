from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr30k',
                       karpathy_json_path='D:\code\Luan_van\image_caption\data_split\\vietnamese\dataset_flickr30k_vi_preview_wbw.json',
                       image_folder='D:\code\Luan_van\\flickr30k_images\\flickr30k_images\\flickr30k_images',
                       captions_per_image=5,
                       min_word_freq=3,
                       output_folder='D:\code\Luan_van\seminar',
                       max_len=50)
