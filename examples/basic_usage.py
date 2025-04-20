"""Basic usage example for the Agent C Session Manager."""

import asyncio
from dotenv import load_dotenv
from zep_cloud.client import AsyncZep

load_dotenv(override=True)

from agent_c_session.repositories.chat_session_repo import ChatSessionRepo
from agent_c_session.models import ChatUser
from agent_c_session.models import ChatMessage


async def main():
    """Demonstrate basic usage of the Agent C Session Manager."""
    # Initialize the repository with Zep Cloud credentials
    zep_client = AsyncZep()

    repo = ChatSessionRepo(zep_client)
    
    # Create a user
    user = await repo.add_chat_user(ChatUser(
        user_id="john_doe",
        email="john@example.com",
        first_name="John",
        last_name="Doe"
    ))
    print(f"Created user: {user.user_id}")
    
    # Create a new session
    session = await repo.new_session(
        username="john_doe",
        title="Getting Started"
    )
    print(f"Created session: {session.session_id} ({session.title})")
    
    # Add messages to the session
    await session.add_message(ChatMessage(
        role="user",
        content="Hello, Agent C!"
    ))
    
    await session.add_message(ChatMessage(
        role="assistant",
        content="Hello! How can I help you today?"
    ))
    
    # Add some metadata
    session.set_meta("topic", "Introduction")
    session.set_managed_meta("application", "language", "en-US")
    
    # Get messages from the session
    messages = await session.get_messages(limit=10)
    print("\nChat history:")
    for msg in messages:
        print(f"{msg.role}: {msg.content}")
    
    # Flush changes to Zep Cloud
    await session.flush()
    print("\nChanges flushed to Zep Cloud")
    
    # Retrieve user sessions
    sessions = await repo.get_user_sessions("john_doe")
    print(f"\nUser has {len(sessions)} sessions")
    
    # Search for sessions
    search_results = await repo.search_user_sessions(
        username="john_doe",
        query="Agent C"
    )
    print(f"Found {len(search_results)} sessions matching search query")


if __name__ == "__main__":
    # Run the example
    asyncio.run(main())