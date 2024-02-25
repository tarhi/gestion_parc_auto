from app import app
from app import urls_car
from app import urls_client
from app import urls_location
from app import urls_suivi
from app import urls_entretien
import uvicorn

if __name__== '__main__':
    uvicorn.run(app)