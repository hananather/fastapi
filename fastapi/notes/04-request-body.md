# Request Body:
- **Request Body vs. Response Body:**
  A *request body* contains data sent by the client to the API (commonly with POST, PUT, DELETE, or PATCH methods). A *response body* is data sent from the API back to the client.

- **Declaring Request Bodies:**
  Request bodies are declared as Python classes that inherit from Pydantic's `BaseModel`.
  Example model:
  ```python
  from pydantic import BaseModel

  class Item(BaseModel):
      name: str
      description: str | None = None
      price: float
      tax: float | None = None
  ```
  The model defines data validation automatically and supports optional fields by setting defaults to `None`.

- **Using in Path Operations:**
  You add the model as a parameter in your path operation function. FastAPI then:
  - Reads and parses incoming JSON payloads.
  - Validates and converts fields to the correct types.
  - Provides clear error messages if data is missing or incorrect.
  - Generates JSON schemas for the models, included in auto-generated OpenAPI docs.
  - Provides editor support (type hints, autocompletion) when using Pydantic models.

The main reason for using Pydantic in FastAPI is to validate and parse incoming data (usually from API requests) on the server side.

- Validation happens on the server, when an HTTP request hits your FastAPI endpoint.
- Pydantic checks if the incoming data matches your schema (fields, types, required/optional).
- If the data is invalid, FastAPI automatically returns a clear error message to the client.
- If valid, your function receives a clean, typed Python object, ready for use.

## Diagram — Request Body Flow

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'background': '#ffffff',
    'fontFamily': 'Inter, ui-sans-serif, system-ui'
  },
  'themeCSS': 'svg { background: #ffffff !important; }',
  'flowchart': { 'useMaxWidth': false, 'diagramPadding': 28, 'htmlLabels': true }
}}%%
flowchart LR
  subgraph CANVAS[ ]
    direction LR
    C["Client"]:::dim --> HTTP["HTTP Request<br/>(JSON body)"]:::dim --> API["FastAPI Endpoint"]:::accent
    API --> VALIDATE["Pydantic Model<br/>Parse & Validate"]:::accent

    VALIDATE -- valid --> OK["Typed Python Object<br/>(Model instance)"]:::good --> HANDLER["Endpoint Function<br/>(business logic)"]:::dim --> RESP["HTTP Response<br/>(200/201 + body)"]:::dim
    VALIDATE -- invalid --> ERR["422 Unprocessable Entity<br/>Validation error details"]:::warn
  end

  classDef good fill:#DCFCE7,stroke:#16A34A,stroke-width:1.2px,color:#064E3B;
  classDef warn fill:#FEF9C3,stroke:#CA8A04,stroke-width:1.2px,color:#713F12;
  classDef accent fill:#E0E7FF,stroke:#6366F1,stroke-width:1.5px,color:#1E1B4B;
  classDef dim fill:#FFFFFF,stroke:#CBD5E1,stroke-width:1px,color:#111827;
  style CANVAS fill:#ffffff,stroke:#ffffff,stroke-width:0px;
```

## Sequence — Validation Path

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'background': '#ffffff',
    'fontFamily': 'Inter, ui-sans-serif, system-ui',
    'actorBkg': '#E0F2FE',
    'actorBorder': '#0284C7',
    'actorTextColor': '#0C4A6E',
    'sequenceNumberColor': '#ffffff',
    'messageTextColor': '#111827',
    'noteBkgColor': '#ffffff',
    'noteTextColor': '#111827'
  },
  'themeCSS': '.sequenceNumber { fill: #ffffff !important; }'
}}%%
sequenceDiagram
  autonumber
  participant Client
  participant API as FastAPI Endpoint
  participant P as Pydantic Model

  rect rgba(255,255,255,1)
    Client->>API: HTTP POST /resource (JSON body)
    API->>P: Parse & validate
    alt valid data
      P-->>API: Model instance (typed)
      API->>API: Business logic / DB ops
      API-->>Client: 200/201 + response body
    else invalid data
      P-->>API: Validation errors
      API-->>Client: 422 Unprocessable Entity
    end
  end
```


# FastAPI — Request Body (Flow)

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'background': '#ffffff',
    'fontFamily': 'Inter, ui-sans-serif, system-ui'
  },
  'themeCSS': 'svg { background: #ffffff !important; }',
  'flowchart': { 'useMaxWidth': false, 'diagramPadding': 28, 'htmlLabels': true }
}}%%
flowchart LR
  subgraph CANVAS[ ]
    direction LR
    C["Client"]:::dim --> HTTP["HTTP Request<br/>(JSON body)"]:::dim --> API["FastAPI Endpoint"]:::accent
    API --> VALIDATE["Pydantic Model<br/>Parse & Validate"]:::accent

    VALIDATE -- valid --> OK["Typed Python Object<br/>(Model instance)"]:::good --> HANDLER["Endpoint Function<br/>(business logic)"]:::dim --> RESP["HTTP Response<br/>(200/201 + body)"]:::dim
    VALIDATE -- invalid --> ERR["422 Unprocessable Entity<br/>Validation error details"]:::warn
  end

  classDef good fill:#DCFCE7,stroke:#16A34A,stroke-width:1.2px,color:#064E3B;
  classDef warn fill:#FEF9C3,stroke:#CA8A04,stroke-width:1.2px,color:#713F12;
  classDef accent fill:#E0E7FF,stroke:#6366F1,stroke-width:1.5px,color:#1E1B4B;
  classDef dim fill:#FFFFFF,stroke:#CBD5E1,stroke-width:1px,color:#111827;
  style CANVAS fill:#ffffff,stroke:#ffffff,stroke-width:0px;
```

Notes
- Request body is JSON sent by the client to FastAPI.
- Pydantic validates and parses on the server.
- Invalid data returns a clear 422 error response.
- Valid data becomes a typed model instance used by your handler.
