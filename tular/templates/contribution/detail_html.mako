<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "contributions" %>

<%def name="sidebar()">
    % if ctx.description:
        <div class="well">
            <h4>Cite as</h4>
            <blockquote>
                ${ctx.description}
            </blockquote>
        </div>
    % endif
    <div class="well">
        <h4>Contributors</h4>
        <ul>
            % for c in ctx.primary_contributors:
                <li>${c.name}</li>
            % endfor
        </ul>
    </div>
</%def>


<h2>${ctx.name}</h2>


% if ctx.id == 'tuled':
    <% dt = request.get_datatable('values', h.models.Value, contribution=ctx) %>
    % if dt:
        <div>
            ${dt.render()}
        </div>
    % endif
% elif ctx.id == 'tudet':
    <p class="lead">
        TuDeT (<b>Tu</b>pían <b>De</b>pendency <b>T</b>reebank) is a collection of treebanks of Tupían languages
        originally part of <a href="https://universaldependencies.org">Universal Dependencies</a>. This database
        displays the sentences, visualization of the dependencies, glossings, and translations in English and
        Portuguese.
        Some of the main goals include: application of treebanks in the development of pedagogical materials (also
        digital) together with indigenous
        teachers, documentation, maintenance, and revitalization of the languages, as well as the use of the treebanks
        for linguistic analyses.
    </p>
    <p>
        The treebanks are in their initial phase of development, in which sentences are being manually annotated. Tools
        are being developed
        to speed up the POS-tagging and to allow for partial automatic annotation. For detailed information about each
        treebank, the annotations, and sources, refer to the links to the GitHub repositories.
    </p>

    <table class="table table-nonfluid">
        <thead>
            <tr>
                <th>Language</th>
                <th>Treebank in TuDeT</th>
                <th>Number of sentences</th>
                <th>Repository on GitHub</th>
            </tr>
        </thead>
        <tbody>
            % for lang, c in languages:
                <tr>
                    <td>
                        ${h.link(req, lang)}
                    </td>
                    <td>
                        <a href="${lang.treebank_url(req)}">${lang.name} Treebank</a>
                    </td>
                    <td class="right">
                        ${c}
                    </td>
                    <td>
                        <img width="20" src="${req.static_url('tular:static/logo-ud.png')}">
                        ${h.external_link('https://github.com/UniversalDependencies/UD_{}-TuDeT/'.format(lang.id))}
                    </td>
                </tr>
            % endfor
        </tbody>
    </table>
% endif
