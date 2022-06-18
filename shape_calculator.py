class Rectangle:
  def __init__(self, width, height):
    '''
    Initializes the rectangle
    
    Parameters
    ----------
      width : float
        shape width
      height : float
        shape height
    
    Returns
    -------
    None
    '''
    self.width = width
    self.height = height

  
  def __repr__(self):
    '''
    Printable representation of the object
    
    Returns
    -------
    str
      
    '''
    return f'Rectangle(width={self.width}, height={self.height})'

  
  def set_width(self, nw):
    '''
    Updates the width
    
    Parameters
    ----------
      nw : float
        New width
    
    Returns
    -------
    None
    '''
    self.width = nw

  def set_height(self, nh):
    '''
    Updates the height
    
    Parameters
    ----------
      nh : float
        New height
    
    Returns
    -------
    None
    '''
    self.height = nh

  def get_area(self):
    '''
    Calculates rectange area
    
    Returns
    -------
    float
      Rectange Area
    '''
    return self.width * self.height

  
  def get_perimeter(self):
    '''
    Calculates rectange perimeter
    
    Returns
    -------
    float
      Rectange perimeter
    '''
    return 2 * (self.width + self.height)

  
  def get_diagonal(self):
    '''
    Calculates the rectange diagonal
    
    Returns
    -------
    float
      Rectange Diagonal Length 
    '''
    return (self.width ** 2 + self.height ** 2) ** 0.5

  
  def get_picture(self):
    '''
    Prints the rectange as a string
    
    Returns
    -------
    str
      Rectange image
    '''
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      pic = '*' * self.width + '\n'
      pic = pic * self.height
      return pic

      
  def get_amount_inside(self, obj):
    '''
    Determines the full number of a given polygon that could fit inside
    the rectange
    
    Returns
    -------
    float
      Rectange Area
    '''
    return self.get_area() // obj.get_area() 
    

class Square(Rectangle):
    def __init__(self, s):
      '''
      Initializes the square using the rectange parent class
      
      Parameters
      ----------
        s : float
          square side length 
      
      Returns
      -------
      None
      '''
      super().__init__(s, s)

    def __repr__(self):
      '''
      Returns printable representation of the square

      Returns
      -------
      str
      '''
      return f'Square(side={self.width})'

    def set_side(self, ns):
      '''
      Updates the square side
      
      Parameters
      ----------
        ns : float
          snew side length 
      
      Returns
      -------
      None
      '''
      self.width = ns
      self.height = ns
