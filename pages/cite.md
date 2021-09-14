<!--
.. title: How to cite Brian
.. slug: cite
.. date: 2020-01-21 13:20:06 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->
## How to cite Brian

### In a paper

When you use Brian in your research, please cite our main paper:

<div class="alert alert-success" role="alert">
{{% publication authors="Stimberg M, Brette R, Goodman DFM" year="2019"
                title="Brian 2, an intuitive and efficient neural simulator"
                url="https://elifesciences.org/articles/47314"
                journal="eLife" extras="8:e47314. doi: 10.7554/eLife.47314" %}}
<details>
<summary>BibTeX (click to expand)</summary>
```bibtex
@article{Stimberg2019,
	title = {Brian 2, an intuitive and efficient neural simulator},
	volume = {8},
	issn = {2050-084X},
	doi = {10.7554/eLife.47314},
	journal = {eLife},
	author = {Stimberg, Marcel and Brette, Romain and Goodman, Dan FM},
	editor = {Skinner, Frances K},
	month = aug,
	year = {2019},
	pages = {e47314}
}
``` 
</details>
</div>

<br>
Some journals use an <abbr title="Research Resource Identifiers">RRID</abbr> to reference software tools. The Brian simulator
is registered as [SCR_002998](https://scicrunch.org/resolver/SCR_002998).

To cite a specific version of Brian, you can refer to the identifiers stored on [Zenodo](https://doi.org/10.5281/zenodo.654861):

<div class="zenodo-versions">
<div class="btn-group btn-group-toggle" data-toggle="buttons" id="zenodo-versions">
</div>
<blockquote id="zenodo-citation" class="blockquote">Requires JavaScript</blockquote>
</div>
<script type="text/javascript">
let versions = {
    // Date, DOI
    "2.4": ["Sep 4, 2020", "10.5281/zenodo.4015226"],
    "2.3": ["Dec 20, 2019", "10.5281/zenodo.3607592"],
    "2.2.2.1": ["Mar 29, 2019", "10.5281/zenodo.2619969"],
    "2.2": ["Oct 8, 2018", "10.5281/zenodo.1459786"],
    "2.1.3.1": ["Jun 7, 2018", "10.5281/zenodo.1346770"],
    "2.1": ["Oct 30, 2017", "10.5281/zenodo.1039232"],
    "2.0.2": ["Jun 7, 2017", "10.5281/zenodo.804429"]
};

function get_citation(version) {
    let data = versions[version];
    let date = data[0];
    let doi = data[1];
    let citation = 'Stimberg, Marcel, Goodman, Dan F.M., & Brette, Romain. (' + date + '). Brian 2 (Version ' + version + '). Zenodo. doi: <a href="http://doi.org/' + doi + '">' + doi + '</a>';
    return citation;
};

function update_text() {
    version = document.querySelector('input[name="version"]:checked').id;
    citation = get_citation(version);
    citation_field = document.getElementById('zenodo-citation');
    citation_field.innerHTML = citation;
};

(function () {
    let button_group = document.getElementById('zenodo-versions');
    let counter = 0;
    for (var version in versions) {
      let new_label = document.createElement('label');
      if (counter == 0) {
        new_label.setAttribute('class', 'btn btn-secondary active m-1');
      } else {
        new_label.setAttribute('class', 'btn btn-secondary m-1');
      };
      if (counter == 0) {      
      new_label.innerHTML='<input type="radio" name="version" autocomplete="off" id="' + version + '" checked onchange="update_text()">Version ' + version + '</input>';
      } else {
      new_label.innerHTML='<input type="radio" name="version" autocomplete="off" id="' + version + '" onchange="update_text()">Version ' + version + '</input>';
      }
      button_group.appendChild(new_label);
      counter++;
    };

    update_text();
})();

</script>

<p>
    You may be interested in our <a href="/publications">other publications about Brian</a>.
</p>

### In a poster

Please cite us above and include a copy of the
<a href="https://github.com/brian-team/brian-material/tree/master/logos">Brian logo</a> and webpage address.
