# Request Body:
 The data sent by the client to your FastAPI app in an HTTP request (often in JSON format).


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
