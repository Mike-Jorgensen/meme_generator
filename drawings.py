
import PIL.Image
import os
import PIL.ImageFont
import PIL.ImageDraw
import textwrap

def draw_border(image, border_size, border_color):
        original_width, original_height = image.size
        width = original_width + border_size * 2
        height = original_height + border_size * 2
        border_canvas = PIL.Image.new('RGB', (width, height), border_color)
        border_canvas.paste(image, (border_size, border_size))
        return border_canvas

def draw_text(image, text, text_color, text_size):
        font = get_font(size=text_size)
        draw_canvas = PIL.ImageDraw.Draw(image)
        text_width, text_height = draw_canvas.textsize(text, font=font)
        image_width = image.size[0]
        if text_width > image_width:
                character_width = text_width / len(text)
                max_character_count = int( image_width / character_width)
                text_lines = wrap_text(text, wrap_width=max_character_count)
        else:
                text_lines = [text]

        for row, line in enumerate(text_lines):
                draw_canvas.text((0, row * text_height), line, fill=text_color, font=font)
        return image

def get_text_as_image(text, text_color, text_size, image_width, background_color):
        placeholder = PIL.Image.new('RGB', (0,0), background_color)
        font = get_font(size=text_size)
        draw_canvas = PIL.ImageDraw.Draw(placeholder)
        text_width, text_height = draw_canvas.textsize(text, font=font)
        if text_width > image_width:
                character_width = text_width / len(text)
                max_characters_count = int(image_width / character_width)
                text_lines = wrap_text(text, wrap_width=max_characters_count)
        else:
                text_lines = [text]

        total_text_height = len(text_lines) * text_height
        image = PIL.Image.new('RGB', (image_width, total_text_height), background_color)
        draw_canvas = PIL.ImageDraw.Draw(image)

        for row, line in enumerate(text_lines):
                row_height = row * text_height
                line_width, _ = draw_canvas.textsize(line, font=font)
                left = (image_width - line_width) / 2
                draw_canvas.text((left, row_height), line, fill=text_color, font=font)
        return image

def bottom_expand_image_with_image(image, expand_image, background_color):
        width = image.size[0]
        height = image.size[1] + expand_image.size[1]
        expand_canvas = PIL.Image.new('RGB', (width, height), background_color)
        expand_canvas.paste(image, (0,0))
        expand_canvas.paste(expand_image, (0, image.size[1]))
        return expand_canvas

def wrap_text(text, wrap_width):
        wrapper = textwrap.TextWrapper(width=wrap_width)
        return wrapper.wrap(text)

def get_font(size):
        path = os.path.join('./Roboto-Regular.ttf') #set this path to font file
        return PIL.ImageFont.truetype(path, size=size)