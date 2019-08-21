


FTTHProject:
    |_Clusters(kmz PolyGon)
                 |_Houses



#Track HousePassed per Cluster per project




class FTTSProject(models.Model):
    project_name = CharField

class Claster(models.Model):
    project_name = FK (FTTHProject)
    no_houses =IntField()
    house_passed = IntField()
    Plah plah = plah field



    




