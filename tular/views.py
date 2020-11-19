from sqlalchemy import func
from pyramid.view import view_config
from clld.db.meta import DBSession
from clld.db.models import common


@view_config(route_name='completeness', renderer='completeness.mako')
def completeness(req):
    num_concepts = DBSession.query(common.Parameter).count()
    coverage = DBSession.query(common.Language, func.count(common.ValueSet.pk))\
        .join(common.ValueSet)\
        .group_by(common.Language)\
        .all()
    return {
        'languages': [(l, c, c / num_concepts * 100) for l, c in coverage],
        'total': (sum(i[1] for i in coverage), sum(i[1] for i in coverage) / (len(coverage) * num_concepts) * 100),
    }
