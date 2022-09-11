from django.core.management.base import BaseCommand
from mainapp.models import Item
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creating superuser and specified number of products for a test'

    def add_arguments(self, parser):
        parser.add_argument('count_of_items', nargs=1, type=int)

    def handle(self, *args, **options):
        #Создание суперпользователя
        Superuser = get_user_model()
        if not Superuser.objects.filter(username='admin'):
            Superuser.objects.create_superuser('admin', 'admin@admin.com', 'adminadmin')

        count_of_items = options['count_of_items'][0]

        #Если нужно/можно очистить весь список продуктов
        # items = Item.objects.all()
        # items.delete()

        #Удаление только тестовых продуктов в том количестве, в котором планируется создать новых
        for i in range(count_of_items):
            item = Item.objects.filter(name=f'Item_{i}')
            item.delete()

        #Создание тестовых продуктов
        for i in range(count_of_items):
            Item.objects.create(name=f'Item_{i}', description=f'description_{i}',
                                price=f'{i*2}')

        self.stdout.write(f'Successfully created {count_of_items} items!')
