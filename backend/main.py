from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .agent import OmniAgent

app = FastAPI(title="OmniArchitect API")

# Enable CORS for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = OmniAgent()

class PromptRequest(BaseModel):
    description: str

class GenerateResponse(BaseModel):
    graph: dict
    ui_code: str
    message: str

@app.get("/")
def read_root():
    return {"status": "OmniArchitect Core Online"}

@app.post("/generate", response_model=GenerateResponse)
async def generate_app(request: PromptRequest):
    try:
        # Step 1: Analyze prompt and build knowledge graph
        analysis = agent.analyze_prompt(request.description)
        
        # Step 2: Generate UI based on the first entity found
        code = agent.generate_ui_code(analysis["entities"])
        
        return {
            "graph": analysis,
            "ui_code": code,
            "message": "App architecture and UI generated successfully."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
