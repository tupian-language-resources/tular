<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "contributions" %>

<h2>${ctx.name}: ${ctx.description}</h2>

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
