def is_valid_hex_color(color):
    if len(color) != 7 or color[0] != "#":
        return False
    
    hex_part = color[1:]
    
    for char in hex_part:
        if not (char.isdigit() or char.lower() in "abcdef"):
            return False
    
    return True
color = input("please type your hex color:")
print(is_valid_hex_color(color))