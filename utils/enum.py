from enum import StrEnum


class ExceptionEnum(StrEnum):
    MISSING_CREDENTIALS = "Missing required environment variables"
    INVALID_API_RESPONSE = "Invalid response from movies API"
    AUTHENTICATION_ERROR = "Authentication failed"
    CONNECTION_ERROR = "Connection to external API failed"


class ValidationEnum(StrEnum):
    MISSING_REQUIRED_FIELD = "Missing required field"
    GENRE_REQUIRED = "Genre filed is required"
    MOVIE_REQUIRED = "Movie field is required"
    TITLE_REQUIRED = "Title field is required"


class ResponseEnum(StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"
    ACCEPTED = "Accepted"
    ERROR = "error"
    NOT_FOUND = "not found"
    INVALID_REQUEST = "invalid request"
    INTERNAL_SERVER_ERROR = "internal server error"
    UNAUTHORIZED = "unauthorized"
    RECORD_DELETED = "Record deleted successfully"
    RECORD_UPDATED = "Record updated successfully"
    COLLECTION_NOT_FOUND = "Collection not found"
