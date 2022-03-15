from imp import reload
import uvicorn
from src.app import create_app
from src.config import Config as config
if __name__ == '__main__':
    uvicorn.run("src.app:create_app", host=config.host, port=config.port, reload=True, access_log=False)