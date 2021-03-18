<%inherit file="../home_comp.mako"/>

<%def name="sidebar()">
    <div class="well">
        <img class="img-polaroid" src="${req.static_url('tular:static/TuLaR_Image.jpeg')}"/>
        <ul class="nav nav-pills nav-stacked">
            <li><a href="#top">Overview</a></li>
            <li><a href="#publications">TuLaR publications</a></li>
        </ul>
    </div>
    <div class="well">
        <a href="https://uni-tuebingen.de/">
            <img src="${req.static_url('tular:static/uni_tuebingen_logo.png')}">
        </a>
    </div>
</%def>

<h2 id="publications">TuLaR (Tupían Language Resources)</h2>

<p class="lead" align="justify">
	Tupían Language Resources (TuLaR) is an ongoing project being compiled within the
    <a href="https://uni-tuebingen.de/de/163612">CrossLingference</a> project that intends to
    collect linguistic (lexical, morphological, and syntactical) and ethnographic data related
    to the Tupían languages. The data is made available under
    <a href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) </a>.
    TuLaR comprises six databases all of which are work-in-progress in different stages of completion.
</p>

<div class="clearfix"></div>

<h3>TuLaR publications</h3>

<ul>
<li class="bullet-list">Aragon, C. &amp; Ferraz Gerardi, F. The typology of grammatical relations in Tuparian languages, with special focus on Akuntsú. In Language Change and Linguistic Diversity: studies in honour of Lyle Campbell. Thiago Chacon, Nala Lee and Wilson Silva (editors). Chapter 11 (forthcoming). </li>
        <li class="bullet-list">Ferraz Gerardi, Fabrício &amp; Reichert, Stanislav &amp; Aragon, Carolina. (2021) TuLeD (Tupían Lexical Database): Introducing a database of a South American language family. To appear in <a href="https://link.springer.com/article/10.1007/s10579-020-09521-5#citeas">Language Resources and Evaluation.</a> DOI 10.1007/s10579-020-09521-5 </li>
<li class="bullet-list"><p>Ferraz Gerardi, Fabrício &amp; Reichert, Stanislav. (2021) The Tupí-Guaraní language family: a phylogenetic classification. <a href="https://benjamins.com/catalog/dia.18032.fer">Diachronica. </a></p></li>

<li class="bullet-list"><p>Fabrício Ferraz Gerardi, Stanislav Reichert, Carolina Aragon, Johann-Mattis List, & Tim Wientzek. (2020). CLDF dataset derived from Gerardi and Reichert's "TuLeD: Tupían lexical database" from 2020 (Version v0.10) [Data set]. <a href="https://doi.org/10.5281/zenodo.4161623"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4161623.svg" alt="DOI"></a></p></li>

<li class="bullet-list"><p>Aragon, Carolina &amp; Ferraz Gerardi, Fabrício (2020) <a href="https://github.com/UniversalDependencies/UD_Akuntsu-TuDeT/tree/dev">  UniversalDependencies/UD_Akuntsu-TuDeT: Akuntsú Treebank </a>  </p></li>

<li class="bullet-list"><p>Aragon, Carolina &amp; Ferraz Gerardi, Fabrício (2021) <a href="https://github.com/UniversalDependencies/UD_Makurap-TuDeT/tree/dev">  UniversalDependencies/UD_Akuntsu-TuDeT: Makurap Treebank </a>  </p></li>

<li class="bullet-list"><p>Ferraz Gerardi, Fabrício &amp; Aragon, Carolina &amp; Godoy, Gustavo <a href="https://github.com/UniversalDependencies/UD_Kaapor-TuDeT/tree/dev">UniversalDependencies/UD_Kaapor-TuDeT: Ka'apor Treebank </a>. </p></li>

<li class="bullet-list"><p>Ferraz Gerardi, Fabrício &amp; Lorena, Martin-Rodriguez <a href="https://github.com/UniversalDependencies/UD_Guajajara-TuDeT/tree/dev">UniversalDependencies/UD_Guajajara-TuDeT: Guajajara Treebank </a>. </p></li>

<li class="bullet-list"><p>Ferraz Gerardi, Fabrício(2020) <a href="https://github.com/UniversalDependencies/UD_Munduruku-TuDeT/tree/dev">  UniversalDependencies/UD_Munduruku-TuDeT: Mundurukú Treebank </a>.</p></li>

<li class="bullet-list"><p>Ferraz Gerardi, Fabrício. (2020) The Structure of Mundurukú (ongoing work). Tübingen.</p></li>

<li class="bullet-list"><p>Ferraz Gerardi, Fabrício &amp; Reichert, Stanislav &amp; Blum, Frederic (2020) TuMoD: Tupían Morphological Database (to be published). Universität Tübingen.</p></li>

<li class="bullet-list"><p>Ferraz Gerardi, Fabrício &amp; Merzhevich, Tatiana (2020) <a href="https://github.com/UniversalDependencies/UD_Tupinamba-TuDeT/tree/dev"> UniversalDependencies/UD_Tupinamba-TuDeT: Tupinambá Treebank </a>.</p></li>

<li class="bullet-list"><p>Godoy, Gustavo &amp; Ferraz Gerardi, Fabrício &amp; Carolina Aragon (2021). Tupían Ethnographic Database (to be published). Universität Tübingen </li></p>
<li class="bullet-list"><p>Fabrício Ferraz Gerardi, Stanislav Reichert, Tim Wientzek, Verena Blaschke, Eric de Mattos, Zhuge Gao, and Nianheng wu. (2019). LanguageStructure/TuLeD: Pre-release (version 0.9). Eberhard Karls Universität Tübingen. <a href="https://zenodo.org/badge/latestdoi/263996134"><img src="data:image/svg+xml; charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgd2lkdGg9IjE4NiIgaGVpZ2h0PSIyMCI+CiAgICAgICAgPGxpbmVhckdyYWRpZW50IGlkPSJiIiB4Mj0iMCIgeTI9IjEwMCUiPgogICAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiNiYmIiIHN0b3Atb3BhY2l0eT0iLjEiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLW9wYWNpdHk9Ii4xIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgICAgICA8bWFzayBpZD0iYSIgd2lkdGg9IjE4NiIgaGVpZ2h0PSIyMCI+CiAgICAgICAgICAgIDxyZWN0IHdpZHRoPSIxODYiIGhlaWdodD0iMjAiIHJ4PSIzIgogICAgICAgICAgICBmaWxsPSIjZmZmIi8+CiAgICAgICAgPC9tYXNrPgogICAgICAgIDxnIG1hc2s9InVybCgjYSkiPgogICAgICAgICAgICA8cGF0aCBmaWxsPSIjNTU1IiBkPSJNMCAwaDMxdjIwSDB6IiAvPgogICAgICAgICAgICA8cGF0aCBmaWxsPSIjMDA3ZWM2IgogICAgICAgICAgICBkPSJNMzEgMGgxNTV2MjBIMzF6IgogICAgICAgICAgICAvPgogICAgICAgICAgICA8cGF0aCBmaWxsPSJ1cmwoI2IpIiBkPSJNMCAwaDE4NnYyMEgweiIgLz4KICAgICAgICA8L2c+CiAgICAgICAgPGcgZmlsbD0iI2ZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkRlamFWdSBTYW5zLAogICAgICAgIFZlcmRhbmEsR2VuZXZhLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiPgogICAgICAgICAgICA8dGV4dCB4PSIxNiIgeT0iMTUiIGZpbGw9IiMwMTAxMDEiCiAgICAgICAgICAgIGZpbGwtb3BhY2l0eT0iLjMiPgogICAgICAgICAgICAgICAgRE9JCiAgICAgICAgICAgIDwvdGV4dD4KICAgICAgICAgICAgPHRleHQgeD0iMTYiIHk9IjE0Ij4KICAgICAgICAgICAgICAgIERPSQogICAgICAgICAgICA8L3RleHQ+CiAgICAgICAgICAgIDx0ZXh0IHg9IjEwOCIKICAgICAgICAgICAgeT0iMTUiIGZpbGw9IiMwMTAxMDEiIGZpbGwtb3BhY2l0eT0iLjMiPgogICAgICAgICAgICAgICAgMTAuNTI4MS96ZW5vZG8uMzk4OTU1NgogICAgICAgICAgICA8L3RleHQ+CiAgICAgICAgICAgIDx0ZXh0IHg9IjEwOCIgeT0iMTQiPgogICAgICAgICAgICAgICAgMTAuNTI4MS96ZW5vZG8uMzk4OTU1NgogICAgICAgICAgICA8L3RleHQ+CiAgICAgICAgPC9nPgogICAgPC9zdmc+" /></a></p></li> 

</ul>


<h3>TuLaR Contributors</h3>

<li>Agnaldo Makuráp</li>
<li>Christian Fest (Universität Wien)</li>
<li>Denny Moore (Museu Paraense Emílio Goeldi)</li>
<li>Françoise Rose (Université de Lyon)</li>
<li>  <a href="http://nupeli-gela.weebly.com"> Gustavo Godoy (Ppgas Universidade Federal do Rio de Janeiro)</a>  </li>
<li>Harald Hammarström (Uppsala Universitet)</li>
<li>Iram Káv Sona Gavião</li>
<li>Nilson Gabas Júnior (University of California)</li>
<li>Swintha Danielsen (Universität Leipzig)</li>
<li>Wolf Dietrich (Universität Münster)</li>
<li>Zachary O'Hagan (University of California)</li>

<br>
