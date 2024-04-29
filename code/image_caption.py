import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to("cuda")

translation_pipeline = pipeline(task=Tasks.translation, model="damo/nlp_csanmt_translation_en2zh_base")

def generate_caption(image_path):
    """
    Generate a caption for an image given its local path.

    Args:
        image_path (str): The local path to the image file.

    Returns:
        str: The generated caption for the image.
    """
    raw_image = Image.open(image_path).convert('RGB')

    inputs = processor(raw_image, return_tensors="pt").to("cuda")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    return caption

def translate_text(input_sequence):
    """
    Translate English text to Chinese.

    Args:
        input_sequence (str): The English text to be translated.

    Returns:
        str: The translated Chinese text.
    """
    outputs = translation_pipeline(input=input_sequence)
    
    return outputs['translation']


if __name__ == '__main__':
    # test
    image_path = '../data/test_image.jpg' 
    caption = generate_caption(image_path)
    print(caption)

    english_text = caption
    chinese_translation = translate_text(english_text)
    print(chinese_translation)
