<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "languages" %>
<%! multirow = True %>

<%block name="title">${_('Language')} ${ctx.name}</%block>


<div class="row-fluid">
    <div class="span12">
        <h2>${_('Language')} ${ctx.name}</h2>
    </div>
</div>
<div class="row-fluid">
    <div class="span8">
        <dl>
            <dt>Glottocode:</dt>
            <dd>${u.glottolog_link(req, ctx)}</dd>
            <dt>Sources:</dt>
            <dd>
                <ul>
                    % for source in ctx.sources:
                        <li>${h.link(request, source, label=source.description)}<br/>
                            <small>${h.link(request, source)}</small></li>
                    % endfor
                </ul>
            </dd>
        </dl>
    </div>
    <div class="span4">
        <div class="well well-small">
            ${request.map.render()}
            ${h.format_coordinates(ctx)}
        </div>
    </div>
</div>
<div class="row-fluid">
    ${request.get_datatable('values', h.models.Value, language=ctx).render()}
</div>
