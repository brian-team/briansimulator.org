from nikola.plugin_categories import ShortcodePlugin

import glob
import os


def file_list(gallery):
    return sorted(glob.glob(os.path.join('files', gallery, '*.html')))


class ExampleGallery(ShortcodePlugin):
    name = "examples"

    def handler(self, gallery_dir, site=None, lang=None, post=None, data=None):
        files = file_list(gallery_dir)
        html_lines = ['<div id="carouselExampleIndicators" class="carousel slide pb-5" data-ride="carousel">']
        html_lines += ['<ol class="carousel-indicators">']
        for i, html in enumerate(files):
            if i == 0:
                html_lines += [f'<li data-target="#carouselExampleIndicators" data-slide-to="{i}" class="active"></li>']
            else:
                html_lines += [f'<li data-target="#carouselExampleIndicators" data-slide-to="{i}"></li>']
        html_lines += ['</ol>']
        html_lines += ['<div class="carousel-inner">']
        for i, html in enumerate(files):
            if i == 0:
                html_lines += ['<div class="carousel-item active">']
            else:
                html_lines += ['<div class="carousel-item">']

            with open(html, 'r') as f:
                html_lines.append(f.read())
            html_lines +=['</div>']
        html_lines += ['</div></div>']
        return '\n'.join(html_lines), files

