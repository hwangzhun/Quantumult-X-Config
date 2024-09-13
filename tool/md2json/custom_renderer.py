# custom_renderer.py
import mistune

class CustomRenderer(mistune.HTMLRenderer):
    def render_table(self, header, body):
        return f'<table><thead>{header}</thead><tbody>{body}</tbody></table>'

    def render_heading(self, text, level):
        return f'<h{level}>{text}</h{level}>'
