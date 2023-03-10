from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from api.models import Personne

"""
curl http://localhost:8000/api/v1/person/

curl --dump-header - -H "Content-Type: application/json" -X POST --data \
    '{"nom": "Corson", "prenom": "Antoine", "date_de_naissance": "1981-02-28"}' \
    http://localhost:8000/api/v1/person/

"""
class PersonResource(ModelResource):
    class Meta:
        queryset = Personne.objects.all().order_by('nom')
        resource_name = 'person'
        allowed_methods = ['post', 'get', 'put', 'delete']
        excludes = ['id', 'created_at', 'updated_at'] 
        filtering = {
            'nom': ALL
        }
        authorization = Authorization()
    
    def dehydrate(self, bundle):
        bundle.data['age'] = bundle.obj.calculate_age()
        # try:
        #     #bundle.data['flocking'] = list(bundle.obj.flocking.order_by('rank').values('product_id'))
        #     bundle.data['flocking'] = model_to_dict(bundle.obj.flocking, exclude=['id', 'productflocking'])
        # except ObjectDoesNotExist:
        #     bundle.data['flocking'] = dict()
        # bundle.data['patch'] = list(bundle.obj.flockingpatch.values('product_id'))
        return bundle