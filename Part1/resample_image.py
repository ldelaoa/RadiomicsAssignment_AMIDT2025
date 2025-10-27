def resample_image(image,interpolator=sitk.sitkNearestNeighbor, new_spacing=[1, 1, 1]):

  original_spacing = image.GetSpacing()
  original_size = image.GetSize()

  new_size = [
      int(round(original_size[0] * (original_spacing[0] / new_spacing[0]))),
      int(round(original_size[1] * (original_spacing[1] / new_spacing[1]))),
      int(round(original_size[2] * (original_spacing[2] / new_spacing[2]))),
  ]

  resample = sitk.ResampleImageFilter()
  resample.SetInterpolator(interpolator)
  resample.SetOutputSpacing(new_spacing)
  resample.SetSize(new_size)
  resample.SetOutputDirection(image.GetDirection())
  resample.SetOutputOrigin(image.GetOrigin())
  #resample.SetDefaultPixelValue(image.GetPixelIDValue())

  return resample.Execute(image)
