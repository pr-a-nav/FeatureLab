from sklearn.preprocessing import Normalizer


class Normalizer:
  
  def __init__(self, data ) :
    transformer = Normalizer().fit(data)
    return transformer

  
  
