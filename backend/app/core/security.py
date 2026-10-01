from datetime import UTC, datetime, timedelta
from hashlib import sha256
from typing import Any

import bcrypt
from jose import jwt

from app.core.config import settings


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return bcrypt.checkpw(plain_password.encode("utf-8")[:72], hashed_password.encode("utf-8"))
    except Exception:
        return False


def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8")[:72], bcrypt.gensalt()).decode("utf-8")



def _create_token(subject: str, expires_delta: timedelta, secret: str, token_type: str) -> str:
    expire = datetime.now(UTC) + expires_delta
    payload: dict[str, Any] = {"sub": subject, "exp": expire, "type": token_type}
    return jwt.encode(payload, secret, algorithm=settings.jwt_algorithm)


def create_access_token(subject: str) -> str:
    return _create_token(
        subject=subject,
        expires_delta=timedelta(minutes=settings.access_token_expire_minutes),
        secret=settings.jwt_secret_key,
        token_type="access",
    )


def create_refresh_token(subject: str) -> str:
    return _create_token(
        subject=subject,
        expires_delta=timedelta(days=settings.refresh_token_expire_days),
        secret=settings.jwt_refresh_secret,
        token_type="refresh",
    )


def decode_access_token(token: str) -> dict[str, Any]:
    return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])


def decode_refresh_token(token: str) -> dict[str, Any]:
    return jwt.decode(token, settings.jwt_refresh_secret, algorithms=[settings.jwt_algorithm])


def hash_token(token: str) -> str:
    return sha256(token.encode("utf-8")).hexdigest()
