import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage import img_as_ubyte
from skimage.transform import resize
import warnings
from demo import load_checkpoints, make_animation

warnings.filterwarnings("ignore")

generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml',
                                          checkpoint_path='data/vox-cpk.pth.tar', cpu=True)


def deepfake(imgpath, vidpath, outpath):
    source_image = imageio.imread(imgpath)
    #driving_video = imageio.mimread('/content/gdrive/My Drive/first-order-motion-model/test.mp4')

    reader = imageio.get_reader(vidpath)
    driving_video = []
    try:
        for im in reader:
            driving_video.append(im)
    except RuntimeError:
        print('runtime error')

    print('img&vid loaded')

    #Resize image and video to 256x256

    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True, cpu=True)

    imageio.mimsave(outpath, [img_as_ubyte(frame) for frame in predictions])

