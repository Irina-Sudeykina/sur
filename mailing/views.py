from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from mailing.models import Recipient, Message, Mailing
from .forms import RecipientForm, MessageForm, MailingForm
from .services import send_messages_by_request


class RecipientListView(ListView):
    model = Recipient


class RecipientDetailView(DetailView):
    model = Recipient


class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy("mailing:recipient_list")

    # def form_valid(self, form):
        # dog = form.save()
        # user = self.request.user
        # dog.owner = user
        # dog.save()
        # return super().form_valid(form)


class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy("mailing:recipient_list")

    def get_success_url(self):
        return reverse("mailing:recipient_detail", args=[self.kwargs.get("pk")])

    # def get_object(self, queryset=None):
        # obj = super().get_object(queryset)
        # if obj.owner != self.request.user and not self.request.user.has_perm("mailing.can_unpublish_Recipient"):
            # raise PermissionDenied("Вы не владелец данного клиента и не можете его редактировать.")
        # return obj

    # def form_valid(self, form):
        # Recipient = form.save(commit=False)

        # Проверяем, имеет ли пользователь разрешение изменять статус публикации
        # if "is_publication" in form.changed_data and not self.request.user.has_perm("mailing.can_unpublish_Recipient"):
            # raise PermissionDenied("Вы не имеете прав менять статус публикации клиента.")

        # Recipient.save()
        # return super().form_valid(form)


class RecipientDeleteView(DeleteView):
    model = Recipient
    success_url = reverse_lazy("mailing:recipient_list")
    permission_required = "mailing.delete_recipient"

    # def dispatch(self, request, *args, **kwargs):
        # """
        # Переопределяем метод dispatch(), чтобы провести дополнительные проверки
        # перед удалением клиента.
        # """
        # obj = self.get_object()
        # if obj.owner != self.request.user and not self.request.user.has_perm("mailing.delete_Recipient"):
            # raise PermissionDenied("Только владельцы и модераторы могут удалить клиента.")
        # return super().dispatch(request, *args, **kwargs)


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")

    def get_success_url(self):
        return reverse("mailing:message_detail", args=[self.kwargs.get("pk")])


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")
    permission_required = "mailing.delete_message"


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.update_status()  # пересчёт и сохранение статуса
        return obj


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")

    def get_success_url(self):
        return reverse("mailing:mailing_detail", args=[self.kwargs.get("pk")])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")
    permission_required = "mailing.delete_mailing"


def send_mailing(request, pk):
    mailing = get_object_or_404(Mailing, id=pk)
    
    if request.method == 'POST':
        result = send_messages_by_request(mailing)
        if result is False:
            messages.error(request, 'Рассылка не доступна в данное время!')
        else:
            messages.success(request, 'Рассылка успешно запущена!')
        return HttpResponseRedirect(reverse('mailing:mailing_detail', kwargs={'pk': pk}))
    
    return render(request, 'mailing/send_confirmation.html', {'mailing': mailing})
