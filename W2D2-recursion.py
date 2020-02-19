sample = []

def recurse_search(arr, target):
  if len(arr) == 0:
    return False
  if arr[0] == target:
    return True
  return recurse_search(arr[1:], target)

print(recurse_search(sample, 3))