from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    def __init__(self) -> None:
       
        self.MIN_SIZE = int(os.getenv("MIN_SIZE", "1"))
        self.MAX_SIZE = int(os.getenv("MAX_SIZE", "20"))
        self.TIMEOUT = int(os.getenv("TIMEOUT_DB", "10"))

        

        self.DATABASE_URL = os.getenv('DATABASE_URL')

        if not self.DATABASE_URL:
            raise RuntimeError(f"DatDATABASE_URL not set")

settings_db = Settings()