
import PIL.Image

def draw_border(image, border_size, border_color):
        original_width, original_height = image.size
        width = original_width + border_size * 2
        height = original_height + border_size * 2
        border_canvas = PIL.Image.new('RGB', (width, height), border_color)
        border_canvas.paste(image, (border_size, border_size))
        return border_canvas