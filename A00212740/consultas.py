from modelo import db
from modelo import Stats
from comandos import get_all_stats, get_cpu, get_service, get_hdd



db.create_all()

stats = Stats('10.4%', '758m', '51G', 'DDead' )



db.session.add(stats)
db.session.commit()

stats2 = Stats.query.all()
print(stats2)

