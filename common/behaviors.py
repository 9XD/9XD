class LimitedPageMixin(object):
    range_length = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page = context['page_obj']
        self.convert_paginator_range(paginator, page)
        return context

    def convert_paginator_range(self, paginator, page):
        page_count = page.paginator.num_pages
        range_length = self.range_length
        current_page = page.number
        if self.range_length < 1:
            raise Exception("Optional argument \"range\" expecting integer greater than 0")
        elif self.range_length > page_count:
            range_length = page_count

        range_length -= 1
        range_min = max(current_page - (range_length // 2), 1)
        range_max = min(current_page + (range_length // 2), page_count)
        range_diff = range_max - range_min
        if range_diff < range_length:
            shift = range_length - range_diff
            if range_min - shift > 0:
                range_min -= shift
            else:
                range_max += shift

        paginator.converted_range = range(range_min, range_max + 1)
