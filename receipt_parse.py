import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "029a9e1b314848d98d5953e9142c750c"
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
'''class parse:
    image_url = ""

    def __init__(self, url):
        image_url = url
'''
#if __name__ == "__main__":
#    getCloudJSON("https://support.checkout51.com/hc/en-us/article_attachments/200464383/receipt_examples_perfect_sm.jpg")


def getCloudJSON(receipt):
    vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/"

    ocr_url = vision_base_url + "ocr"

        # Set image_url to the URL of an image that you want to analyze.
    image_url = receipt;

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params  = {'language': 'unk', 'detectOrientation': 'true'}
    data    = {'url': image_url}
    response = requests.post(ocr_url, headers=headers, params=params, json=data)
    response.raise_for_status()

    print(response.json())
    # print(analysis)

    # # Extract the word bounding boxes and text.
    # line_infos = [region["lines"] for region in analysis["regions"]]
    # word_infos = []
    # for line in line_infos:
    #     for word_metadata in line:
    #         for word_info in word_metadata["words"]:
    #             word_infos.append(word_info)
    # word_infos
    #
    # # Display the image and overlay it with the extracted text.
    # plt.figure(figsize=(5, 5))
    # image = Image.open(BytesIO(requests.get(image_url).content))
    # ax = plt.imshow(image, alpha=0.5)
    # for word in word_infos:
    #     bbox = [int(num) for num in word["boundingBox"].split(",")]
    #     text = word["text"]
    #     origin = (bbox[0], bbox[1])
    #     patch  = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='y')
    #     ax.axes.add_patch(patch)
    #     plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
    # plt.axis("off")
