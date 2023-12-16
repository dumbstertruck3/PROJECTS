def calculate(list=[0,1,2,3,4,5,6,7,8]):
  npArray = np.array(list)
  npArray = npArray.reshape(3,3)

  #mean
  axis1 = np.mean(npArray, axis=0)
  axis2 = np.mean(npArray, axis=1)
  flattened = np.mean(npArray)

  #variance
  variance1 = np.var(npArray, axis = 0)
  variance2 = np.var(npArray, axis = 1)
  variance_fl = np.var(npArray)

  #standard deviation
  std1 = np.std(npArray, axis=0)
  std2 = np.std(npArray, axis=1)
  std_fl = np.std(npArray)
  
  #min
  min1 = np.min(npArray, axis=0)
  min2 = np.min(npArray, axis=1)
  min_fl = np.min(npArray)

  #max
  max1 = np.max(npArray, axis = 0)
  max2 = np.max(npArray, axis=1)
  max_fl = np.max(npArray)

  #sum
  sum1 = np.sum(npArray, axis= 0)
  sum2 = np.sum(npArray, axis= 1)
  sum_fl = np.sum(npArray)

  calculations = {'mean': [axis1,axis2,flattened],
                  'variance': [variance1, variance2, variance_fl],
                  'standard deviation': [std1, std2, std_fl],
                  'max': [max1, max2, max_fl],
                  'min': [min1, min2, min_fl],
                  'sum': [sum1, sum2, sum_fl]
                  }
  return calculations
calculate()