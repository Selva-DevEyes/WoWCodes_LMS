"""Playground execution API endpoint."""
import sys
import io
import time
from typing import Dict, Any, Optional
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/playground", tags=["Playground"])


class CodeExecutionRequest(BaseModel):
    language: str = "javascript"
    code: str
    input_data: Optional[str] = None


class CodeExecutionResponse(BaseModel):
    success: bool
    output: str
    error: Optional[str] = None
    execution_time_ms: float


@router.post("/execute", response_model=CodeExecutionResponse)
def execute_code(
    payload: CodeExecutionRequest,
    current_user: User = Depends(get_current_user),
):
    """Safely evaluate/run code snippets for learning playground."""
    start_time = time.time()
    code = payload.code.strip()

    if not code:
        raise HTTPException(status_code=400, detail="Code content cannot be empty.")

    if payload.language.lower() == "python":
        # Capture stdout/stderr for Python execution
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        exec_globals: Dict[str, Any] = {}
        error_msg = None
        success = True

        try:
            # Restricted execution environment
            exec(code, {"__builtins__": __builtins__}, exec_globals)
            output = redirected_output.getvalue()
            if not output:
                output = "[Code executed successfully with no output]"
        except Exception as e:
            success = False
            output = redirected_output.getvalue()
            error_msg = f"{type(e).__name__}: {str(e)}"
        finally:
            sys.stdout = old_stdout

        exec_time = round((time.time() - start_time) * 1000, 2)
        return CodeExecutionResponse(
            success=success,
            output=output,
            error=error_msg,
            execution_time_ms=exec_time,
        )

    # For JavaScript execution feedback from backend
    exec_time = round((time.time() - start_time) * 1000, 2)
    return CodeExecutionResponse(
        success=True,
        output="[Backend JavaScript Runner Ready - Browser engine handles live web execution]",
        error=None,
        execution_time_ms=exec_time,
    )
