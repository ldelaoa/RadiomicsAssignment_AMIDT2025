def ScreenshotViews(CT,BW_tumor,numimages,step,contourBool,colorbar):
  slice_sums = np.sum(BW_tumor, axis=(1, 2))
  axial_indices = np.where(slice_sums > 0)[0]

  coronal_sums = np.sum(BW_tumor, axis=(0, 2))
  coronal_indices = np.where(coronal_sums > 0)[0]

  sagittal_sums = np.sum(BW_tumor, axis=(0, 1))
  sagittal_indices = np.where(sagittal_sums > 0)[0]
  plt.figure(figsize=(15, 5))
  for i in range(0,numimages,step):

    currAx = axial_indices[i]
    currSag = sagittal_indices[i]
    currCor = coronal_indices[i]
    plt.subplot(131),plt.imshow(CT[currAx,:,:],cmap="gray"),plt.title("Axial"+str(currAx)),plt.axis('off')
    if colorbar: plt.colorbar()
    if contourBool: plt.contour(BW_tumor[currAx,:,:],colors='r')
    plt.subplot(132),plt.imshow(np.flip(CT[:,:,currSag]),cmap="gray"),plt.title("Sagital"+str(currSag)),plt.axis('off')
    if colorbar: plt.colorbar()
    if contourBool: plt.contour(np.flip(BW_tumor[:,:,currSag]),colors='r')
    plt.subplot(133),plt.imshow(np.flip(CT[:,currCor,:]),cmap="gray"),plt.title("Coronal"+str(currCor)),plt.axis('off'),
    if colorbar: plt.colorbar()
    if contourBool: plt.contour(np.flip(BW_tumor[:,currCor,:]),colors='r')
    plt.show(),plt.close(),plt.clf()

  return 0

def cropper(ctSTRUC, CT_c):
    x_non_zero = np.where(~np.all(np.all(ctSTRUC == 0, axis=2), axis=1))[0]
    y_non_zero = np.where(~np.all(np.all(ctSTRUC == 0, axis=2), axis=0))[0]
    z_non_zero = np.where(~np.all(np.all(ctSTRUC == 0, axis=1), axis=0))[0]
    x_min, x_max = x_non_zero.min() - 1, x_non_zero.max() + 2
    y_min, y_max = y_non_zero.min() - 1, y_non_zero.max() + 2
    z_min, z_max = z_non_zero.min() - 1, z_non_zero.max() + 2


    CT_c = CT_c[x_min:x_max, y_min:y_max, z_min:z_max]
    ctSTRUC = ctSTRUC[x_min:x_max, y_min:y_max, z_min:z_max]
    M1 = np.zeros(ctSTRUC.shape)
    M1[ctSTRUC > 0] = 1
    return ctSTRUC, M1, CT_c


def binHU(I, HUstep, Range):
    binI = np.copy(I)
    HUbins = np.arange(Range[0], Range[1] + HUstep, HUstep)
    for b in range(len(HUbins)):
        if b > 0 and b < len(HUbins) - 1:
            binI[(binI >= HUbins[b]) & (binI <= HUbins[b] + HUstep)] = b + 1
        elif b == len(HUbins) - 1:
            binI[binI >= HUbins[b]] = b + 1
    levnum = len(HUbins)
    return binI,levnum
