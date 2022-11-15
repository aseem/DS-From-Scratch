class Vector:
  def __init__(self, input = []):
    print("init!")
    self._vector = input

  def __repr__(self):
    return ' '.join(str(e) for e in self._vector)

  def __add__(self, other):
    """Adds the corresponding elements of each vector."""
    assert(len(self._vector) == len(other._vector))
    total = [x_i + y_i for x_i, y_i in zip(self._vector, other._vector)]
    return Vector(total)

  def __sub__(self, other):
    """Subtracts the corresponding elements of each vector"""
    assert(len(self._vector) == len(other._vector))
    return self + other.scale(-1)

  def scale(self, factor):
    """Multiplies the vector by scalar"""
    scaled_vector = [x * factor for x in self._vector]
    return Vector(scaled_vector)

  @classmethod 
  def vector_sum(cls, vectors):
    """Sum a list of vectors"""
    total = [0]*len(vectors[0]._vector)
    for v in vectors:
      total = [t_i + x_i for t_i, x_i in zip(total, v._vector)]
    return cls(total)

  