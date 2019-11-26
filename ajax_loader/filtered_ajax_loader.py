from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader, DEFAULT_PAGE_SIZE


class FilteredAjaxModelLoader(QueryAjaxModelLoader):
    additional_filters = []

    def get_list(self, term, offset=0, limit=DEFAULT_PAGE_SIZE):
        filters = list(
            field.ilike(u'%%%s%%' % term) for field in self._cached_fields
        )
        for f in self.additional_filters:
            filters.append(f)

        return (
            db.session.query(self.model).filter(*filters).all()
        )

    def __init__(self, name, session, model, **options):
        super(FilteredAjaxModelLoader, self).__init__(name, session, model, **options)
        self.additional_filters = options.get('filters')
