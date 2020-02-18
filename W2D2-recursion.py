sample = [1, 4, 3, 3, 4, 6, 7]

def recurse_search(arr, target):
  if len(arr) == 0:
    print('false')
    return False
  if arr[0] == target:
    print('true')
    return True
  return recurse_search(arr[1:], target)

recurse_search(sample, 8)