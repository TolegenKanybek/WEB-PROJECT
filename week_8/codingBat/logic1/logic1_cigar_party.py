def cigar_party(cigars, is_weekend):
  a = range(61)
  if is_weekend and cigars not in a:
    return True
  elif cigars in range(40,61):
    return True
  else:
    return False



cigar_party(30,False)