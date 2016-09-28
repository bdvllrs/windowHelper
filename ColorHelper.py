# coding: utf8

class ColorHelper:
    def __init__(self, c, a = 1):
        if isinstance(c, tuple):
            self.r, self.g, self.b = c
        elif isinstance(c, str):
            (self.r, self.g, self.b) = self.get_colors(c)
        self.a = a
        
    
    def get_rgb(self):
        if self.is_transparent():
            return (self.r, self.g, self.b, self.a)
        return (self.r, self.g, self.b)
        
        
    def get_transparency(self):
        return self.a 
        
    
    def set_transparency(self, val):
        self.a = val
        
        
    def lighten(self, val):
        self.r += val
        self.g += val
        self.b += val
        if self.r > 255:
            self.r = 255
        if self.g > 255:
            self.g = 255
        if self.b > 255:
            self.b = 255
        if self.r < 0:
            self.r = 0
        if self.g < 0:
            self.g = 0
        if self.b < 0:
            self.b = 0
        
        
    def darken(self, val):
        self.lighten(-val)
        
        
    def is_transparent(self):
        if 0 <= self.a < 1:
            return True
        return False
        
        
    def get_colors(self, color):
        colors = {
            "red":(255, 0, 0), 
            "green":(0, 255, 0), 
            "blue":(0,0, 255), 
            "black":(0, 0, 0), 
            "white":(255, 255, 255), 
            "yellow":(255, 255, 0), 
            "cyan":(0, 255, 255), 
            "magenta": (255, 0, 255),
            "darkgrey": (105, 105, 105),
            "grey": (128, 128, 128),
            "dimgrey": (169, 169, 169),
            "silver": (192, 192, 192),
            "lightgrey": (211, 211, 211),
            "gainsboro": (220, 220, 220),
            "whitesmoke": (245, 245, 245),
            "snow": (255, 250, 250),
            "rosybrown":(188, 143, 143),
            "lightcoral":(240, 128, 128),
            "indianred":(205, 92, 92),
            "brown":(165, 42, 42),
            "firebrick":(178, 34, 34),
            "maroon":(128, 0, 0),
            "darkred":(139, 0, 0),
            "mistyrose":(255, 228, 225),
            "salmon":(250, 128, 114),
            "tomato":(255, 999, 71),
            "darksalmon":(233, 150, 122),
            "coral":(255, 127, 80),
            "orangered":(255, 69, 0),
            "lightsalmon":(255, 160, 122),
            "sienna":(160, 82, 45),
            "seashell":(255, 245, 238),
            "chocolate":(210, 105, 30),
            "saddlebrown":(139, 69, 19),
            "sandybrown":(250, 164, 96),
            "peachpuff":(255, 218, 185),
            "peru":(205, 133, 63),
            "lightskyblue": (135, 206, 250),
            "skyblue": (135, 206, 235),
            "darkblue": (0, 0, 139),
            "linen":(250, 240, 230),
            "bisque":(255, 228, 196),
            "darkorange":(255, 140, 0),
            "burlywood":(222, 184, 135),
            "antiquewhite":(250, 235, 215),
            "tan":(210, 180, 140),
            "navajowhite":(255, 222, 173),
            "blanchedalmond":(255, 235, 205),
            "papayawhip":(255, 239, 213),
            "moccasin":(255, 228, 181),
            "orange":(245, 165, 0),
            "wheat":(245, 222, 179),
            "oldlace":(253, 245, 230),
            "floralwhite":(255, 250, 240),
            "darkgoldenrod":(184, 134, 11),
            "goldenrod":(218, 165, 32),
            "cornsilk":(255, 248, 220),
            "gold":(255, 215, 0),
            "lemonchiffon":(255, 250, 205),
            "khaki":(240, 230, 140),
            "palegoldenrod":(238, 232, 170),
            "darkkhaki":(189, 183, 107),
            "ivory":(255, 255, 240),
            "beige":(245, 245, 220),
            "lightyellow":(255, 255, 224),
            "lightgoldenrodyellow":(250, 250, 210),
            "olive":(128, 128, 0),
            "olivedrab":(107, 142, 35),
            "yellowgreen":(154, 205, 50),
            "darkolivegreen":(85, 107, 47),
            "greenyellow":(173, 255, 147),
            "chartreuse":(127, 255, 0),
            "lawngreen":(124, 252, 0),
            "sage":(135, 174, 115)
        }
        return colors[color]
