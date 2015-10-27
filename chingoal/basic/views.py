from django.views.generic import UpdateView, ListView
from django.http import HttpResponse
from django.template.loader import render_to_string
from basic.models import Item
from basic.forms import ItemForm

# items list
class ItemListView(ListView):
    model = Item
    template_name = 'basic/item_list.html';

    def get_queryset(self):
        return Item.objects.all()

# &quot;&quot;&quot;
# Edit item
# &quot;&quot;&quot;
class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'basic/item_edit_form.html';

    def dispatch(self, *args, **kwargs):
        self.item_id = kwargs[&#39;pk&#39;]
        return super(ItemUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = Item.objects.get(id=self.item_id)
        return HttpResponse(render_to_string('basic/item_edit_form_success.htm', {'item': item}))

