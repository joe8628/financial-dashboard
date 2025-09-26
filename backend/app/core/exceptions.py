from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

class CustomException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

async def custom_exception_handler(request: Request, exc: CustomException):
    logger.error(f"Custom exception: {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

class DatabaseException(CustomException):
    def __init__(self, message: str = "Database operation failed"):
        super().__init__(message, status_code=500)

class ValidationException(CustomException):
    def __init__(self, message: str = "Validation failed"):
        super().__init__(message, status_code=422)