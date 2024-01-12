## Python Image Tagging Widget

Messing around with a personal project for boot.dev. Partially reviving/modifying my photo-tagging webapp in the aranaris/photo-tagging repo using tkinter in python.

### Getting initial set of images

I'm using Google's Open Images dataset as an initial set of images to load and experiment with. There's a [colab tutorial](https://colab.research.google.com/github/voxel51/fiftyone/blob/v0.9.1/docs/source/tutorials/open_images.ipynb#scrollTo=Nr1Fq8PPh95d) provided, but for this project, i'm mostly interested in just retrieving images and displaying the tags provided from the dataset using the FiftyOne python package.

cmd-line setup:

> pip install fiftyone

> fiftyone config

I did this in Google's Colab, and you can download the output afterwards yourself. The images are outputted directly to /validation/data/

```python
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "open-images-v6",
    split="validation",
    max_samples=100,
    seed=51,
    shuffle=True,
)
```

I currently have the above sample set of 100 images stored in a public github repo that I can access by their image id `https://aranaris.github.io/image-repo/$IMAGE_ID.jpg`

