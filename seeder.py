from django_seed import Seed
#from myapp.models import Game, Player
from apps.products.models import Product

seeder = Seed.seeder()



seeder.add_entity(Product, 10, {
    'code':         random.randint(0,1000),
    'name':         faker.name(),
    'description':  faker.text(),
    'image':        faker.text(),
})
seeder.execute()