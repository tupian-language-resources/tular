<%inherit file="home_comp.mako"/>
<%namespace name="util" file="util.mako"/>

<h2>Completeness of the Tupían lexical database (TuLeD)</h2>

<%util:table items="${languages}" args="item" eid="refs" class_="table-condensed table-striped" options="${dict(aaSorting=[[3, 'desc']])}">\
    <%def name="head()">
        <th>Doculect</th><th>Subfamily</th><th>Translated concepts</th><th>Completion</th>
    </%def>
    <td>${h.link(request, item[0])}</td>
    <td>${item[0].subfamily}</td>
    <td class="right">${item[1]}</td>
    <td class="right">
        <span style="display: inline-block; direction: rtl; border-radius: 4px; padding-right: 2px; background-color: #CCFF66; width: ${item[2]}%">
            ${"{:.1f}".format(item[2])}%
        </span>
    </td>
    <%def name="foot()">
        <th style="text-align: left;" colspan="2">Total:</th>
        <th style="text-align: right;">${total[0]}</th>
        <th style="text-align: right;">${"{:.1f}".format(total[1])}%</th>
    </%def>
</%util:table>
