import cv2
import numpy as np
import os
import sys

def return_resized_img(img, target_dim, resize_option, resize_unit, pad_color):
    target_dim = np.flip(np.array(target_dim),0)
    input_dim = np.array(img.shape[:2]).astype(int)
    center_pixel = (0.5*input_dim).astype(int)
    input_ratio = input_dim/input_dim[0]
    output_ratio = target_dim/target_dim[0] # compute aspect ratio based on width (width is always 1)

    if output_ratio[1]>input_ratio[1]:
        # normed output width greater than input width
        if resize_option is 'pad':
            # --> hold height constant & increase width to match output ratio
            output_dim = np.ceil(np.array([input_dim[0],input_dim[0]*output_ratio[1]])).astype(int)
            start_pix = int((output_dim[1]-input_dim[1])/2)
            output_img = pad_color*np.ones((output_dim[0],output_dim[1],3))
            output_img[:,start_pix:start_pix+input_dim[1],:] = img
        elif resize_option is 'crop':
            # --> hold width constant & decrease height to match output ratio
            output_dim = np.ceil(np.array([input_dim[1]/output_ratio[1],input_dim[1]])).astype(int)
            start_pix = int((input_dim[0]-output_dim[0])/2)
            output_img = img[start_pix:start_pix+output_dim[0],:,:]
    else:
        # normed output width less than input width
        if resize_option is 'pad':
            # --> hold width constant & increase height to match output ratio
            output_dim = np.ceil(np.array([input_dim[1]/output_ratio[1],input_dim[1]])).astype(int)
            start_pix = int((output_dim[0]-input_dim[0])/2)
            output_img = pad_color*np.ones((output_dim[0],output_dim[1],3))
            output_img[start_pix:start_pix+input_dim[0],:,:] = img
        elif resize_option is 'crop':
            # --> hold height constant & decrease width to match output ratio
            output_dim = np.ceil(np.array([input_dim[0],input_dim[0]*output_ratio[1]])).astype(int)
            start_pix = int((input_dim[1]-output_dim[1])/2)
            output_img = img[:,start_pix:start_pix+output_dim[1],:]

    if resize_unit is 'aspect':
        return output_img.astype('uint8')
    elif resize_unit is 'pixel':
        return cv2.resize(output_img, dsize=(target_dim[1],target_dim[0])).astype('uint8')

def is_an_image(img_name, image_types=['.png', '.jpg']):
    is_image = False
    for t in image_types:
        if t in img_name.lower():
            is_image = True
    return is_image

def thumbnail_everything(img_folder, target_dim, resize_option, resize_unit, pad_color, image_types, always_overwrite):
    # make output folder
    output_folder = img_folder+'/thumbnail/'
    if not os.path.isdir(output_folder):
        print('Making output folder:',output_folder)
        os.mkdir(output_folder)

    # grab all image files in folder
    images = [im for im in os.listdir(img_folder) if is_an_image(im, image_types)]
    for img in images:
        # convert
        tn_img = output_folder+img
        if always_overwrite or ~os.path.isfile(tn_img):
            print(tn_img)
            img_mat = cv2.imread(img_folder+img)
            output_img = return_resized_img(img_mat, target_dim, resize_option, resize_unit, pad_color)
            cv2.imwrite(tn_img, output_img)

# def main():
#     import argparse
#     parser = argparse.ArgumentParser(description='Convert all images within a folder to image of a particular size or aspect ratio. Useful for batch making thumbnails from original images.')
#     parser.add_argument('--img_folder', help='Directory (full path) for where the images are gathered and resized.', required=True)
#     parser.add_argument('--resize_option', help='pad/crop. Pad or crop original photo for resizing. (default=\'pad\')', default='pad')
#     parser.add_argument('--resize_unit', help='pixel/aspect. Resize dimension in pixels or aspect ratio. (default=\'pixel\')', default='pixel')
#     parser.add_argument('--target_W', help='Width of resized photo, can be int or float. (default=300)', default=300)
#     parser.add_argument('--target_H', help='Height of resized photo, can be int or float. (default=300)', default=300)
#     parser.add_argument('--always_overwrite', help='Whether to always overwrite existing resized images. (default=True)', default=True)
#     args = parser.parse_args()
#     image_types = ['.jpg', '.png', '.tif', '.gif']
#     print(args.img_folder)
#     thumbnail_everything(args.img_folder, [float(args.target_W), float(args.target_H)], args.resize_option, args.resize_unit, image_types, args.always_overwrite)
#
# if __name__ =="__main__":
#     main()
