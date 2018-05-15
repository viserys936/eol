from django.db.backends.signals import connection_created
def deactivate_synchronous(sender, connection, **kwargs):
    """Enable integrity constraint with sqlite."""
    if connection.vendor == 'sqlite':
        cursor = connection.cursor()
        cursor.execute('PRAGMA synchronous=OFF;')

connection_created.connect(deactivate_synchronous)
