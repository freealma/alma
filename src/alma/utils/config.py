import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
load_dotenv(BASE_DIR / "config" / "alma.env")

class Config:
    # DeepSeek API
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE", "https://api.deepseek.com")
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db/alma.db")
    
    # LLM
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "deepseek-chat")
    DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))
    
    # Memory
    MEMORY_CONTEXT_SIZE = int(os.getenv("MEMORY_CONTEXT_SIZE", "5"))
    
    @staticmethod
    def validate():
        """Validate essential configuration"""
        if not Config.DEEPSEEK_API_KEY:
            raise ValueError("DEEPSEEK_API_KEY is not set in environment variables")

config = Config()