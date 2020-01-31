import io
import os
import urllib.parse

from nikola.plugins.compile.ipynb import CompileIPynb as _CompileIPynb
from nikola.utils import makedirs


HEADER = '''
    <div class="alert alert-primary notebook-header" role="alert">
    <p>
    This article is written as a <a href="https://jupyter.org">Jupyter notebook</a> which you can execute and modify interactively.
    You can either download it via the "Source" link on the top right, or run it directly in the browser on the
    <a href="https://mybinder.org">mybinder</a> infrastructure: <a href="https://mybinder.org/v2/gh/brian-team/briansimulator.org/master?filepath={fname}">
    <img src="https://static.mybinder.org/badge_logo.svg" alt="Launch binder" class="d-inline-block"></a>
    </p>
    <p><strong>For more information, see our general <a href="/posts/2020/notes-notebooks/">Notes on Notebooks</a>.</strong></p>
    </div>
'''


class CompileIPynbWithHeader(_CompileIPynb):
    """Compile IPynb into HTML."""

    name = "ipynb_with_header"
    friendly_name = "Jupyter Notebook with header"
    demote_headers = True
    default_kernel = 'python3'
    supports_metadata = True


    # Overwriting compile_string would be enough, but we have to work around
    # Nikola's wrong call of compile_string (see #3343)
    def compile(self, source, dest, is_two_file=False, post=None, lang=None):
        """Compile the source file into HTML and save as dest."""
        makedirs(os.path.dirname(dest))
        with io.open(dest, "w+", encoding="utf8") as out_file:
            with io.open(source, "r", encoding="utf8") as in_file:
                nb_str = in_file.read()
            output, shortcode_deps = self.compile_string(nb_str, source,
                                                         is_two_file, post, lang)
            out_file.write(output)
        if post is None:
            if shortcode_deps:
                self.logger.error(
                    "Cannot save dependencies for post {0} (post unknown)",
                    source)
        else:
            post._depfile[dest] += shortcode_deps

    def compile_string(self, data, source_path=None, is_two_file=True,
                       post=None, lang=None):
        html, deps = super(CompileIPynbWithHeader, self).compile_string(data,
                                                                  source_path=source_path,
                                                                  is_two_file=is_two_file,
                                                                  post=post,
                                                                  lang=lang)                                                        
        if (source_path is not None and
              not post.meta['en'].get('hide_notebook_header', 'false').strip().lower() == 'true'):
            return f'<!-- {str(post.meta)} -->' + HEADER.format(fname=urllib.parse.quote(source_path, safe='')) + html, deps
        else:
            return html, deps

    def read_metadata(self, post, lang=None):
        metadata = super(CompileIPynbWithHeader, self).read_metadata(post, lang)
        if 'has_math' not in metadata:
            metadata['has_math'] = 'true'
        if 'previewimage' not in metadata:
            nb_fname = os.path.basename(post.source_path)
            base_fname = os.path.splitext(nb_fname)[0]
            for extension in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
                image_fname = os.path.join('images', base_fname+extension)
                if os.path.isfile(os.path.join('files', image_fname)):
                    metadata['previewimage'] = f'/{image_fname}'
                    break
        return metadata
