import asyncio
import random
from agents import agents, ItemsHelpers

async def main():
    agent = Agent(
        instructions="You are a helpfull assistant. First, determine how many jokes to tell, then provides jokes.",
        tools=[how_many_jokes],
    )

    result = Runner.run_streamed(agent, input="Hello")

    async for event in result.stream_events():
        if event.item.type == "tool_call_output_item":
            print(f"Tool output: {event.item.output}")
        elif event.item.type == "message_output_item":
            print(ItemHelpers.text_message_output(event.item))

asyncio.run(main()) 