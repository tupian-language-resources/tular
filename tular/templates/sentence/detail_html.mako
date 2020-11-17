<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "sentences" %>

<%block name="head">
    <link href="${request.static_url('tular:static/style-vis.css')}" rel="stylesheet">
    <script src="${request.static_url('tular:static/jquery.min.js')}"></script>
    <script src="${request.static_url('tular:static/jquery-ui.min.js')}"></script>
    <script src="${request.static_url('tular:static/jquery.svg.min.js')}"></script>
    <script src="${request.static_url('tular:static/jquery.svgdom.min.js')}"></script>
    <script src="${request.static_url('tular:static/waypoints.min.js')}"></script>
    <script src="${request.static_url('tular:static/configuration.js')}"></script>
    <script src="${request.static_url('tular:static/util.js')}"></script>
    <script src="${request.static_url('tular:static/annotation_log.js')}"></script>
    <script src="${request.static_url('tular:static/webfont.js')}"></script>
    <script src="${request.static_url('tular:static/dispatcher.js')}"></script>
    <script src="${request.static_url('tular:static/url_monitor.js')}"></script>
    <script src="${request.static_url('tular:static/visualizer.js')}"></script>
    <script src="${request.static_url('tular:static/annodoc.js')}"></script>
    <script src="${request.static_url('tular:static/config.js')}"></script>
    <script src="${request.static_url('tular:static/conllu.js')}"></script>

</%block>

<%def name="sidebar()">
    % if ctx.value_assocs:
    <%util:well title="${_('Datapoints')}">
        <ul>
        % for va in ctx.value_assocs:
            % if va.value:
            <li>${h.link(request, va.value.valueset, label='%s: %s' % (va.value.valueset.parameter.name, va.value.domainelement.name))}</li>
            % endif
        % endfor
        </ul>
    </%util:well>
    % endif
</%def>

<h2>${_('Sentence')} ${ctx.id}</h2>
<dl>
    <dt>${_('Language')}:</dt>
    <dd>${h.link(request, ctx.language)}</dd>
</dl>

${h.rendered_sentence(ctx)|n}

<code class="conllu-parse" tabs="yes"><pre>
${ctx.conllu}
</pre></code>


<dl>
% if ctx.comment:
<dt>Comment:</dt>
<dd>${ctx.markup_comment or ctx.comment|n}</dd>
% endif
% if ctx.source:
<dt>${_('Type')}:</dt>
<dd>${ctx.type}</dd>
% endif
% if ctx.references or ctx.source:
<dt>${_('Source')}:</dt>
% if ctx.source:
<dd>${ctx.source}</dd>
% endif
% if ctx.references:
<dd>${h.linked_references(request, ctx)|n}</dd>
% endif
% endif
</dl>

<script>
    var documentCollections = {};
    var webFontURLs = [
        '${req.static_url("tular:static/PT_Sans-Caption-Web-Regular.ttf.css")}',
        '${req.static_url("tular:static/Liberation_Sans-Regular.ttf.css")}',
    ];

    $(document).ready(function() {
        Annodoc.activate(Config.bratCollData, documentCollections);
        $('.show-hide-div').hide();
    });
</script>