# Agent C Session Manager

The Agent C Session Manager is a critical component of the Agent C framework, providing a robust abstraction layer for managing chat sessions, users, and message history. It integrates with Zep Cloud for persistent storage and provides a clean API for the Agent C runtime.

## Features

- **Chat User Management**: Create, update, and delete chat users with associated metadata
- **Session Management**: Create and manage chat sessions with full message history
- **Metadata Management**: Structured approach to managing metadata at both user and session levels
- **Adapter Architecture**: Flexible adapter system for translating between different message formats
- **Performant Design**: Optimized for high-throughput applications with caching and batch updates
- **Async API**: Fully asynchronous API for integration with modern Python applications

## Installation

```bash
pip install agent-c-session
```

## Quick Start

```python
import asyncio
from agent_c.session.repositories.chat_session_repo import ChatSessionRepo
from agent_c.session.models.chat_user import ChatUser
from agent_c.session.models.chat_session import ChatMessage

async def main():
    # Initialize the repository with Zep Cloud credentials
    repo = ChatSessionRepo(
        zep_api_url="https://api.zep.us/v2",
        zep_api_key="your_api_key_here"
    )
    
    # Create a user
    user = await repo.add_chat_user(ChatUser(
        username="john_doe",
        email="john@example.com",
        first_name="John",
        last_name="Doe"
    ))
    
    # Create a new session
    session = await repo.new_session(
        username="john_doe",
        title="Getting Started"
    )
    
    # Add messages to the session
    await session.add_message(ChatMessage(
        role="user",
        content="Hello, Agent C!"
    ))
    
    await session.add_message(ChatMessage(
        role="assistant",
        content="Hello! How can I help you today?"
    ))
    
    # Get messages from the session
    messages = await session.get_messages(limit=10)
    for msg in messages:
        print(f"{msg.role}: {msg.content}")
    
    # Flush changes to Zep Cloud
    await session.flush()

# Run the example
asyncio.run(main())
```

## Architecture

The Agent C Session Manager consists of several key components:

- **ChatUser**: Model representing a user in the system with metadata management
- **ChatSession**: Model representing a chat session with message history and metadata
- **ChatSessionRepo**: Repository for managing users and sessions with Zep Cloud
- **Adapters**: System for translating between different message formats

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/agentc/session.git
cd session

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev,test]"
```

### Testing

```bash
python -m pytest
```

### Code Quality

```bash
# Run formatters
black src tests
isort src tests

# Run linters and type checking
flake8 src tests
mypy src tests
```

## License

MIT