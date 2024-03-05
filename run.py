from app.projet import app
from app.projet import urls_car
from app.projet import urls_client
from app.projet import urls_location
from app.projet import urls_suivi
from app.projet import urls_entretien
from app.projet import urls_handler




import uvicorn

if __name__== '__main__':
    uvicorn.run(app)