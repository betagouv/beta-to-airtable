from airtable import airtable


class AirtableAPI:

    def __init__(self, base, key, table):
        self.api = airtable.Airtable(base, key)
        self.table = table

    def all(self):
        # Récupérer les données Airtable
        records = self.api.get(self.table, fields=['ID', 'Nom', 'Statut'])
        startups = records['records']

        while records.get('offset'):
            records = self.api.get(
                self.table,
                fields=['ID', 'Nom', 'Statut'],
                offset=records.get('offset')
            )
            startups += records['records']

        # ,limit=10
        return startups

    def create(self, id, name, mission):
        self.api.create(self.table,
                        {'ID': id,
                         'Nom': name,
                         'Mission': mission})

    def update(self, id, name, mission, start):
        end
