from smoothing import *
from copy import copy

def smooth_template(lc,  smooth=False, image=False, differenced=False, **kwargs):
	'''Plot a pixel lc as either a set of light curves or an image
	in which rows represent light curves

	args:
	ax - matplotlib Axes object to plot to
	lc - NxM numpy array of light curves
	smooth - Bool or int of boxcar smoothing window over which to smooth the light curve
	image - Bool, whether to plot individual light curves or make an image plot
	differenced - Bool, whether to difference the rows of the light curve
	cmap - matplotlib color map to apply to the image
	'''

	# create the image from the rows of the light curve
	image_ = np.copy(lc[::]) if not differenced else lc[:, 1:] - lc[:, :-1]
	
	# whiten the light curve
	image_[::] -= np.nanmedian(image_, axis=0)
	image_[::] /= np.nanstd(image_, axis=0)

	# optionally smooth the light curve
	if smooth:
		N = 30 if smooth is True else smooth
		image_[::] = running_median(image_, N, axis=0)
	return image_
	#if image:
	#	return ax.imshow(image_.T[::-1], **kwargs)
	
	#return [ax.plot(line, **kwargs) for line in image_.T] 