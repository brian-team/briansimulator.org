from nikola.plugin_categories import ShortcodePlugin

import glob
import os


def image_list(gallery):
    img_meta = []
    for img in glob.glob(os.path.join('galleries', gallery) + '/*.png'):
        fname, ext = os.path.splitext(img)
        img_meta.append((fname + '.png', fname + '.meta'))
    return sorted(img_meta)


class ExampleGallery(ShortcodePlugin):
    name = "examples"

    def handler(self, gallery_dir, site=None, lang=None, post=None, data=None):
        # raise Exception(f'gallery_dir: {gallery_dir}')
        html_lines = ['<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">']
        html_lines += ['<div class="carousel-inner">']
        for i, (img, meta) in enumerate(image_list(gallery_dir)):
            if i == 0:
                html_lines += ['<div class="carousel-item active">']
            else:
                html_lines += ['<div class="carousel-item">']
            # First line is title, second line is description
            with open(meta, 'r') as f:
                lines = f.readlines()
                html_lines += [f'<a href="{lines[1]}"<h4>{lines[0]}</h4></a>']
                html_lines += [f'<p>{lines[2]}</p>']
            html_lines += [f'<img class="d-block" src="{img}" style="max-height: 20rem; margin-left: auto; margin-right: auto;">']
            html_lines +=['</div>']
        html_lines.extend(['</div>',
                           '</div>',
                           '<a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">',
                           '<span class="carousel-control-prev-icon" aria-hidden="true"></span>',
                           '<span class="sr-only">Previous</span>',
                           '</a>',
                           '<a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">',
                           '<span class="carousel-control-next-icon" aria-hidden="true"></span>',
                           '<span class="sr-only">Next</span>',
                           '</a>',
                           '</div>'])
        return '\n'.join(html_lines), []

