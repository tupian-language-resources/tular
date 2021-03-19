<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "sentences" %>


<%block name="head">
    % if lang:
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
        <style>
            li.sentence {border-bottom: 2px solid black; margin-bottom: 1em;}
            div.show-hide-div {visibility: hidden;}
        </style>
    % endif
</%block>


% if lang is None:
    <h2>${_('Examples')}</h2>
    <div>
        ${ctx.render()}
    </div>
% else:
        <h2>Dependency treebank for ${lang.name}</h2>
        <ol>
            % for sent in sorted(sentences, key=lambda s: int(s.id.split('-')[1])):
                <li class="sentence">
                    <div class="well well-small">
                        ${h.rendered_sentence(sent)|n}
                    </div>
                    <table class="table table-nonfluid table-condensed">
                        <thead>
                        <tr>
                            <th>form</th>
                            % for token in sent.tokenlist:
                                <td>${token['form']}</td>
                            % endfor
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <th>lemma</th>
                            % for token in sent.tokenlist:
                                <td>${token['lemma']}</td>
                            % endfor
                        </tr>
                        <tr>
                            <th>pos</th>
                            % for token in sent.tokenlist:
                                <td>${token['xpos'] or ''}</td>
                            % endfor
                        </tr>
                        <tr>
                            <th>features</th>
                            % for token in sent.tokenlist:
                                <td>${'|'.join('{}={}'.format(k, v) for k, v in (token['feats'] or {}).items())}</td>
                            % endfor
                        </tr>
                        </tbody>
                    </table>
                    <code class="conllu-parse" tabs="yes"><pre>
                        ${u.fix_conllu(sent.conllu)}
                    </pre>
                    </code>
                </li>
            % endfor
        </ol>

    <script>
        var documentCollections = {};
        var webFontURLs = [
            '${req.static_url("tular:static/PT_Sans-Caption-Web-Regular.ttf.css")}',
            '${req.static_url("tular:static/Liberation_Sans-Regular.ttf.css")}',
        ];

        $(document).ready(function () {
            Annodoc.activate(Config.bratCollData, documentCollections);
        });
    </script>

% endif
