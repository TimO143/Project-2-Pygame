from Values import *

class Functions():
    def text_objects(self,text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def button(self,msg, msgcolor, x, y, width, height, inactive_color, active_color):
        mouse_pos = py.mouse.get_pos()
        button = py.draw.rect(display_screen, active_color, (x, y, width, height))

        text_surface, text_rect = self.text_objects(msg, small_text, msgcolor)
        text_rect.center = (x + width / 2, y + height / 2)

        if (button.collidepoint(mouse_pos)):
            button = py.draw.rect(display_screen, inactive_color, (x, y, width, height))
            text_surface, text_rect = self.text_objects(msg, small_text_highlight, msgcolor)
            text_rect.center = (x + width / 2, y + height / 2)

        display_screen.blit(text_surface, text_rect)

        return button
