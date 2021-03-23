<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "contributions" %>

<h2>${ctx.name}: ${ctx.description}</h2>

<p class="lead" align="justify">

TuDeT (<b>Tu</b>pían <b>De</b>pendency <b>T</b>reebank) is a collection of treebanks of Tupían languages
originally part of <a href"https://universaldependencies.org"> Universal Dependencies</a>. This database
displays the sentences, visualization of the dependencies, glossings, and translations in English and Portuguese. 
Some of the main goals include: application the treebanks in the development of pedagogical materials (also digital) together with indigenous 
teachers, documentation, maintenance, and revitalization of the languages, as well as the use of the treebanks for linguistic analyses.

The treebanks are in their initial phase of development, in which sentences are being manually annotated. Tools are being developed
to speed up the POS-tagging and to allow for partial automatic annotation. For detailed information about each treebank, the annotations, and
sources, refer to the links at the bottom of the page:

</p>


${util.data()}

% if ctx.id == 'tuled':
    <% dt = request.get_datatable('values', h.models.Value, contribution=ctx) %>
    % if dt:
        <div>
            ${dt.render()}
        </div>
    % endif
% elif ctx.id == 'tudet':
    <ul>
        % for lang, c in languages:
            <li>
                <a href="${lang.treebank_url(req)}">${lang.name}</a>
                (${c} sentences)
            </li>
        % endfor
    </ul>
% endif

<ul>

<li class="bullet-list"><p>Aragon, Carolina &amp; Ferraz Gerardi, Fabrício (2020) <a href="https://github.com/UniversalDependencies/UD_Akuntsu-TuDeT/tree/dev">  UniversalDependencies/UD_Akuntsu-TuDeT: Akuntsú Treebank </a>  </p></li>

<li class="bullet-list"><p>Aragon, Carolina &amp; Ferraz Gerardi, Fabrício (2021) <a href="https://github.com/UniversalDependencies/UD_Makurap-TuDeT/tree/dev">  UniversalDependencies/UD_Akuntsu-TuDeT: Makurap Treebank </a>  </p></li>

<li class="bullet-list"><p>Ferraz Gerardi, Fabrício &amp; Aragon, Carolina &amp; Godoy, Gustavo (2021) <a href="https://github.com/UniversalDependencies/UD_Kaapor-TuDeT/tree/dev"> UniversalDependencies/UD_Kaapor-TuDeT: Ka'apor Treebank </a>. </p></li>

<li class="bullet-list"><p> Lorena, Martin-Rodriguez &am; Ferraz Gerardi, Fabrício (2021) <a href="https://github.com/UniversalDependencies/UD_Guajajara-TuDeT/tree/dev">UniversalDependencies/UD_Guajajara-TuDeT: Guajajara Treebank </a>. </p></li>

<li class="bullet-list"><p>Ferraz Gerardi, Fabrício(2020) <a href="https://github.com/UniversalDependencies/UD_Munduruku-TuDeT/tree/dev"> UniversalDependencies/UD_Munduruku-TuDeT: Mundurukú Treebank </a>.</p></li>

<li class="bullet-list"><p>Ferraz Gerardi, Fabrício &amp; Merzhevitch, Tatiana (2020) <a href="https://github.com/UniversalDependencies/UD_Tupinamba-TuDeT/tree/dev"> UniversalDependencies/UD_Tupinamba-TuDeT: Tupinambá Treebank </a>.</p></li>


</ul>
